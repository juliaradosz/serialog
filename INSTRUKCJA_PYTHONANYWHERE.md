# SeriaLog na telefonie — instrukcja (PythonAnywhere, za darmo)

Po wykonaniu tych kroków aplikacja będzie działać pod adresem `https://TWOJA_NAZWA.pythonanywhere.com`
— z każdego miejsca, także gdy komputer jest wyłączony — i będzie można ją dodać do ekranu głównego iPhone'a.

> **Co nie zadziała na darmowym planie:** Kino → **Repertuar** (darmowy PythonAnywhere blokuje strony kin).
> Działa wszystko inne, także Kino → „Teraz w kinach” i „Wkrótce”.

---

## Krok 1. Załóż darmowe konto

1. Wejdź na **https://www.pythonanywhere.com** i kliknij **Pricing & signup**.
2. Wybierz **Create a Beginner account** (darmowe, bez karty).
3. Wpisz nazwę użytkownika — będzie częścią adresu aplikacji (np. `julkar8` → `julkar8.pythonanywhere.com`), e-mail i hasło.
4. Potwierdź adres e-mail (link w wiadomości od PythonAnywhere).

## Krok 2. Wgraj pliki

W folderze aplikacji jest gotowa paczka **`serialog_pythonanywhere.zip`** (aplikacja, serwer, ikony, klucz TMDB i Twoje konto z danymi).

1. W PythonAnywhere otwórz zakładkę **Files**.
2. Kliknij **Upload a file** i wybierz `serialog_pythonanywhere.zip`.
3. Otwórz zakładkę **Consoles** → **Bash** i wpisz (Enter po każdej linii):
   ```bash
   unzip -o serialog_pythonanywhere.zip
   ls serialog
   ```
   Powinna pojawić się lista: `index.html  server.py  manifest.json  icon-180.png  icon-192.png  icon-512.png  tmdb_klucz.txt  serialog.db`.
4. Zamknij konsolę (wróć do Dashboard).

## Krok 3. Utwórz aplikację WWW

1. Otwórz zakładkę **Web** i kliknij **Add a new web app** → **Next**.
2. Wybierz **Manual configuration** (nie „Flask” ani „Django”!).
3. Wybierz najnowszą wersję **Python 3.x** z listy → **Next**.

## Krok 4. Podłącz serwer SeriaLog

1. Nadal w zakładce **Web**, w sekcji **Code**, kliknij link przy **WSGI configuration file**
   (wygląda jak `/var/www/TWOJA_NAZWA_pythonanywhere_com_wsgi.py`).
2. **Usuń całą zawartość** tego pliku i wklej (zamień `TWOJA_NAZWA` na swoją nazwę użytkownika):
   ```python
   import sys
   path = '/home/TWOJA_NAZWA/serialog'
   if path not in sys.path:
       sys.path.insert(0, path)
   from server import application
   ```
3. Kliknij **Save** (u góry po prawej).

## Krok 5. Włącz HTTPS i uruchom

1. Wróć do zakładki **Web**.
2. W sekcji **Security** włącz **Force HTTPS** (bezpieczne logowanie).
3. Kliknij duży zielony przycisk **Reload TWOJA_NAZWA.pythonanywhere.com**.
4. Otwórz w przeglądarce `https://TWOJA_NAZWA.pythonanywhere.com` — powinien pojawić się ekran logowania SeriaLog.
   Zaloguj się tym samym kontem co na komputerze (dane zostały przeniesione w paczce).

## Krok 6. Dodaj do ekranu głównego iPhone'a

1. Na iPhonie otwórz **Safari** i wejdź na `https://TWOJA_NAZWA.pythonanywhere.com`.
2. Zaloguj się.
3. Stuknij **Udostępnij** (kwadrat ze strzałką w górę) → **Do ekranu początkowego** → **Dodaj**.
4. Na ekranie pojawi się ikona **SeriaLog** — aplikacja otwiera się na pełnym ekranie, bez paska Safari.

---

## Ważne na przyszłość

- **Co 3 miesiące** zaloguj się do PythonAnywhere → zakładka **Web** → kliknij **Run until 3 months from today**.
  (PythonAnywhere przypomina e-mailem. Jeśli zapomnisz, strona się wyłączy, ale dane zostaną — wystarczy kliknąć i Reload.)
- **Jedna wersja danych:** po przeniesieniu korzystaj z wersji internetowej także na komputerze
  (`https://TWOJA_NAZWA.pythonanywhere.com`). Wersja z `start.bat` ma osobną bazę i nie synchronizuje się z internetową.
- **Aktualizacje aplikacji:** gdy coś zmienimy, wgraj nowy `index.html` (i ewentualnie `server.py`) przez **Files** do folderu `serialog`
  (Upload a file → nadpisz), a potem w zakładce **Web** kliknij **Reload**.
- **Nie udostępniaj** nikomu pliku `tmdb_klucz.txt` ani paczki zip (zawiera klucz i bazę kont).
- Jeśli coś nie działa: zakładka **Web** → sekcja **Log files** → **Error log** — skopiuj ostatnie linie i wklej mi je.
