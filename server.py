"""SeriaLog — serwer z kontami użytkowników.

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
import os
import re
import secrets
import sqlite3
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta
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
    r'|movie/(now_playing|upcoming|popular)|person/\d+|find/[\w.-]+)$')
TMDB_CACHE_SECONDS = 30 * 60
tmdb_cache = {}  # url -> (wygasa, status, treść)
# serwujemy tylko aplikację (i jej ikony), nic więcej — baza, klucz i kod serwera są niedostępne
STATIC = {'/': 'index.html', '/index.html': 'index.html', '/manifest.json': 'manifest.json',
          '/icon-180.png': 'icon-180.png', '/icon-192.png': 'icon-192.png', '/icon-512.png': 'icon-512.png'}
STATIC_TYPES = {'.html': 'text/html; charset=utf-8', '.json': 'application/manifest+json', '.png': 'image/png'}
SESSION_SECONDS = 30 * 24 * 3600
MAX_BODY = 5 * 1024 * 1024
USERNAME_RE = re.compile(r'^[\w.\-]{3,30}$')
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


# ---------- repertuar kin (Cinema City, Multikino, Helios) ----------
# Publiczne dane repertuarowe z serwisów sieci kin; serwer ujednolica je i trzyma w pamięci podręcznej.
CC_API = 'https://www.cinema-city.pl/pl/data-api-service/v1/quickbook/10103/'
MK_API = 'https://www.multikino.pl/api/microservice/showings/'
HE_API = 'https://restapi.helios.pl/api/'
CINEMA_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) SeriaLog/1.0 (osobisty planer seansow)'
http_cache = {}  # url -> (wygasa, dane)
CINEMA_KEY_RE = re.compile(r'^(cc|mk|he):[\w-]{1,40}$')
DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
CC_ATTRS = {'2d': '2D', '3d': '3D', 'imax': 'IMAX', '4dx': '4DX', 'screenx': 'ScreenX', 'dubbed': 'dubbing', 'subbed': 'napisy', 'vip': 'VIP', 'dolby-atmos': 'Dolby Atmos'}
HE_SPEAK = {'NAP': 'napisy', 'DUB': 'dubbing', 'LEK': 'lektor', 'ORG': 'wersja oryginalna', 'PL': 'polski'}


def get_json(url, ttl):
    hit = http_cache.get(url)
    if hit and hit[0] > time.time():
        return hit[1]
    req = urllib.request.Request(url, headers={'User-Agent': CINEMA_UA, 'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = json.loads(r.read())
    if len(http_cache) > 2000:
        http_cache.clear()
    http_cache[url] = (time.time() + ttl, data)
    return data


def all_cinemas():
    until = (date.today() + timedelta(days=60)).isoformat()
    out = []
    try:
        for c in get_json(f'{CC_API}cinemas/with-event/until/{until}?attr=&lang=pl_PL', 12 * 3600)['body']['cinemas']:
            a = c.get('addressInfo') or {}
            out.append({'key': f"cc:{c['id']}", 'chain': 'Cinema City', 'name': c['displayName'], 'city': a.get('city') or c['displayName'], 'address': a.get('address1') or '', 'url': c.get('link') or 'https://www.cinema-city.pl/'})
    except Exception:
        pass
    try:
        for c in get_json(HE_API + 'cinema', 12 * 3600):
            out.append({'key': f"he:{c['id']}", 'chain': 'Helios', 'name': c['name'], 'city': c.get('city') or '', 'address': c.get('street') or '', 'url': 'https://www.helios.pl/'})
    except Exception:
        pass
    try:
        cities = sorted({c['city'] for c in out if c['city']}, key=len, reverse=True)
        for g in get_json(MK_API + 'cinemas', 12 * 3600)['result']:
            for c in g['cinemas']:
                name = c['cinemaName']
                city = next((x for x in cities if name == x or name.startswith(x + ' ')), name.split(' ')[0] if ' ' in name else name)
                out.append({'key': f"mk:{c['cinemaId']}", 'chain': 'Multikino', 'name': name, 'city': city, 'address': '', 'url': c.get('whatsOnUrl') or 'https://www.multikino.pl/'})
    except Exception:
        pass
    return sorted(out, key=lambda c: (c['city'], c['chain'], c['name']))


def showtimes(key, day):
    chain, cid = key.split(':', 1)
    films = {}
    if chain == 'cc':
        body = get_json(f'{CC_API}film-events/in-cinema/{cid}/at-date/{day}?attr=&lang=pl_PL', 15 * 60)['body']
        for f in body.get('films', []):
            films[f['id']] = {'title': f['name'], 'year': f.get('releaseYear'), 'length': f.get('length'), 'poster': f.get('posterLink'), 'url': f.get('link'), 'times': []}
        for e in body.get('events', []):
            if e['filmId'] in films:
                films[e['filmId']]['times'].append({'t': e['eventDateTime'][11:16], 'url': e.get('bookingLink'),
                                                     'attrs': [CC_ATTRS[a] for a in e.get('attributeIds', []) if a in CC_ATTRS]})
    elif chain == 'mk':
        for f in get_json(f'{MK_API}cinemas/{cid}/films', 15 * 60).get('result', []):
            times = []
            for g in f.get('showingGroups', []):
                if g.get('date', '')[:10] != day:
                    continue
                for s in g.get('sessions', []):
                    attrs = [a.get('shortName', '') for a in s.get('attributes', []) if a.get('attributeType') != 'Movie'][:3]
                    times.append({'t': s['startTime'][11:16], 'url': 'https://www.multikino.pl' + s.get('bookingUrl', ''),
                                  'attrs': [a if a in ('2D', '3D', 'IMAX', '4DX') else a.lower() for a in attrs if a]})
            if times:
                films[f['filmId']] = {'title': f.get('filmTitle'), 'original': f.get('originalTitle') or None, 'year': (f.get('releaseDate') or '')[:4],
                                      'length': f.get('runningTime'), 'poster': f.get('posterImageSrc'), 'url': f.get('filmUrl'), 'times': times}
    elif chain == 'he':
        rows = get_json(f'{HE_API}cinema/{cid}/screening?dateTimeFrom={day}T00:00:00&dateTimeTo={day}T23:59:59', 15 * 60)
        ids = sorted({r['movieId'] for r in rows})
        with ThreadPoolExecutor(8) as ex:
            movies = dict(zip(ids, ex.map(lambda i: get_json(f'{HE_API}movie/{i}', 12 * 3600), ids)))
        for r in rows:
            m = movies.get(r['movieId']) or {}
            f = films.setdefault(r['movieId'], {'title': m.get('title'), 'original': m.get('originalTitle') or None, 'year': m.get('yearOfProduction'),
                                                'length': m.get('duration'), 'poster': (m.get('posters') or [None])[0], 'url': 'https://www.helios.pl/', 'times': []})
            f['times'].append({'t': r['screeningTimeFrom'][11:16], 'url': 'https://www.helios.pl/',
                               'attrs': [x for x in (r.get('printType'), HE_SPEAK.get((r.get('speakingType') or '').upper())) if x]})
    result = [f for f in films.values() if f['times'] and f['title']]
    for f in result:
        f['times'].sort(key=lambda x: x['t'])
    return sorted(result, key=lambda f: f['times'][0]['t'])


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
        if path in ('/api/kina', '/api/seanse'):
            if not current_user(req):
                return json_response(401, {'error': 'Niezalogowany'})
            if path == '/api/kina':
                return json_response(200, all_cinemas())
            q = dict(urllib.parse.parse_qsl(query))
            key, day = q.get('kino', ''), q.get('data', '')
            if not CINEMA_KEY_RE.match(key) or not DATE_RE.match(day):
                return json_response(400, {'error': 'Nieprawidłowe kino lub data'})
            try:
                return json_response(200, showtimes(key, day))
            except urllib.error.HTTPError as e:
                if e.code in (401, 403):  # sieć nie udostępnia publicznie repertuaru tego kina
                    return json_response(403, {'error': 'Ta sieć nie udostępnia publicznie repertuaru tego kina.'})
                return json_response(502, {'error': f'Nie udało się pobrać repertuaru: {e}'})
            except Exception:
                return json_response(502, {'error': 'Ten serwer nie ma dostępu do stron kin (np. darmowy hosting blokuje te strony).'})
        if path == '/api/config':
            return json_response(200, {'tmdb': bool(tmdb_key())})
        if path == '/api/me':
            user = current_user(req)
            return json_response(200, {'username': user['username']}) if user else json_response(401, {'error': 'Niezalogowany'})
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
            try:
                with db() as con:
                    cur = con.execute('INSERT INTO users (username, salt, pw_hash, created) VALUES (?, ?, ?, ?)',
                                      (username, salt, hash_password(password, salt), int(time.time())))
                    user_id = cur.lastrowid
            except sqlite3.IntegrityError:
                return json_response(409, {'error': 'Ta nazwa użytkownika jest już zajęta'})
            return json_response(200, {'username': username}, start_session(req, user_id))
        # logowanie
        if too_many_failures(req.ip):
            return json_response(429, {'error': 'Zbyt wiele nieudanych prób. Spróbuj za kilka minut.'})
        with db() as con:
            user = con.execute('SELECT id, username, salt, pw_hash FROM users WHERE username = ?', (username,)).fetchone()
        if not user or not hmac.compare_digest(hash_password(password, user['salt']), user['pw_hash']):
            failed_logins.setdefault(req.ip, []).append(time.time())
            return json_response(401, {'error': 'Nieprawidłowa nazwa użytkownika lub hasło'})
        return json_response(200, {'username': user['username']}, start_session(req, user['id']))

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
    server_version = 'SeriaLog'

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
    print(f'SeriaLog działa: http://{"localhost" if host in ("127.0.0.1", "0.0.0.0") else host}:{port}  (Ctrl+C zatrzymuje)')
    ThreadingHTTPServer((host, port), Handler).serve_forever()
