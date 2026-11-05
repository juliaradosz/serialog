"""SeenIt — serwer z kontami użytkowników.

Uruchomienie lokalne:  python server.py  (albo start.bat)  -> http://localhost:8000
Hosting (np. PythonAnywhere): plik WSGI z linią  from server import application
Zmienne środowiskowe:
  PORT  — port (domyślnie 8000)
  HOST  — adres (domyślnie 127.0.0.1; 0.0.0.0 = dostęp z innych urządzeń w sieci domowej)

Tylko biblioteka standardowa Pythona. Dane: plik serialog.db (SQLite) obok tego pliku.
Dane o filmach i serialach: TMDB — klucz API w pliku tmdb_klucz.txt (serwer pośredniczy
w zapytaniach, więc klucz nigdy nie trafia do przeglądarki).
"""
import hashlib
import hmac
import json
import unicodedata
import math
import random
import os
import re
import secrets
import sqlite3
import time
import urllib.error
import urllib.parse
import urllib.request
from http.cookies import SimpleCookie
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(ROOT, 'serialog.db')
TMDB_KEY_FILE = os.path.join(ROOT, 'tmdb_klucz.txt')
TMDB_API = 'https://api.themoviedb.org/3/'
# tylko te ścieżki TMDB można odpytać przez serwer
TMDB_PATH_RE = re.compile(
    r'^(search/(tv|movie)|discover/(tv|movie)|trending/(tv|movie)/(day|week)|genre/(tv|movie)/list'
    r'|(tv|movie)/\d+|(tv|movie)/\d+/(recommendations|similar)|tv/\d+/season/\d+(/episode/\d+)?'
    r'|movie/(now_playing|upcoming|popular)|person/\d+|find/[\w.-]+|watch/providers/(tv|movie))$')
TMDB_CACHE_SECONDS = 30 * 60
tmdb_cache = {}  # url -> (wygasa, status, treść)
# serwujemy tylko aplikację (i jej ikony), nic więcej — baza, klucz i kod serwera są niedostępne
STATIC = {'/': 'index.html', '/index.html': 'index.html', '/manifest.json': 'manifest.json',
          '/icon-180.png': 'icon-180.png', '/icon-192.png': 'icon-192.png', '/icon-512.png': 'icon-512.png',
          '/icon-maskable.png': 'icon-maskable.png'}
STATIC_TYPES = {'.html': 'text/html; charset=utf-8', '.json': 'application/manifest+json', '.png': 'image/png'}
SESSION_SECONDS = 30 * 24 * 3600
MAX_BODY = 5 * 1024 * 1024
USERNAME_RE = re.compile(r'^[\w.\-]{3,30}$')


def name_key(name):
    """Postać nazwy do porównań: liczy się tylko wielkość liter („Julka” = „julka”, „Łukasz” = „łukasz”).
    Polskie znaki, kropki, podkreślenia, myślniki i cyfry rozróżniają nazwy („jul.ka”, „júlka”, „ju1ka” to inne konta)."""
    return unicodedata.normalize('NFC', str(name)).casefold()
failed_logins = {}  # ip -> [czasy nieudanych prób]


def db():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def init_db():
    with db() as con:
        con.executescript('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE COLLATE NOCASE,
                salt BLOB NOT NULL,
                pw_hash BLOB NOT NULL,
                created INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS sessions (
                token TEXT PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id),
                expires INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS states (
                user_id INTEGER PRIMARY KEY REFERENCES users(id),
                data TEXT NOT NULL,
                updated INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS friends (
                from_id INTEGER NOT NULL REFERENCES users(id),
                to_id INTEGER NOT NULL REFERENCES users(id),
                accepted INTEGER NOT NULL DEFAULT 0,
                created INTEGER NOT NULL,
                PRIMARY KEY (from_id, to_id));
            -- wspólna lista „Na później razem” dwojga znajomych (a_id < b_id)
            CREATE TABLE IF NOT EXISTS shared_later (
                a_id INTEGER NOT NULL REFERENCES users(id),
                b_id INTEGER NOT NULL REFERENCES users(id),
                kind TEXT NOT NULL,
                tid INTEGER NOT NULL,
                title TEXT NOT NULL,
                poster TEXT NOT NULL DEFAULT '',
                added_by INTEGER NOT NULL,
                created INTEGER NOT NULL,
                PRIMARY KEY (a_id, b_id, kind, tid));
        ''')



def hash_password(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 200_000)


def tmdb_key():
    try:
        with open(TMDB_KEY_FILE, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    return line
    except OSError:
        pass
    return None


def tmdb_fetch(path, query):
    """Pobiera dane z TMDB (z pamięcią podręczną). Zwraca (status, bajty JSON)."""
    key = tmdb_key()
    if not key:
        return 503, json.dumps({'error': 'Brak klucza TMDB w pliku tmdb_klucz.txt'}).encode()
    params = [(k, v) for k, v in urllib.parse.parse_qsl(query) if k != 'api_key']
    if not any(k == 'language' for k, _ in params):
        params.append(('language', 'pl-PL'))
    url = TMDB_API + path + '?' + urllib.parse.urlencode(sorted(params))
    hit = tmdb_cache.get(url)
    if hit and hit[0] > time.time():
        return hit[1], hit[2]
    headers = {'Accept': 'application/json'}
    full = url
    if len(key) == 32:  # klucz API v3
        full += '&api_key=' + urllib.parse.quote(key)
    else:  # token dostępu v4
        headers['Authorization'] = 'Bearer ' + key
    try:
        with urllib.request.urlopen(urllib.request.Request(full, headers=headers), timeout=20) as r:
            status, body = r.status, r.read()
    except urllib.error.HTTPError as e:
        status, body = e.code, e.read()
    except (urllib.error.URLError, TimeoutError) as e:
        return 502, json.dumps({'error': f'TMDB niedostępne: {e}'}).encode()
    if status == 200:
        if len(tmdb_cache) > 3000:
            tmdb_cache.clear()
        tmdb_cache[url] = (time.time() + TMDB_CACHE_SECONDS, status, body)
    return status, body


def too_many_failures(ip):
    now = time.time()
    recent = [t for t in failed_logins.get(ip, []) if now - t < 300]
    failed_logins[ip] = recent
    return len(recent) >= 10


# ---------- obsługa zapytań (wspólna dla serwera lokalnego i WSGI/PythonAnywhere) ----------
class Request:
    def __init__(self, method, path, query, headers, body, ip, https):
        self.method, self.path, self.query = method, path, query
        self.headers, self.body, self.ip, self.https = headers, body, ip, https


def json_response(code, obj, cookie=None):
    headers = [('Content-Type', 'application/json; charset=utf-8'), ('Cache-Control', 'no-store')]
    if cookie:
        headers.append(('Set-Cookie', cookie))
    return code, headers, json.dumps(obj, ensure_ascii=False).encode('utf-8')


def read_json(req):
    if not req.headers.get('content-type', '').startswith('application/json'):
        return None  # wymagany JSON — formularze z obcych stron nie przejdą
    if not req.body or len(req.body) > MAX_BODY:
        return None
    try:
        return json.loads(req.body)
    except ValueError:
        return None


def session_token(req):
    cookie = SimpleCookie(req.headers.get('cookie', ''))
    return cookie['sid'].value if 'sid' in cookie else None


# administrator (widzi rzeczy techniczne: eksport/import, czyszczenie danych, sprawdzanie z Wikipedią…):
# pierwsze konto na serwerze albo nazwy z zmiennej środowiskowej SERIALOG_ADMINS (oddzielone przecinkami)
ADMINS = {n.strip().lower() for n in (os.environ.get('SERIALOG_ADMINS') or 'julkar8').split(',') if n.strip()}


ADMINS_FILE = os.path.join(ROOT, 'admini.txt')  # jedna nazwa w linii (plik tylko na serwerze, nie w repozytorium)


def admins_from_file():
    try:
        with open(ADMINS_FILE, encoding='utf-8') as f:
            return {l.strip().lower() for l in f if l.strip() and not l.strip().startswith('#')}
    except OSError:
        return set()


def is_admin(user_id, username):
    name = (username or '').lower()
    return user_id == 1 or name in ADMINS or name in admins_from_file()


def me_info(user_id, username):
    return {'username': username, 'admin': True} if is_admin(user_id, username) else {'username': username}


def current_user(req):
    token = session_token(req)
    if not token:
        return None
    with db() as con:
        return con.execute(
            'SELECT users.id, users.username FROM sessions JOIN users ON users.id = sessions.user_id '
            'WHERE sessions.token = ? AND sessions.expires > ?', (token, int(time.time()))).fetchone()


def session_cookie(req, token, max_age):
    # przez HTTPS (hosting) ciasteczko jest dodatkowo „Secure” — nie wyjdzie przez nieszyfrowane połączenie
    return f'sid={token}; HttpOnly; SameSite=Lax; Path=/; Max-Age={max_age}' + ('; Secure' if req.https else '')


def start_session(req, user_id):
    token = secrets.token_urlsafe(32)
    with db() as con:
        con.execute('DELETE FROM sessions WHERE expires < ?', (int(time.time()),))
        con.execute('INSERT INTO sessions VALUES (?, ?, ?)', (token, user_id, int(time.time()) + SESSION_SECONDS))
    return session_cookie(req, token, SESSION_SECONDS)


# ---------- znajomi ----------
def user_by_name(con, name):
    return con.execute('SELECT id, username FROM users WHERE username = ?', (str(name).strip(),)).fetchone()


def friend_lists(con, uid):
    rows = con.execute('SELECT f.from_id, f.to_id, f.accepted, a.username AS a_name, b.username AS b_name FROM friends f '
                       'JOIN users a ON a.id = f.from_id JOIN users b ON b.id = f.to_id WHERE f.from_id = ? OR f.to_id = ?', (uid, uid)).fetchall()
    out = {'friends': [], 'incoming': [], 'outgoing': []}
    for r in rows:
        other = r['b_name'] if r['from_id'] == uid else r['a_name']
        if r['accepted']:
            out['friends'].append(other)
        elif r['to_id'] == uid:
            out['incoming'].append(other)
        else:
            out['outgoing'].append(other)
    for k in out:
        out[k].sort(key=str.lower)
    names = out['friends'] + out['incoming'] + out['outgoing']
    out['avatars'] = {}
    if names:
        rows = con.execute('SELECT u.username, s.data FROM users u JOIN states s ON s.user_id = u.id WHERE u.username IN (%s)' % ','.join('?' * len(names)), names).fetchall()
        for r in rows:
            a = avatar_of(json.loads(r['data']))
            if a:
                out['avatars'][r['username']] = a
    return out


def avatar_of(state):
    a = (state.get('prefs') or {}).get('avatar')
    return a if isinstance(a, str) and a.startswith('data:image/') and len(a) < 400000 else None


def shared_later_list(con, me, other):
    a, b = sorted((me, other))
    rows = con.execute('SELECT kind, tid, title, poster, added_by, created FROM shared_later WHERE a_id = ? AND b_id = ? ORDER BY created DESC', (a, b)).fetchall()
    return [{'type': r['kind'], 'id': r['tid'], 'title': r['title'], 'poster': r['poster'], 'mine': r['added_by'] == me, 't': r['created']} for r in rows]


def are_friends(con, a, b):
    return con.execute('SELECT 1 FROM friends WHERE accepted = 1 AND ((from_id = ? AND to_id = ?) OR (from_id = ? AND to_id = ?))', (a, b, b, a)).fetchone()


def friend_likes(state):
    """Gust znajomego do wspólnych propozycji: tytuły, które lubi najbardziej (w losowej kolejności),
    i ulubione gatunki (od -1 do 1). Same oceny, recenzje i notatki nie wychodzą z serwera."""
    watched = state.get('watched') or {}
    favs = state.get('favs') or {}
    per_show = {}
    for w in watched.values():
        per_show[str(w.get('s'))] = per_show.get(str(w.get('s')), 0) + 1 + len(w.get('rw') or [])
    seeds, g = [], {'tv': {}, 'movie': {}}

    def add_g(kind, names, v):
        for n in names or []:
            g[kind][n] = g[kind].get(n, 0) + v
    for s in (state.get('shows') or {}).values():
        r, eps = s.get('rating') or 0, per_show.get(str(s.get('id')), 0)
        fav = ('tv:%s' % s.get('id')) in favs
        add_g('tv', s.get('genres'), -1.5 if s.get('dropped') else .4 + math.log2(1 + eps) * .5 + ((r - 3) * .7 if r else 0) + (1.5 if fav else 0))
        if s.get('dropped') or (r and r <= 2) or not (eps or fav):
            continue
        seeds.append((.6 + math.log2(1 + eps) * .6 + ((r - 3) * .8 if r else 0) + (2 if fav else 0), {'type': 'tv', 'id': s.get('id'), 'title': s.get('name')}))
    for m in (state.get('movies') or {}).values():
        r, fav, seen = m.get('rating') or 0, ('movie:%s' % m.get('id')) in favs, m.get('status') == 'seen'
        add_g('movie', m.get('genres'), (1 if seen else .5) + ((r - 3) * .7 if r else 0) + (1.5 if fav else 0) + len(m.get('rw') or []) * .5)
        if not seen or (r and r <= 2):
            continue
        seeds.append((1.6 + ((r - 3) * .8 if r else 0) + (2 if fav else 0) + len(m.get('rw') or []) * .5, {'type': 'movie', 'id': m.get('id'), 'title': m.get('title')}))
    for k in g:
        mx = max([1] + [abs(v) for v in g[k].values()])
        g[k] = {n: round(v / mx, 1) for n, v in g[k].items()}
    top = [x for _, x in sorted(seeds, key=lambda p: -p[0])[:16]]
    random.shuffle(top)
    return {'likes': top, 'taste': g}


def friend_profile(state):
    """Co widzi znajomy: listy i liczby — bez recenzji, ocen, notatek i reakcji (te są prywatne)."""
    watched = state.get('watched') or {}
    per_show, minutes = {}, 0
    for w in watched.values():
        per_show[w.get('s')] = per_show.get(w.get('s'), 0) + 1 + len(w.get('rw') or [])
        minutes += (w.get('m') or 0) * (1 + len(w.get('rw') or []))
    shows = [{'id': x.get('id'), 'name': x.get('name'), 'poster': x.get('poster'), 'eps': per_show.get(x.get('id'), per_show.get(str(x.get('id')), 0)),
              'dropped': bool(x.get('dropped'))} for x in (state.get('shows') or {}).values()]
    movies = [{'id': m.get('id'), 'title': m.get('title'), 'poster': m.get('poster'), 'year': m.get('year'), 'status': m.get('status'), 'seenAt': m.get('seenAt')}
              for m in (state.get('movies') or {}).values()]
    for m in movies:
        if m['status'] == 'seen':
            minutes += next((x.get('runtime') or 0 for x in (state.get('movies') or {}).values() if x.get('id') == m['id']), 0)
    favs = [{'type': f.get('type'), 'id': f.get('id'), 'title': f.get('title'), 'poster': f.get('poster')} for f in (state.get('favs') or {}).values()]
    return {'shows': shows, 'movies': movies, 'favs': favs, 'episodes': sum(per_show.values()), 'minutes': minutes, 'avatar': avatar_of(state), **friend_likes(state)}


def static_file(path):
    name = STATIC[path]
    with open(os.path.join(ROOT, name), 'rb') as f:
        body = f.read()
    ext = os.path.splitext(name)[1]
    cache = 'no-cache' if ext in ('.html', '.json') else 'public, max-age=604800'
    return 200, [('Content-Type', STATIC_TYPES[ext]), ('Cache-Control', cache)], body


db_ready = False


def handle(req):
    global db_ready
    if not db_ready:
        init_db()
        db_ready = True
    try:
        return route(req)
    except Exception as e:  # nie pokazujemy szczegółów błędu na zewnątrz
        print('Błąd:', repr(e))
        return json_response(500, {'error': 'Błąd serwera'})


def route(req):
    path, query = req.path, req.query
    if req.method == 'GET':
        if path.startswith('/api/tmdb/'):
            if not current_user(req):
                return json_response(401, {'error': 'Niezalogowany'})
            sub = path[len('/api/tmdb/'):]
            if not TMDB_PATH_RE.match(sub):
                return json_response(404, {'error': 'Nieobsługiwane zapytanie'})
            status, body = tmdb_fetch(sub, query)
            return status, [('Content-Type', 'application/json; charset=utf-8'), ('Cache-Control', 'private, max-age=600')], body
        if path == '/api/friends':
            user = current_user(req)
            if not user:
                return json_response(401, {'error': 'Niezalogowany'})
            with db() as con:
                return json_response(200, friend_lists(con, user['id']))
        if path == '/api/friends/profile':
            user = current_user(req)
            if not user:
                return json_response(401, {'error': 'Niezalogowany'})
            name = dict(urllib.parse.parse_qsl(query)).get('u', '')
            with db() as con:
                other = user_by_name(con, name)
                friend = bool(other and are_friends(con, user['id'], other['id']))
                # administrator może podejrzeć każde konto (tak jak znajomy: listy, bez ocen, recenzji i notatek)
                if not other or not (friend or is_admin(user['id'], user['username'])):
                    return json_response(403, {'error': 'Ten profil widzą tylko znajomi'})
                row = con.execute('SELECT data FROM states WHERE user_id = ?', (other['id'],)).fetchone()
            data = friend_profile(json.loads(row['data']) if row else {})
            data['username'] = other['username']
            data['friend'] = friend
            return json_response(200, data)
        if path == '/api/admin/users':  # lista kont — tylko dla administratora
            user = current_user(req)
            if not user or not is_admin(user['id'], user['username']):
                return json_response(404, {'error': 'Nie znaleziono'})
            with db() as con:
                rows = con.execute('SELECT users.id, users.username, users.created, states.updated, states.data FROM users '
                                   'LEFT JOIN states ON states.user_id = users.id ORDER BY users.created DESC').fetchall()
                fr = {}
                for r in con.execute('SELECT from_id, to_id FROM friends WHERE accepted = 1'):
                    fr[r['from_id']] = fr.get(r['from_id'], 0) + 1
                    fr[r['to_id']] = fr.get(r['to_id'], 0) + 1
            users = []
            for r in rows:
                try:
                    st = json.loads(r['data']) if r['data'] else {}
                except ValueError:
                    st = {}
                users.append({'username': r['username'], 'created': r['created'], 'active': r['updated'], 'friends': fr.get(r['id'], 0),
                              'shows': len(st.get('shows') or {}), 'movies': len(st.get('movies') or {}), 'avatar': avatar_of(st),
                              'admin': is_admin(r['id'], r['username']), 'me': r['id'] == user['id']})
            return json_response(200, {'users': users})
        if path == '/api/friends/later':
            user = current_user(req)
            if not user:
                return json_response(401, {'error': 'Niezalogowany'})
            name = dict(urllib.parse.parse_qsl(query)).get('u', '')
            with db() as con:
                other = user_by_name(con, name)
                if not other or not are_friends(con, user['id'], other['id']):
                    return json_response(403, {'error': 'Tylko dla znajomych'})
                return json_response(200, {'items': shared_later_list(con, user['id'], other['id'])})
        if path == '/api/config':
            return json_response(200, {'tmdb': bool(tmdb_key())})
        if path == '/api/me':
            user = current_user(req)
            return json_response(200, me_info(user['id'], user['username'])) if user else json_response(401, {'error': 'Niezalogowany'})
        if path == '/api/state':
            user = current_user(req)
            if not user:
                return json_response(401, {'error': 'Niezalogowany'})
            with db() as con:
                row = con.execute('SELECT data FROM states WHERE user_id = ?', (user['id'],)).fetchone()
            return json_response(200, json.loads(row['data']) if row else {})
        if path in STATIC:
            return static_file(path)
        return 404, [('Content-Type', 'text/plain; charset=utf-8')], 'Nie znaleziono'.encode('utf-8')

    if req.method == 'POST':
        if path == '/api/logout':
            token = session_token(req)
            if token:
                with db() as con:
                    con.execute('DELETE FROM sessions WHERE token = ?', (token,))
            return json_response(200, {'ok': True}, session_cookie(req, '', 0))
        if path == '/api/friends/later':  # dopisanie / usunięcie tytułu ze wspólnej listy „Na później razem”
            user = current_user(req)
            if not user:
                return json_response(401, {'error': 'Niezalogowany'})
            data = read_json(req)
            if not isinstance(data, dict) or data.get('type') not in ('tv', 'movie') or data.get('op') not in ('add', 'remove'):
                return json_response(400, {'error': 'Nieprawidłowe dane'})
            try:
                tid = int(data.get('id'))
            except (TypeError, ValueError):
                return json_response(400, {'error': 'Nieprawidłowe dane'})
            title = str(data.get('title') or '')[:200]
            poster = str(data.get('poster') or '')
            if not poster.startswith('https://image.tmdb.org/') or len(poster) > 300:
                poster = ''
            with db() as con:
                other = user_by_name(con, data.get('username', ''))
                if not other or not are_friends(con, user['id'], other['id']):
                    return json_response(403, {'error': 'Tylko dla znajomych'})
                a, b = sorted((user['id'], other['id']))
                if data['op'] == 'remove':
                    con.execute('DELETE FROM shared_later WHERE a_id = ? AND b_id = ? AND kind = ? AND tid = ?', (a, b, data['type'], tid))
                elif title:
                    n = con.execute('SELECT COUNT(*) FROM shared_later WHERE a_id = ? AND b_id = ?', (a, b)).fetchone()[0]
                    if n >= 300:
                        return json_response(400, {'error': 'Wspólna lista jest pełna (300 tytułów)'})
                    con.execute('INSERT OR IGNORE INTO shared_later VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (a, b, data['type'], tid, title, poster, user['id'], int(time.time())))
                return json_response(200, {'items': shared_later_list(con, user['id'], other['id'])})
        if path in ('/api/friends/add', '/api/friends/accept', '/api/friends/remove'):
            user = current_user(req)
            if not user:
                return json_response(401, {'error': 'Niezalogowany'})
            data = read_json(req)
            if not isinstance(data, dict):
                return json_response(400, {'error': 'Nieprawidłowe dane'})
            with db() as con:
                other = user_by_name(con, data.get('username', ''))
                if not other:
                    return json_response(404, {'error': 'Nie ma użytkownika o takiej nazwie'})
                me, them = user['id'], other['id']
                if me == them:
                    return json_response(400, {'error': 'Nie możesz dodać samej/samego siebie'})
                if path == '/api/friends/remove':  # usunięcie znajomego, odrzucenie lub cofnięcie zaproszenia
                    con.execute('DELETE FROM friends WHERE (from_id = ? AND to_id = ?) OR (from_id = ? AND to_id = ?)', (me, them, them, me))
                    con.execute('DELETE FROM shared_later WHERE a_id = ? AND b_id = ?', tuple(sorted((me, them))))
                elif path == '/api/friends/accept':
                    con.execute('UPDATE friends SET accepted = 1 WHERE from_id = ? AND to_id = ?', (them, me))
                else:
                    if con.execute('SELECT 1 FROM friends WHERE from_id = ? AND to_id = ?', (them, me)).fetchone():
                        con.execute('UPDATE friends SET accepted = 1 WHERE from_id = ? AND to_id = ?', (them, me))  # wzajemne zaproszenie = znajomi
                    elif not con.execute('SELECT 1 FROM friends WHERE from_id = ? AND to_id = ?', (me, them)).fetchone():
                        con.execute('INSERT INTO friends VALUES (?, ?, 0, ?)', (me, them, int(time.time())))
                return json_response(200, friend_lists(con, me))
        if path not in ('/api/login', '/api/register'):
            return json_response(404, {'error': 'Nie znaleziono'})
        data = read_json(req)
        if not isinstance(data, dict):
            return json_response(400, {'error': 'Nieprawidłowe dane'})
        username = str(data.get('username', '')).strip()
        password = str(data.get('password', ''))
        if path == '/api/register':
            if not USERNAME_RE.match(username):
                return json_response(400, {'error': 'Nazwa: 3–30 znaków (litery, cyfry, _ . -)'})
            if len(password) < 6:
                return json_response(400, {'error': 'Hasło musi mieć co najmniej 6 znaków'})
            salt = secrets.token_bytes(16)
            key = name_key(username)
            with db() as con:
                if any(name_key(r['username']) == key for r in con.execute('SELECT username FROM users')):
                    return json_response(409, {'error': 'Ta nazwa użytkownika jest już zajęta'})
            try:
                with db() as con:
                    cur = con.execute('INSERT INTO users (username, salt, pw_hash, created) VALUES (?, ?, ?, ?)',
                                      (username, salt, hash_password(password, salt), int(time.time())))
                    user_id = cur.lastrowid
            except sqlite3.IntegrityError:
                return json_response(409, {'error': 'Ta nazwa użytkownika jest już zajęta'})
            return json_response(200, me_info(user_id, username), start_session(req, user_id))
        # logowanie
        if too_many_failures(req.ip):
            return json_response(429, {'error': 'Zbyt wiele nieudanych prób. Spróbuj za kilka minut.'})
        with db() as con:
            user = con.execute('SELECT id, username, salt, pw_hash FROM users WHERE username = ?', (username,)).fetchone()
        if not user or not hmac.compare_digest(hash_password(password, user['salt']), user['pw_hash']):
            failed_logins.setdefault(req.ip, []).append(time.time())
            return json_response(401, {'error': 'Nieprawidłowa nazwa użytkownika lub hasło'})
        return json_response(200, me_info(user['id'], user['username']), start_session(req, user['id']))

    if req.method == 'PUT' and path == '/api/state':
        user = current_user(req)
        if not user:
            return json_response(401, {'error': 'Niezalogowany'})
        data = read_json(req)
        if not isinstance(data, dict):
            return json_response(400, {'error': 'Nieprawidłowe dane'})
        with db() as con:
            con.execute('INSERT INTO states VALUES (?, ?, ?) ON CONFLICT(user_id) DO UPDATE SET data = excluded.data, updated = excluded.updated',
                        (user['id'], json.dumps(data, ensure_ascii=False), int(time.time())))
        return json_response(200, {'ok': True})

    return 405, [('Content-Type', 'text/plain; charset=utf-8')], 'Niedozwolona metoda'.encode('utf-8')


# ---------- uruchomienie lokalne (start.bat / python server.py) ----------
class Handler(BaseHTTPRequestHandler):
    server_version = 'SeenIt'

    def run(self):
        path, _, query = self.path.partition('?')
        length = int(self.headers.get('Content-Length') or 0)
        body = self.rfile.read(length) if 0 < length <= MAX_BODY else b''
        headers = {k.lower(): v for k, v in self.headers.items()}
        status, out_headers, out = handle(Request(self.command, path, query, headers, body, self.client_address[0], False))
        self.send_response(status)
        for k, v in out_headers:
            self.send_header(k, v)
        self.send_header('Content-Length', str(len(out)))
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(out)

    do_GET = do_POST = do_PUT = do_HEAD = do_DELETE = run


# ---------- WSGI — hosting (np. PythonAnywhere: w pliku WSGI „from server import application”) ----------
def application(environ, start_response):
    headers = {k[5:].replace('_', '-').lower(): v for k, v in environ.items() if k.startswith('HTTP_')}
    for k in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
        if environ.get(k):
            headers[k.replace('_', '-').lower()] = environ[k]
    length = int(environ.get('CONTENT_LENGTH') or 0)
    body = environ['wsgi.input'].read(length) if 0 < length <= MAX_BODY else b''
    # za pośrednikiem hostingu prawdziwy adres klienta jest w nagłówku
    ip = headers.get('x-real-ip') or headers.get('x-forwarded-for', '').split(',')[0].strip() or environ.get('REMOTE_ADDR', '')
    https = environ.get('wsgi.url_scheme') == 'https' or headers.get('x-forwarded-proto') == 'https'
    status, out_headers, out = handle(Request(environ['REQUEST_METHOD'], environ.get('PATH_INFO') or '/', environ.get('QUERY_STRING', ''), headers, body, ip, https))
    start_response(f'{status} {HTTPStatus(status).phrase}', out_headers + [('Content-Length', str(len(out)))])
    return [out if environ['REQUEST_METHOD'] != 'HEAD' else b'']


if __name__ == '__main__':
    init_db()
    host, port = os.environ.get('HOST', '127.0.0.1'), int(os.environ.get('PORT', '8000'))
    print(f'SeenIt działa: http://{"localhost" if host in ("127.0.0.1", "0.0.0.0") else host}:{port}  (Ctrl+C zatrzymuje)')
    ThreadingHTTPServer((host, port), Handler).serve_forever()
