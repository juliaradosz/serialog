# SeriaLog

Aplikacja do śledzenia seriali i filmów po polsku: odcinki i postęp, premiery w Polsce, „gdzie obejrzeć w Polsce”,
repertuar kin, propozycje „Dla Ciebie”, recenzje i notatki, konta użytkowników.

- `index.html` — cała aplikacja (widoki, style, logika)
- `server.py` — serwer (konta, baza SQLite, pośrednik do TMDB, repertuar kin); działa lokalnie i jako WSGI
- `start.bat` — uruchomienie lokalne na Windows → http://localhost:8000
- `INSTRUKCJA_PYTHONANYWHERE.md` — jak postawić aplikację za darmo w internecie i dodać ją na iPhone
- `PROJEKT.md` — pełny opis projektu i dziennik prac

Klucz TMDB (`tmdb_klucz.txt`) i baza kont (`serialog.db`) **nie są** w repozytorium — patrz `tmdb_klucz.przyklad.txt`.
