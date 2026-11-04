# SeriaLog na telefonie — instrukcja (PythonAnywhere, za darmo, z GitHuba)

Po wykonaniu tych kroków aplikacja będzie działać pod adresem `https://TWOJA_NAZWA.pythonanywhere.com`
— z każdego miejsca, także gdy komputer jest wyłączony — i będzie można ją dodać do ekranu głównego iPhone'a.

Kod aplikacji jest na GitHubie: **https://github.com/juliaradosz/serialog** (publiczny, **bez** klucza TMDB i bez bazy kont).

> **Co nie zadziała na darmowym planie:** Kino → **Repertuar** (darmowy PythonAnywhere blokuje strony kin).
> Działa wszystko inne, także Kino → „Teraz w kinach” i „Wkrótce”.

---

## Krok 1. Załóż darmowe konto

1. Wejdź na **https://www.pythonanywhere.com** → **Pricing & signup** → **Create a Beginner account** (darmowe, bez karty).
2. Wpisz nazwę użytkownika (będzie częścią adresu, np. `julkar8` → `julkar8.pythonanywhere.com`), e-mail i hasło.
3. Potwierdź e-mail (link w wiadomości).

## Krok 2. Pobierz aplikację z GitHuba (konsola)

1. Otwórz zakładkę **Consoles** → kliknij **Bash**.
2. Wpisz (skopiuj i wklej), Enter:
   ```bash
   git clone https://github.com/juliaradosz/serialog.git
   ```
3. Sprawdź, czy się pobrało:
   ```bash
   ls serialog
   ```
   Powinno być m.in. `index.html  server.py  manifest.json  icon-180.png …`

## Krok 3. Wgraj klucz TMDB i swoje konto (2 pliki z komputera)

Te dwa pliki celowo **nie są** na GitHubie — wgrywasz je raz, ręcznie:

1. Otwórz zakładkę **Files** → kliknij folder **serialog**.
2. Kliknij **Upload a file** i wybierz z folderu aplikacji na komputerze:
   - **`tmdb_klucz.txt`** — klucz do bazy filmów (bez niego aplikacja nie pokaże filmów),
   - **`serialog.db`** — Twoje konto i dane (seriale, obejrzane odcinki, recenzje). Jeśli go nie wgrasz, po prostu założysz nowe konto.

## Krok 4. Utwórz aplikację WWW

1. Zakładka **Web** → **Add a new web app** → **Next**.
2. Wybierz **Manual configuration** (nie „Flask” ani „Django”!).
3. Wybierz najnowszą wersję **Python 3.x** → **Next**.

## Krok 5. Podłącz serwer SeriaLog

1. W zakładce **Web**, w sekcji **Code**, kliknij link przy **WSGI configuration file**
   (wygląda jak `/var/www/TWOJA_NAZWA_pythonanywhere_com_wsgi.py`).
2. **Usuń całą zawartość** pliku i wklej (zamień `TWOJA_NAZWA` na swoją nazwę użytkownika z PythonAnywhere):
   ```python
   import sys
   path = '/home/TWOJA_NAZWA/serialog'
   if path not in sys.path:
       sys.path.insert(0, path)
   from server import application
   ```
3. Kliknij **Save** (u góry po prawej).

## Krok 6. Włącz HTTPS i uruchom

1. Wróć do zakładki **Web**.
2. W sekcji **Security** włącz **Force HTTPS**.
3. Kliknij zielony przycisk **Reload TWOJA_NAZWA.pythonanywhere.com**.
4. Otwórz `https://TWOJA_NAZWA.pythonanywhere.com` — pojawi się ekran logowania SeriaLog.

## Krok 7. Dodaj do ekranu głównego iPhone'a

1. Na iPhonie otwórz **Safari** → `https://TWOJA_NAZWA.pythonanywhere.com` → zaloguj się.
2. Stuknij **Udostępnij** (kwadrat ze strzałką w górę) → **Do ekranu początkowego** → **Dodaj**.
3. Na ekranie pojawi się ikona **SeriaLog** — otwiera się na pełnym ekranie, bez paska Safari.

---

## Aktualizacje (gdy coś zmienimy w aplikacji)

Ja wysyłam zmiany na GitHuba, a Ty na PythonAnywhere robisz tylko:

1. **Consoles** → **Bash** (albo otwórz istniejącą konsolę) i wpisz:
   ```bash
   cd ~/serialog && git pull
   ```
2. Zakładka **Web** → zielony przycisk **Reload**.
3. Na telefonie zamknij i otwórz aplikację (albo odśwież stronę).

Twoje konto, klucz i dane zostają nietknięte — `git pull` ich nie rusza.

## Nowa ikona na iPhonie

iPhone zapamiętuje ikonę w chwili dodania do ekranu. Po zmianie ikony: przytrzymaj starą ikonę SeriaLog →
**Usuń zakładkę**, potem w Safari ponownie **Udostępnij → Do ekranu początkowego**.

## Ważne na przyszłość

- **Co 3 miesiące** zaloguj się do PythonAnywhere → **Web** → **Run until 3 months from today** (przypomną e-mailem).
  Jeśli zapomnisz, strona się wyłączy, ale dane zostaną — wystarczy kliknąć i Reload.
- **Jedna wersja danych:** po przeniesieniu korzystaj z wersji internetowej także na komputerze.
  Wersja z `start.bat` ma osobną bazę i nie synchronizuje się z internetową.
- **Nie wgrywaj** nigdzie publicznie pliku `tmdb_klucz.txt` ani `serialog.db`.
- Jeśli coś nie działa: **Web** → **Log files** → **Error log** — skopiuj ostatnie linie i wklej mi je.
