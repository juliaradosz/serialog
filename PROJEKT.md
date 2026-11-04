# SeriaLog — aplikacja do śledzenia seriali i filmów

## Opis projektu

Aplikacja webowa do śledzenia oglądanych seriali i filmów, wzorowana na funkcjach aplikacji typu TV Time.
Ma własną nazwę i wygląd — nie kopiuje logo, nazwy ani grafik TV Time.
Każdy użytkownik ma własne konto (logowanie), a jego dane są przechowywane na serwerze.

**Dolne menu (stan aktualny):** Seriale · Filmy · Kino · Dla Ciebie · Nadchodzące · Profil

**Wszystkie dane dotyczą Polski:** tytuły i opisy po polsku (także odcinków, jeśli są przetłumaczone w TMDB), „gdzie obejrzeć” tylko w polskich serwisach, polskie daty premier filmów, polskie produkcje oznaczone 🇵🇱 i wyżej w wynikach.

**Funkcje:**
- **Logowanie / zakładanie konta** — nazwa użytkownika + hasło; każdy ma osobne seriale, filmy, ulubione i historię.
- **Seriale** — trzy podzakładki:
  - *Moje seriale* — „Oglądasz” / „Chcę obejrzeć” / „Na bieżąco”, następny odcinek, pasek postępu, serwis w Polsce, „✓” = obejrzany.
  - *Szukaj* — wyszukiwarka seriali i programów (TMDB, polskie produkcje na górze) + sekcje: „Popularne w polskich serwisach”, „Polskie seriale i programy”, „Na czasie w tym tygodniu”.
  - *Gatunki* — gatunki z TMDB po polsku + „🇵🇱 Polskie”; przełącznik „Dostępne w Polsce / Wszystkie”; „Pokaż więcej”.
- **Filmy** — trzy podzakładki:
  - *Moje filmy* — „Chcę obejrzeć” / „Obejrzane”; przy filmach z przyszłą premierą — polska data premiery.
  - *Szukaj* — wyszukiwarka (ok. 1 mln filmów) + sekcje: „Teraz w kinach w Polsce”, „Wkrótce w kinach w Polsce”, „Popularne w polskich serwisach”, „Polskie filmy”.
  - *Gatunki* — 19 gatunków + „🇵🇱 Polskie”, z przełącznikiem „Dostępne w Polsce”.
- **Strona serialu** — zakładki Odcinki / O serialu / Podobne, karta „Następny do obejrzenia”, menu „⋯”, pasek postępu: w trakcie / zielony „na bieżąco” / czerwony „zakończony”.
- **„Nie obejrzę”** przy sezonach i odcinkach — pominięte nie liczą się do postępu ani „Do obejrzenia”, można je przywrócić.
- **Obsada i strony osób** — 12 osób ze zdjęciami + „Pokaż więcej” (cała obsada); kliknięcie osoby pokazuje jej biografię, seriale i filmy.
- **Przerwane oglądanie** — serial z zapisanym postępem znika z bieżących list, trafia do „Przerwane” i można go wznowić.
- **Zwiastuny** (YouTube, ładowane po kliknięciu) i **polecane/podobne tytuły** na stronach seriali i filmów.
- **Kino → Repertuar** — wybór miasta i kina (Cinema City, Multikino, Helios), dzień, godziny seansów z linkami do biletów.
- **Dla Ciebie** — propozycje na podstawie obejrzanych, ocenionych, ulubionych i odłożonych tytułów (z uzasadnieniem „bo: …”), odświeżane.
- **Kino** — „Teraz w kinach” (repertuar w Polsce) i „Wkrótce w kinach” (zapowiedzi z polskimi datami premier, wg miesięcy).
- **Obejrzane wszystko** i **pytanie o poprzednie** odcinki przy zaznaczaniu odcinka/sezonu.
- **Nadchodzące → Do obejrzenia** (grupy zwinięte, rozwijane kliknięciem) — wszystkie wyemitowane, nieobejrzane odcinki po kolei (grupami wg serialu, „Pokaż wszystkie”) i filmy z listy, które już miały premierę; licznik zaległości.
- **Nadchodzące → Nadchodzące** — wszystkie nadchodzące odcinki dodanych seriali i polskie premiery filmów z listy, po kolei wg daty („Dziś”, „Jutro”, kolejne dni), przy odcinku serwis dostępny w Polsce (np. Player). Kropka z liczbą przy ikonie = odcinki z dzisiejszą premierą.
- **Karta serialu** — polski tytuł (i oryginalny), opis po polsku, status, liczba sezonów, ocena, obsada, sezony i odcinki (odhaczanie pojedynczo, sezonem, „Oznacz wszystkie”), **Gdzie obejrzeć w Polsce**.
- **Karta odcinka** — polski tytuł i opis (gdy brak polskiego — angielski z oznaczeniem), data, czas, reakcje.
- **Karta filmu** — polski tytuł, opis, reżyser, obsada, ocena; „Chcę obejrzeć później” / „Już obejrzany” / ❤; po obejrzeniu: data, ocena 1–5 ★, reakcja; **Gdzie obejrzeć w Polsce** z polskimi premierami (kino / VOD / TV).
- **Gdzie obejrzeć w Polsce** — serwisy w abonamencie, za darmo, do wypożyczenia i kupienia (z logotypami; kliknięcie otwiera polską stronę serwisu), emisja w polskiej telewizji (dla polskich produkcji), następny odcinek, link „Wszystkie opcje w Polsce” i Filmweb.
- **Profil** — nagłówek konta, 6 statystyk, czas przed ekranem, półki z okładkami (Oglądam, Seriale na później, Seriale obejrzane, Filmy obejrzane, Filmy na później, Ulubione), Moje recenzje, Notatki do odcinków, gatunki, historia, ustawienia (motyw, eksport/import/reset).
- **Recenzje** (prywatne) — ocena 1–5 ★ i tekst dla obejrzanych seriali i filmów, z możliwością edycji i usunięcia.
- **Notatki do odcinków** (prywatne) — w karcie odcinka; ikona 📝 na liście odcinków.
- **Sprawdzanie z Wikipedią** — na stronie serialu liczba sezonów i odcinków z polskiej Wikipedii obok danych aplikacji, z ostrzeżeniem przy niezgodności.
- **Dodatki do programów** (Extra, Reunion…) — oznaczone w wynikach; na ich stronie ostrzeżenie i przycisk zamiany na główny program.
- **Miniaturki odcinków** — kadry z odcinków na listach (z zastępczym kadrem programu, gdy brak).
- **Znane daty premier** — plakietki w nagłówku serialu/filmu, w „Moich serialach”, „Do obejrzenia” i na kafelkach (📅 data).

**Wygląd:** 10 motywów do wyboru w Profilu → Ustawienia (Krem, Szałwia, Ocean, Lawenda, Pudrowy róż, Piasek, Mięta, Wieczór, Noc, Grafit), czcionki Fraunces + Nunito; motyw zapisany na koncie.

**Technologia:**
- Front: czysty HTML + CSS + JavaScript w jednym pliku `index.html`.
- Serwer: `server.py` — Python, tylko biblioteka standardowa; baza SQLite `serialog.db`.
  - Hasła: PBKDF2-SHA256 (200 000 iteracji, losowa sól); sesja w ciasteczku `sid` (HttpOnly, SameSite=Lax, 30 dni).
  - Ochrona: limit 10 nieudanych logowań / 5 min z jednego IP; serwer udostępnia tylko `index.html` (baza, kod serwera i plik z kluczem są niedostępne z przeglądarki).
  - API: `POST /api/register`, `POST /api/login`, `POST /api/logout`, `GET /api/me`, `GET /api/config`, `GET/PUT /api/state`, `GET /api/tmdb/...` (pośrednik do TMDB — tylko dla zalogowanych, tylko dozwolone ścieżki, pamięć podręczna 30 min, domyślnie `language=pl-PL`).
- Dane: **TMDB** (themoviedb.org) — klucz API w `tmdb_klucz.txt`, używany wyłącznie przez serwer. Dostępność w serwisach: JustWatch (przez TMDB, region `PL`). Obrazy: `image.tmdb.org`.
- Aplikacja wymaga serwera (bez niego pokazuje instrukcję uruchomienia `start.bat`).

**Uruchomienie:** dwuklik `start.bat` albo w terminalu `python server.py`, potem http://localhost:8000.
Po zmianie `server.py` trzeba zamknąć stare okno serwera i uruchomić `start.bat` ponownie.
Dostęp z innych urządzeń w domu (np. telefon): `set HOST=0.0.0.0` przed `python server.py`, potem adres IP komputera, np. `http://192.168.1.10:8000`.
Dostęp przez internet wymaga wgrania na serwer/hosting — patrz „Pomysły na dalej”.

## Struktura plików

| Plik | Zawartość |
|---|---|
| `index.html` | Cała aplikacja (style, widoki, logika) |
| `server.py` | Serwer: konta, logowanie, zapis danych, pośrednik do TMDB |
| `start.bat` | Uruchamia serwer i otwiera przeglądarkę (Windows) |
| `tmdb_klucz.txt` | Klucz API TMDB (nie udostępniać!) |
| `serialog.db` | Baza kont i danych użytkowników |
| `manifest.json`, `icon-*.png` | Ikona i ustawienia do instalacji na ekranie głównym telefonu |
| `INSTRUKCJA_PYTHONANYWHERE.md` | Jak postawić aplikację za darmo w internecie i dodać ją na iPhone |
| `serialog_pythonanywhere.zip` | Paczka plików do wgrania na PythonAnywhere (zawiera klucz i bazę — nie udostępniać!) |
| `PROJEKT.md` | Ten plik — opis projektu i dziennik prac |

---

## Dziennik prac

### 2026-11-03 — Polecenie 1
> „przy każdym moim poleceniu i wszystko co robisz po kolei zapisuj w pliku md, tak żeby cała informacja o projekcie się tam zawierała”

1. Utworzono plik `PROJEKT.md` (opis projektu + dziennik).
2. Zapisano tę zasadę w pamięci Claude, żeby obowiązywała także w kolejnych sesjach.

### 2026-11-03 — Polecenie 2
> „czy jesteś w stanie spojrzeć jak wyglądała aplikacja TV Time i odtworzyć ją?”

Decyzje:
- Odtworzono **funkcje i układ** aplikacji typu TV Time (lista do obejrzenia, nadchodzące, odkrywanie, profil ze statystykami czasu oglądania, reakcje na odcinki), ale z **własną nazwą (SeriaLog) i własnym wyglądem** — bez kopiowania znaku towarowego, logo i grafik oryginału.
- Zamiast własnej bazy danych użyto darmowego API TVMaze (prawdziwe seriale, sezony, odcinki, daty emisji).
- Brak serwera/kont — dane trzymane lokalnie w przeglądarce.
- Interfejs po polsku, ciemny motyw, układ „mobilny” (dolna nawigacja), działa też na komputerze.

Kroki:
1. Napisano `index.html` z widokami: Do obejrzenia, Nadchodzące, Odkrywaj, Karta serialu, Karta odcinka, Profil.
2. Dodano `.claude/launch.json` — lokalny serwer podglądu (`python -m http.server 8765`, adres `http://localhost:8765`).
3. Test w przeglądarce:
   - Odkrywaj: ładują się popularne seriale z plakatami ✔
   - Dodanie do obserwowanych (Breaking Bad, Person of Interest) ✔
   - „✓” na liście przesuwa do następnego odcinka, serial przechodzi do sekcji „Oglądasz” ✔
   - Karta serialu: oznaczenie całego sezonu, karta odcinka, reakcja emoji ✔
   - Profil: czas oglądania, liczniki, gatunki, historia ✔
   - Brak błędów w konsoli.
4. Poprawka: kafelki w siatce „Odkrywaj” miały różne szerokości → `grid-template-columns: repeat(3, minmax(0,1fr))`.
5. Wyczyszczono dane testowe z przeglądarki.

Znane drobiazgi / pomysły na dalej:
- Brak filmów (TVMaze ma tylko seriale) — można dodać przez TMDB (wymaga darmowego klucza API).
- Historia „Ostatnio obejrzane” przy oznaczeniu całego sezonu naraz ma tę samą godzinę dla wszystkich odcinków.
- Możliwe rozszerzenia: konto i synchronizacja między urządzeniami, komentarze, powiadomienia o premierach, wersja PWA na telefon.

### 2026-11-03 — Polecenie 3
> „zrób tak, żeby były dostępne tam wszystkie możliwe istniejące filmy, żeby można było wybrać co się oglądało itp.”

Decyzje:
- Źródło filmów: **Wikidata + Wikipedia** — największa otwarta baza filmów (ok. 300 tys.), darmowa, bez klucza API, z polskimi tytułami. Rozważany był TMDB (lepsze plakaty), ale wymaga rejestracji i klucza — można go dodać później.
- Wyszukiwanie obejmuje typy: film, film fabularny, animowany, animowany pełnometrażowy, dokumentalny, telewizyjny, niemy.
- „Popularne filmy” = 45 filmów z największą liczbą artykułów w Wikipediach (lista ID wpisana w kod, bo liczenie tego na żywo trwa ok. 11 s).
- Film ma 3 stany: brak → „do obejrzenia” → „obejrzany” (z datą, oceną 1–5 i reakcją).

Kroki:
1. Sprawdzono źródła (curl): wyszukiwanie w Wikidata ✔, plakaty z Wikipedii (`pilicense=any`, także plakaty niewolne) ✔, nagłówki CORS ✔.
2. Dodano do `index.html`:
   - zakładkę **Filmy** w dolnym menu (Do obejrzenia / Obejrzane),
   - przełącznik **Seriale / Filmy** w Odkrywaj,
   - **kartę filmu** (`#/movie/Q…`) z datą obejrzenia, oceną, reakcjami, obsadą, opisem i linkami,
   - filmy w **Profilu** (czas, licznik, gatunki, historia),
   - dane filmów w `localStorage` (`state.movies`), objęte eksportem/importem/resetem.
3. Optymalizacja: jedno duże zapytanie SPARQL trwało ~7,5 s → rozbite na 3 równoległe (dane / gatunki / reżyserzy) → ~1,7 s.
4. Test w przeglądarce: popularne filmy z plakatami ✔, wyszukiwanie „Kiler” (polskie filmy Machulskiego) ✔, dodanie do listy ✔, oznaczenie jako obejrzany + ocena 4★ + reakcja ✔, Profil liczy czas filmów ✔, brak błędów w konsoli ✔.
5. Poprawki: czas w Profilu pokazywany jako „X h Y min”; polska odmiana w liczniku u góry („1 film”, „2 filmy”, „5 filmów”); przycisk „Obejrzałem” zmieniony na neutralne „Obejrzany”.
6. Serwer podglądu: `.claude/launch.json` w `C:\tmp` (serwuje folder aplikacji na `http://localhost:8765`). Dane testowe wyczyszczone.

Ograniczenia:
- Nie każdy film w Wikidata ma plakat lub polski opis (mało znane filmy pokazują inicjały zamiast plakatu).
- Pierwsze wejście w Odkrywaj → Filmy ładuje się ok. 2 s (zapytania do Wikidata).

### 2026-11-03 — Polecenie 4 (przeniesienie projektu)
> „Tak, przenieś”

- Otwarto okno wyboru folderu — wybór został anulowany. Pliki zostają w folderze sesji; przeniesienie można powtórzyć później.

### 2026-11-03 — Polecenie 5
> 1. podział na seriale i filmy — zakładka Filmy do przeszukiwania filmów, tak samo z serialami; opisy po polsku po kliknięciu w okładkę
> 2. na dole „Nadchodzące” — po kolei, który odcinek kiedy wyjdzie (np. 5 seriali z codziennymi odcinkami)
> 3. w serialu odznaczanie obejrzanych odcinków, w filmie: obejrzany / chcę obejrzeć później
> 4. informacje gdzie obejrzeć, gdzie się niedługo pojawi
> 5. wybieranie po tematyce (np. fantasy)
> 6. logowanie — każdy użytkownik ma swoje konto, ulubione itp.

Decyzje:
- **Menu** przebudowane na: Seriale · Filmy · Nadchodzące · Profil (zakładka „Odkrywaj” zniknęła — wyszukiwanie i gatunki są teraz w Serialach i Filmach osobno). Stare adresy `#/discover…` przekierowują.
- **Polskie opisy**: z polskiej Wikipedii (seriale łączone z Wikidata przez IMDb). Opisy odcinków zostają po angielsku — nie ma darmowego źródła polskich opisów odcinków.
- **Gdzie obejrzeć**: darmowe dane z Wikidata (identyfikatory Netflix/Disney+/Max/Prime Video/Apple TV, polska data premiery) + stacja z TVMaze + link do JustWatch. Pełne, aktualne dane „dostępne w Polsce na …” ma tylko TMDB/JustWatch API (wymaga klucza) — zostawione jako możliwe rozszerzenie.
- **Gatunki**: wyszukiwarka Wikidata z filtrem gatunku, posortowana wg popularności (`srsort=incoming_links_desc`) — szybko (~0,3 s) i dla dowolnej liczby tytułów. Identyfikatory gatunków serialowych dobrane zapytaniem o najczęstsze gatunki seriali w Wikidata. Seriale z gatunków są łączone z TVMaze przez IMDb (`/lookup/shows?imdb=`), żeby mieć odcinki.
- **Konta**: własny serwer w Pythonie (bez dodatkowych instalacji) z bazą SQLite. Rozważane: profile tylko w przeglądarce (nie są prawdziwymi kontami), Firebase/Supabase (wymagają założenia usługi i kluczy). Wybrano własny serwer — prawdziwe konta, dane na serwerze, łatwe przeniesienie na hosting.
- Przy pierwszym logowaniu aplikacja proponuje przeniesienie danych z trybu lokalnego na konto.
- Dodano **Ulubione (❤)** dla seriali i filmów.

Kroki:
1. Sprawdzono źródła (curl): właściwości Wikidata dla serwisów (P1874 Netflix, P7595/P7596 Disney+, P8298 Max, P8055 Prime Video, P9586/P9751 Apple TV) i ich adresy URL; identyfikatory gatunków; TVMaze lookup po IMDb (CORS ✔); adres wyszukiwarki JustWatch (`/pl/search?q=`).
2. Napisano `server.py` (konta, sesje, zapis danych) i `start.bat`.
3. Przepisano `index.html`: nowe menu, podzakładki, gatunki, „Gdzie obejrzeć”, polskie opisy, Nadchodzące (od początku dnia, z godzinami, filmy z listy), ulubione, ekran logowania, synchronizacja z serwerem.
4. Optymalizacje po testach:
   - strona serialu ładowała się ~6 s → odcinki pokazują się od razu, polski opis i serwisy doładowują się w tle;
   - to samo na stronie filmu;
   - zapytanie o reżyserów bywało bardzo wolne (8,5 s) → doładowuje się w tle i nie blokuje list.
5. Testy w przeglądarce (serwer na porcie 8001):
   - rejestracja, logowanie, złe hasło (odrzucone), wylogowanie ✔; drugi użytkownik nie widzi danych pierwszego ✔; dane zostają po przeładowaniu ✔;
   - `/server.py` i `/serialog.db` niedostępne z przeglądarki (404) ✔;
   - Seriale → Gatunki → Fantasy: Gra o tron, Buffy, Supernatural… ✔; dodanie „Gry o tron” z gatunku ✔;
   - karta „Gra o tron”: polski opis z Wikipedii, emisja HBO, linki Max i Apple TV ✔;
   - Nadchodzące z 5 codziennymi programami: 66 odcinków po kolei z godzinami, „Dziś: 5”, kropka przy ikonie ✔;
   - Filmy → Gatunki → Fantasy (4701 filmów) i Horror, „Pokaż więcej” ✔; karta „Harry Potter i Kamień Filozoficzny”: polski opis, Netflix/Max/Apple TV, obsada ✔.
6. Usunięto testową bazę `serialog.db` (testowe konta) — przy pierwszym uruchomieniu powstanie nowa, pusta.

Ograniczenia:
- Linki do serwisów pochodzą z Wikidata i nie zawsze odpowiadają ofercie w Polsce (stąd dodatkowy link do JustWatch).
- Przypisanie gatunków w Wikidata bywa nieprecyzyjne (np. „Gwiezdne wojny” w fantasy, „Grawitacja” w horrorze).
- Pierwsze wejście w gatunek trwa kilka sekund (zapytania do Wikidata); kolejne strony ~2 s.
- Konta działają na komputerze, na którym uruchomiony jest `server.py` (i w sieci domowej z `HOST=0.0.0.0`). Aby korzystać przez internet, trzeba wgrać aplikację na hosting.

Pomysły na dalej:
- Hosting w internecie (VPS/Render/Railway) + HTTPS, żeby konta działały z każdego miejsca.
- Klucz TMDB → dokładne „gdzie obejrzeć w Polsce” (dane JustWatch), lepsze plakaty, polskie opisy odcinków.
- Reset hasła przez e-mail, znajomi i wspólne listy, powiadomienia o nowych odcinkach.

### 2026-11-03 — Polecenie 6
> „Tak, wybierz folder”

- Wybrano folder `C:\Users\Julka\Downloads\aplikacja z filmami` — projekt (index.html, server.py, start.bat, PROJEKT.md) został tam przeniesiony i od teraz tam jest jego stałe miejsce.

### 2026-11-03 — Polecenie 7
> „zrób tak, aby wszystkie premiery i dane dotyczące filmu lub serialu dotyczyły Polski, a nie Stanów. Nie chcę informacji, gdzie obejrzeć w innym kraju, tylko w Polsce. Tytuły i opisy też po polsku. Nie ma niektórych seriali, takich jak Hotel Paradise (Polska). Rozszerz bazę.”

Analiza (sprawdzone curl):
- **TVMaze** (obecne źródło seriali) ma „Hotel Paradise” (TVN, id 81076), ale tylko do 16.04.2025 — brak nowszych edycji; w wyszukiwarce jest dopiero na 7. miejscu (przed nim zagraniczne „Paradise Hotel”). TVMaze nie ma polskich tytułów ani opisów, a daty emisji to daty z kraju produkcji (USA itp.). Plan emisji dla Polski w TVMaze jest pusty.
- **Wikidata** daje polskie tytuły/opisy tylko dla części tytułów, a linki do serwisów nie mówią, czy coś jest dostępne w Polsce.
- **TMDB (The Movie Database)** ma wszystko, czego potrzeba: ~1 mln filmów i ~200 tys. seriali (także polskie programy), tytuły i opisy po polsku (także opisy odcinków), **„gdzie obejrzeć” konkretnie w Polsce** (dane JustWatch: abonament / wypożyczenie / kupno), polskie daty premier filmów, odkrywanie po gatunkach z filtrem „dostępne w Polsce”.
- TMDB wymaga **darmowego klucza API** (rejestracja na themoviedb.org) — bez niego API odpowiada 401. Konto musi założyć użytkownik.

Decyzja:
- Przejść na TMDB jako główne źródło seriali i filmów (z polskim językiem `pl-PL` i regionem `PL`); klucz trzymany na serwerze (`server.py` pośredniczy w zapytaniach), żeby nie był widoczny w przeglądarce.
- Utworzono plik `tmdb_klucz.txt` — tu użytkownik wkleja swój klucz.
- Czekam na klucz, żeby zbudować i od razu przetestować nową wersję. Istniejące dane kont (`serialog.db`) zostaną zachowane i przeniesione na nowe identyfikatory.
- Uwaga: daty emisji odcinków zagranicznych seriali to daty światowe/kraju produkcji — osobnych polskich dat emisji odcinków nie publikuje żadne darmowe źródło. W Nadchodzących będą oznaczone serwisem dostępnym w Polsce.

### 2026-11-03 — Polecenie 8
> „Zrób bez klucza” → zaraz potem: „(klucz TMDB) masz klucz i dokończ”

1. Zaczęto wersję bez klucza (sprawdzono: Hotel Paradise w Wikidata jako Q97372453 „program telewizyjny”, Filmweb ID w Wikidata = P5032, adresy wyszukiwarek polskich serwisów), ale użytkownik przerwał i podał klucz TMDB — przejście na TMDB.
2. Klucz zapisano w `tmdb_klucz.txt` (tylko na dysku; serwer go czyta, przeglądarka nigdy go nie dostaje).
3. Sprawdzono TMDB: „Hotel Paradise” (id 211656, TVN 7) — 13 edycji, odcinki do bieżącego tygodnia, w Polsce: Player i HBO Max; „Gra o tron” — polskie tytuły i opisy odcinków („Nadchodzi zima”); „Matrix” — polska premiera kinowa 13.08.1999; gatunki po polsku.
4. `server.py`: dodano pośrednika `/api/tmdb/...` (wymaga zalogowania, lista dozwolonych ścieżek, pamięć podręczna 30 min, domyślnie polski język) i `/api/config`.
5. `index.html` przepisany na TMDB:
   - polskie tytuły/opisy wszędzie, angielski opis tylko jako zapas z oznaczeniem „brak polskiego opisu”;
   - „Gdzie obejrzeć w Polsce” (abonament / za darmo / wypożyczenie / kupno, logotypy, linki do polskich stron serwisów, Filmweb);
   - polskie premiery filmów (kino / VOD / TV) — także w Nadchodzących i na liście „Chcę obejrzeć”;
   - sekcje „Teraz w kinach w Polsce”, „Wkrótce w kinach w Polsce”, „Popularne w polskich serwisach”, „Polskie seriale i programy”, „Polskie filmy”;
   - gatunki z przełącznikiem „Dostępne w Polsce”;
   - polskie produkcje oznaczone 🇵🇱 i na górze wyników wyszukiwania.
6. **Przeniesienie danych** ze starej wersji: seriale TVMaze → TMDB (przez IMDb/TVDB, a w ostateczności po tytule), obejrzane odcinki i reakcje → nowe klucze `serial:sezon:odcinek`, filmy z Wikidata → TMDB (właściwość P4947 lub wyszukiwanie), ulubione. Dzieje się automatycznie przy pierwszym logowaniu.
7. Testy (serwer testowy na porcie 8002, osobne konto testowe z kopią danych konta „julkar8”):
   - przeniesienie: 7/7 seriali (np. „Dom z papieru”, „Rekrut”, „Love Never Lies: Polska”), obejrzany odcinek, reakcja, film „Matrix” z oceną 5★ i ulubione ✔;
   - „hotel paradise” w wyszukiwarce → 🇵🇱 Hotel Paradise na 1. miejscu ✔; karta: polski opis, 622 odcinki, Player + HBO Max, emisja TVN/TVN 7, następny odcinek „jutro” ✔;
   - Nadchodzące: kolejne odcinki Hotel Paradise z serwisem Player, premiera filmu w Polsce (20.11.2026) ✔;
   - Filmy: „Teraz w kinach w Polsce”, karta filmu z polską premierą kinową, Fantasy z filtrem PL (1594 filmy) ✔;
   - pośrednik TMDB: bez logowania 401, niedozwolona ścieżka 404, `tmdb_klucz.txt` niedostępny z przeglądarki ✔;
   - poprawka po teście: okładki w „Ulubionych” po przeniesieniu danych.
8. Usunięto konto testowe z `serialog.db` (zostało tylko konto „julkar8” — jego dane przeniosą się przy najbliższym logowaniu).

Ograniczenia:
- TMDB nie podaje godzin emisji odcinków ani osobnych polskich dat emisji odcinków zagranicznych seriali — w Nadchodzących są daty premier (w polskich serwisach zwykle ten sam dzień).
- Nie każdy tytuł/odcinek ma polskie tłumaczenie w TMDB (wtedy np. „Odcinek 5” albo opis po angielsku z oznaczeniem).
- Dane o dostępności pochodzą z JustWatch i mogą się różnić od bieżącej oferty o kilka dni.
- Działający wcześniej serwer (stara wersja) trzeba zamknąć i uruchomić ponownie `start.bat`.

### 2026-11-03 — Polecenie 9
> „zrób jeszcze tam, gdzie są odcinki, które wyjdą, zakładkę do obejrzenia też — niech będą tam odcinki lub filmy, które nie zostały jeszcze obejrzane; jeśli np. nie obejrzałam jeszcze 10 odcinków, niech będą wymienione po kolei. Zrób też ładniejszy wygląd aplikacji, a nie taki czarny i surowy”

Decyzje:
- W zakładce **Nadchodzące** są teraz dwie podzakładki: **Nadchodzące** (kalendarz premier) i **Do obejrzenia** (z licznikiem zaległości).
- „Do obejrzenia”: wszystkie **wyemitowane, nieobejrzane odcinki** każdego serialu po kolei (sezon → odcinek), pogrupowane wg serialu (najpierw ostatnio oglądane), z serwisem w Polsce; przy dużych zaległościach widać pierwsze 10 i przycisk „Pokaż wszystkie (N)”. Pod spodem **filmy** z listy „Chcę obejrzeć”, które już miały premierę. „✓” od razu oznacza obejrzane i usuwa z listy.
- Nowy wygląd: **jasny motyw** (domyślny) — jasnofioletowe tło z delikatnymi kolorowymi poświatami, białe karty z cieniem, fioletowo-różowe gradienty na przyciskach i aktywnych zakładkach, czcionka Plus Jakarta Sans, pływające zaokrąglone menu dolne, nagłówek serialu/filmu jako zaokrąglona karta ze zdjęciem w tle, kolorowe kafelki gatunków, daty w kalendarzu jako kolorowe etykiety.
- Dodatkowo motyw **„Wieczorny”** (granatowo-fioletowy, nie czarny) — przełącznik w Profilu → Wygląd; wybór zapamiętywany w przeglądarce.
- Flaga 🇵🇱 (Windows wyświetlał ją jako „PL”) zastąpiona małą narysowaną biało-czerwoną flagą.

Kroki:
1. `index.html`: dodano widok `#/towatch` (`renderToWatch`, `todoData`, podzakładki `upTabs`), akcje `expand` i `theme`, funkcję `setTheme`.
2. Wymieniono cały arkusz stylów (zmienne kolorów dla dwóch motywów, nowe komponenty: `.group`, `.cnt`, `.plb`).
3. Poprawki znalezione w testach: kropka „0” przy „Nadchodzące” była widoczna mimo braku dzisiejszych odcinków (`[hidden]` nadpisywane przez CSS); zbyt jaskrawe kolory gatunków → spokojniejsza paleta odcieni.
4. Test (serwer testowy, konto testowe z Grą o tron, Domem z papieru, Hotel Paradise i 2 filmami): lista „Do obejrzenia” — 688 odcinków + 2 filmy, odcinki po kolei od pierwszego nieobejrzanego (S02E03…), „✓” usuwa odcinek i zmniejsza licznik, „Pokaż wszystkie” rozwija listę; zrzuty ekranu obu motywów ✔. Konto testowe usunięte.

Ograniczenia:
- Motyw jest zapamiętywany osobno w każdej przeglądarce (nie na koncie).
- Aby zobaczyć zmiany, trzeba odświeżyć stronę (serwera nie trzeba restartować — zmienił się tylko `index.html`).

### 2026-11-03 — Polecenie 10
> 1. jak jest już znana data nadchodzących premier albo odcinków, niech będzie to gdzieś pokazane
> 2. w aplikacji Hotel Paradise ma tylko 12 sezonów, a teraz trwa emisja 13 — popraw, bo są niespójne dane
> 3. popraw zakładkę Profil: statystyki, ale też ładniejszy wygląd, wgląd do obejrzanych lub odłożonych na później seriali i filmów, ulubione; recenzje użytkownika (ocena obejrzanych, z możliwością zmiany)
> 4. ładna opcja dodania komentarza do odcinka, widocznego tylko dla użytkownika

Ustalenia i decyzje:
1. **Daty premier** są teraz widoczne w wielu miejscach:
   - nagłówek serialu: plakietka „📅 Nowy odcinek S13E41 — jutro” (albo „Premiera sezonu N — data”, gdy zapowiedziany jest nowy sezon bez listy odcinków);
   - nagłówek filmu: „🎟️ Premiera w kinach w Polsce — data” (oraz VOD / TV), gdy premiera jest w przyszłości;
   - „Moje seriale” i „Do obejrzenia”: przy każdym serialu najbliższa znana data;
   - kafelki w wyszukiwarce i listach: zamiast roku data premiery („📅 20 lis 2026”) dla tytułów, które jeszcze nie wyszły.
2. **Hotel Paradise**: sprawdzono TMDB — ma 13 sezonów (13. od 29.08.2026, 48 odcinków, ostatni zapowiedziany na 17.11.2026), a zapytanie aplikacji pobiera wszystkie 13. Dla pewności liczba sezonów jest teraz liczona z faktycznie pobranych odcinków, a przy trwającym sezonie wyświetla się „trwa emisja sezonu 13”. Prawdopodobna przyczyna „12 sezonów”: otwarta była jeszcze stara wersja strony/serwera — po ponownym uruchomieniu `start.bat` i odświeżeniu strony (Ctrl+F5) dane są spójne.
3. **Profil** przebudowany:
   - kolorowy nagłówek z awatarem, nazwą, łącznym czasem i „Wyloguj”;
   - 6 kafelków statystyk (seriale, odcinki, filmy, ulubione, recenzje, notatki) + czas przed ekranem;
   - przewijane w poziomie „półki” z okładkami: **Oglądam**, **Seriale na później**, **Seriale obejrzane**, **Filmy obejrzane**, **Filmy na później**, **Ulubione** (z postępem i gwiazdkami oceny);
   - **Moje recenzje** (karty z oceną, tekstem i datą — kliknięcie prowadzi do edycji), **Notatki do odcinków**, ulubione gatunki, ostatnio obejrzane, ustawienia (motyw, dane).
   - **Recenzje**: na stronie serialu (gdy obejrzano co najmniej 1 odcinek) i filmu (po oznaczeniu jako obejrzany) — panel „✍️ Oceń i napisz recenzję”: gwiazdki 1–5 z opisem słownym (Słaby … Arcydzieło), tekst do 3000 znaków, Zapisz / Anuluj / Usuń; zapisana recenzja ma przycisk „Edytuj”. Dawna ocena filmu (gwiazdki) została włączona do recenzji.
4. **Notatki do odcinków**: w karcie odcinka „📝 Dodaj notatkę do odcinka” → pole tekstowe, Zapisz / Anuluj / Usuń, później „Edytuj”; przy odcinku na liście widać ikonę 📝. Notatki i recenzje są zapisywane tylko na koncie użytkownika (prywatne — nikt inny ich nie widzi).

Kroki:
1. `index.html`: `showNextDate`, plakietki `.hbadge`, daty w kartach i kafelkach; `nSeasons` i „trwa emisja sezonu”; `reviewPanel`, `notePanel`, akcje `revEdit/revRate/revSave/revDel/noteEdit/noteSave/noteDel/cancelEdit`; nowe `state.notes`; nowy `renderProfile` (asynchroniczny — ładuje postęp seriali); nowe style.
2. Test (serwer testowy 8002, konto testowe): Hotel Paradise — „trwa emisja sezonu 13 · 13 sezonów”, „Nowy odcinek S13E41 — jutro” ✔; recenzja Gry o tron: dodanie 4★ + tekst, edycja na 5★ + nowy tekst (tekst nie znika przy zmianie gwiazdek) ✔; notatka do S01E01 + ikona 📝 ✔; Profil: półki (Oglądam 1, Na później 2, Obejrzane 1, Filmy obejrzane 2, Na później 1), recenzje, notatki ✔; „Wkrótce w kinach”: daty 📅 na kafelkach, plakietka premiery w Polsce na stronie filmu ✔; brak poziomego przewijania strony ✔. Konto testowe usunięte.

### 2026-11-03 — Polecenie 11
> (zrzut ekranu: sezony 8–12, sezon 12 — 0/2) „hotel paradise dalej ma 12 sezonów, więc coś źle jest; nie bierz tylko informacji z tej strony, ale też ogólnie z internetu, żeby nie było takich błędów”
> → dopisane w trakcie: „najlepiej by było, jakby aplikacja ściągała też miniaturki odcinków”

Diagnoza:
- Na koncie użytkownika był zapisany **„Hotel Paradise Extra”** (TMDB 233680) — osobny wpis z rozszerzonymi wydaniami (sezony z 1–3 odcinkami, 12 sezonów, sezon 12 = 2 odcinki), a nie główny **„Hotel Paradise”** (TMDB 211656: 13 sezonów, sezon 12 = 50 odcinków, sezon 13 = 48). Oba wyglądają w wyszukiwarce prawie tak samo.
- Porównanie z polską Wikipedią (artykuł „Hotel Paradise”): „13 edycji + All Stars”, 608 odcinków (stan na 3 września 2026), TVN 7 — zgodne z głównym wpisem TMDB.

Zmiany:
1. **Ostrzeżenie o dodatkach**: wpisy typu „Extra”, „Reunion”, „Aftershow”, „Kulisy” itp. są rozpoznawane; na ich stronie pojawia się żółta ramka „To jest dodatek do programu — główny program to …” z przyciskami **„Przejdź do …”** i **„Zamień w moich serialach”** (przenosi też ulubione). W wynikach wyszukiwania takie wpisy mają etykietę „dodatek do programu”.
2. **Sprawdzanie z internetem (polska Wikipedia)**: na stronie serialu panel „📖 Sprawdzone z Wikipedią” — liczba sezonów/edycji i odcinków z infoboksu artykułu (ze „stanem na” dzień), obok liczby w aplikacji; zielone „✓ zgodne” albo ostrzeżenie „⚠️ w bazie brakuje części sezonów — lista może być niepełna”. Artykuł jest szukany przez Wikidata (identyfikator TMDB/IMDb), a gdy go tam nie ma — w wyszukiwarce Wikipedii z kontrolą zgodności roku premiery (żeby nie pomylić z innym artykułem). Obsługiwane pola: „liczba sezonów”, „liczba serii”, „liczba edycji”, „liczba odcinków”.
3. **Miniaturki odcinków**: przy każdym odcinku na liście sezonów i w „Do obejrzenia” kadr z odcinka (TMDB); gdy odcinek nie ma kadru (np. większość odcinków Hotel Paradise), pokazuje się kadr programu z kolorową nakładką i numerem odcinka. Obrazy ładują się dopiero po rozwinięciu sezonu.
4. Naprawiono brak funkcji `getJSON` (usunięta przy przejściu na TMDB, a używana przez nowe sprawdzanie Wikipedii).

Testy (serwer testowy 8002, konto testowe): wyszukiwanie „hotel paradise” → główny program pierwszy, „Extra” z etykietą „dodatek do programu” ✔; dodanie „Extra” → ramka ostrzeżenia → „Zamień w moich serialach” → na liście tylko „Hotel Paradise” ✔; Hotel Paradise: Wikipedia „13 edycji + All Stars” vs aplikacja 13 → „✓ zgodne”, ostatnie sezony 12 (50 odc.) i 13 (48 odc.) ✔; Gra o tron: Wikipedia 8 sezonów / 73 odcinki = aplikacja ✔; miniaturki odcinków Gry o tron widoczne, Hotel Paradise: 5 prawdziwych kadrów + zastępcze ✔. Konto testowe usunięte.

Do zrobienia przez użytkownika: na koncie „julkar8” jest nadal „Hotel Paradise Extra” — po odświeżeniu strony (Ctrl+F5) wejść w niego i kliknąć „Zamień w moich serialach”.

### 2026-11-03 — Polecenie 12
> „Zamienię sam”

- Użytkownik sam zamieni na koncie „Hotel Paradise Extra” na główny „Hotel Paradise” (Ctrl+F5 → strona „Extra” → „Zamień w moich serialach”). Bez zmian w kodzie.

### 2026-11-03 — Polecenie 13
> 1. popraw wygląd aplikacji, niech nie wygląda jakby była zrobiona przez AI, tylko comfy ładna aplikacja
> 2. jak się klika odcinek, niech będzie jego opis, a nie tylko dodanie notatki
> 3. w profilu niech będzie wszystko mniejsze i czytelniejsze, bo statystyki zajmują cały ekran
> 4. opcja „obejrzałam wszystko” — wtedy automatycznie wszystko się zaznacza
> 5. gdy zaznaczy się np. 6. sezon, aplikacja pyta, czy zaznaczyć wszystkie poprzednie też jako obejrzane; tak samo z odcinkami
> 6. w „Do obejrzenia” seriale i filmy zwinięte — rozwijają się dopiero po kliknięciu
> 7. w szukaniu filmów mają być wszystkie filmy, a nie kina (co będzie i co było niedawno)
> 8. osobna zakładka z tym, co wchodzi do kin albo jest aktualnie w kinach

Zmiany:
1. **Nowy wygląd „przytulny”**: ciepłe kremowe tło, karty w kolorze papieru, akcent terakota, zieleń szałwii dla „obejrzane”, złote gwiazdki; nagłówki szeryfową czcionką Fraunces, tekst — Nunito; bez neonowych gradientów, poświat i emoji w nagłówkach; dolne menu jako zwykły pasek z kreską nad aktywną zakładką; zakładki jako segmentowany przełącznik; gatunki w pastelowych, przygaszonych kolorach. Motyw „Wieczorny” — ciepły, przygaszony brąz zamiast granatu.
2. **Karta odcinka**: duży kadr z tytułem, data/czas/ocena, **opis odcinka na pierwszym planie**; gdy baza nie ma opisu (np. większość odcinków Hotel Paradise — tylko 4 z 48 w sezonie 13 mają opis, po angielsku brak) — informacja „Opis tego odcinka nie został jeszcze dodany do bazy” + opis sezonu (albo programu). Przycisk „Oznacz jako obejrzany”, reakcje, notatka jako mały link na dole, przyciski „‹ poprzedni / następny ›”.
3. **Profil kompaktowy**: jedna karta — awatar, nazwa, czas przed ekranem w jednym wierszu, 6 małych liczników w jednym rzędzie i podział seriale/filmy; mniejsze okładki na półkach, nagłówki bez emoji.
4. **„Obejrzane wszystko”**: przycisk na stronie serialu (obok „Obejrzany SxxExx”) i w rozwiniętej grupie w „Do obejrzenia”; pyta w ładnym okienku i zaznacza wszystkie wyemitowane odcinki.
5. **Pytanie o poprzednie**: przy zaznaczeniu odcinka lub sezonu, jeśli wcześniej są nieobejrzane odcinki, okienko „Zaznaczyć też poprzednie? Przed sezonem 6 jest jeszcze 50 nieobejrzanych odcinków…” z przyciskami „Tak, zaznacz poprzednie (50)” / „Tylko ten sezon/odcinek”. Systemowe okienka `confirm` zastąpione własnym okienkiem w stylu aplikacji (`ask`).
6. **„Do obejrzenia”**: każdy serial to zwinięta karta (okładka, liczba zaległych odcinków, następny odcinek, serwis, data nowego odcinka); kliknięcie rozwija listę (pierwsze 10 + „Pokaż wszystkie”) ze stopką „Otwórz serial ›” i „Obejrzane wszystko”. Filmy — jedna zwijana karta „Filmy do obejrzenia”.
7. **Filmy → Szukaj**: sekcje z całej bazy filmów: „Popularne filmy”, „Do obejrzenia w polskich serwisach”, „Najpopularniejsze wszech czasów”, „Najwyżej oceniane”, „Polskie filmy”, „Klasyka kina”. (Seriale: dodana sekcja „Najwyżej oceniane seriale”.)
8. **Nowa zakładka „Kino”** w dolnym menu: „Teraz w kinach” (repertuar w Polsce, od najpopularniejszych, „W kinach od …”) i „Wkrótce w kinach” (zapowiedzi z **polskimi** datami premier kinowych, pogrupowane wg miesięcy, „Premiera za 3 dni (6 lis 2026)”); przy każdym filmie „+” = „Chcę obejrzeć”.

Testy (serwer testowy 8002, konto testowe): zaznaczenie sezonu 6 Gry o tron → okienko o 50 poprzednich → „Tak” → 60 obejrzanych ✔; zaznaczenie S08E03 → pytanie → „Tylko ten odcinek” ✔; karta odcinka Hotel Paradise bez opisu → komunikat + opis sezonu 13 + nawigacja ‹ › ✔; karta odcinka Gry o tron z pełnym polskim opisem ✔; „Do obejrzenia” zwinięte, rozwinięcie pokazuje odcinki z miniaturkami i stopkę ✔; Kino: 40 filmów teraz, 19 zapowiedzi z polskimi datami ✔; Filmy → Szukaj: 6 nowych sekcji ✔; Profil kompaktowy ✔; poprawiona odmiana („jest jeszcze 50 nieobejrzanych odcinków”). Konto testowe usunięte.

### 2026-11-04 — Polecenie 14
> 1. dodaj opcję przy serialach „przerwane oglądanie” — serial się popsuł i nie chcę dalej oglądać, ale chcę mieć zaznaczone, do jakiego momentu oglądałam; nie ma się usuwać z profilu, tylko trafić do „Przerwane”, z możliwością wznowienia
> 2. jeśli to możliwe, dodaj zwiastuny pod serialami lub filmami
> 3. pod filmem lub serialem podobne lub powiązane filmy i seriale

Zmiany:
1. **Przerwane oglądanie**: na stronie serialu przycisk „Przerwij oglądanie” → okienko z informacją o zapisanym postępie („obejrzane do S03E05”) → serial dostaje znacznik `dropped` (data). Taki serial:
   - zostaje na koncie razem z obejrzanymi odcinkami, recenzją i notatkami;
   - znika z „Oglądasz/Chcę obejrzeć/Na bieżąco”, z „Do obejrzenia”, z kalendarza „Nadchodzące” i z kropki „dziś”;
   - jest w sekcji **„Przerwane”** na dole „Moich seriali” (wyszarzona okładka, „obejrzane do …”, data przerwania, przycisk „Wznów”) i na półce „Przerwane” w Profilu;
   - na jego stronie widać ramkę „Oglądanie przerwane …” z przyciskiem „Wznów oglądanie”.
2. **Zwiastuny** (TMDB → YouTube): sekcja „Zwiastun” na stronie serialu i filmu; najpierw polski, potem angielski; podgląd (kadr + przycisk ▶) — film ładuje się dopiero po kliknięciu, przez `youtube-nocookie.com` (bez śledzenia przed odtworzeniem). Dodatkowe zwiastuny jako przyciski „▶ Zwiastun 2/3…”. Gdy w bazie nie ma zwiastuna (np. Hotel Paradise) — przycisk „Poszukaj zwiastuna na YouTube”.
3. **Powiązane tytuły**: przewijany rząd okładek „Polecane seriale / Polecane filmy” (rekomendacje TMDB; gdy brak — „Podobne”); dla polskich produkcji dodatkowo „Polskie programy i seriale z tego gatunku” (bo rekomendacje TMDB dla polskich programów bywają przypadkowe). Każdą okładkę można od razu dodać przyciskiem „+”.
   - Dane pobierane w tym samym zapytaniu co strona (`append_to_response=videos,recommendations,similar`, `include_video_language=pl,en,null`).

Testy (serwer testowy 8002, konto testowe): Gra o tron — zwiastun, odtwarzanie po kliknięciu, „Polecane seriale”: Ród Smoka, Szmaragdowy Gród, Wiedźmin… ✔; przerwanie po 25 odcinkach → ramka „Obejrzane do S03E05 (25/73)”, sekcja „Przerwane” w Moich serialach, brak w „Do obejrzenia” ✔; wznowienie ✔; Hotel Paradise — „Polskie programy i seriale z tego gatunku” (Jeden z dziesięciu, The Voice of Poland, Top Model…), przycisk szukania zwiastuna ✔; Matrix — zwiastun + 4 dodatkowe, „Polecane filmy”: Matrix Reaktywacja, Rewolucje, Zmartwychwstania ✔. Poprawka: dodatkowe zwiastuny miały takie same nazwy → numeracja. Konto testowe usunięte.

### 2026-11-04 — Polecenie 15
> (zrzut: „Dostępność w Polsce: JustWatch (przez TMDB). Kliknij serwis, aby go otworzyć.”)
> 1. gdy się wchodzi w kina, niech będzie opcja wybrania miasta i kina, i wtedy będą ściągane filmy
> 2. usuń to, co wysłałam na zdjęciu
> 3. dodaj zakładkę, która będzie analizowała obejrzane filmy i seriale lub te odłożone na później i na tej podstawie dawała więcej takich, które mogą się spodobać
> 4. propozycje filmów/seriali niech się mieszają, żeby nie było ciągle tego samego
> 5. nie dawaj opcji „pokaż więcej”, tylko od razu pokazuj wszystko

Źródła repertuaru (sprawdzone): publiczne dane repertuarowe stron sieci **Cinema City** (36 kin), **Multikino** (38) i **Helios** (52) — razem 126 kin. Cinema City i Helios zwracają repertuar wszystkich kin; Multikino udostępnia publicznie repertuar tylko części kin (pozostałe odpowiadają „401 — brak dostępu”). Tego ograniczenia nie obchodzimy — dla takich kin aplikacja pokazuje komunikat i przycisk do repertuaru na stronie Multikina.

Zmiany:
1. **Kino → Repertuar** (nowa pierwsza podzakładka): wybór **miasta** i **kina** (sieć · nazwa), wybór dnia (dziś + 6 dni), lista filmów z plakatem, długością i **godzinami seansów** (z wersją: 2D/3D/IMAX/4DX, napisy/dubbing); kliknięcie godziny otwiera zakup biletu na stronie kina; minione seanse dzisiaj są przekreślone; „Opis, zwiastun i gdzie obejrzeć ›” wyszukuje film w bazie i otwiera jego stronę. Wybrane miasto i kino zapamiętywane na koncie (`state.prefs`). Pozostałe podzakładki: „Teraz w kinach”, „Wkrótce”.
   - `server.py`: nowe `GET /api/kina` (lista kin z 3 sieci, pamięć podręczna 12 h) i `GET /api/seanse?kino=…&data=…` (ujednolicony repertuar, pamięć 15 min); tylko dla zalogowanych, z kontrolą parametrów.
2. Usunięto dopisek „Dostępność w Polsce: JustWatch (przez TMDB)…” z panelu „Gdzie obejrzeć” (informacja o źródle została tylko w stopce Profilu).
3. **Nowa zakładka „Dla Ciebie”** (w dolnym menu): analizuje seriale (liczba obejrzanych odcinków, ocena, ulubione; przerwane pomijane) i filmy (obejrzane, na później, ocena, ulubione) → losuje ważone „ziarna” → zbiera rekomendacje TMDB + popularne tytuły z ulubionych gatunków → sortuje wg dopasowania z odrobiną losowości. Sekcje „Seriale, które mogą Ci się spodobać” i „Filmy…”, przy każdej okładce „bo: Gra o tron” / „bo: gatunek: Dramat”; tytuły już dodane są pomijane. Przycisk „↻ Inne propozycje”.
4. **Mieszanie propozycji**: sekcje w „Szukaj” (seriale i filmy) losują stronę wyników i kolejność przy każdym wejściu; „Podobne i polecane” na stronach seriali/filmów łączą rekomendacje i podobne, bez tytułów już dodanych, w losowej kolejności (stałej w obrębie jednej wizyty, żeby nie skakało przy klikaniu).
5. **Bez „Pokaż więcej”**: listy (gatunki, polskie, itp.) doładowują się same przy przewijaniu; w „Do obejrzenia” po rozwinięciu serialu od razu wszystkie odcinki; sekcje w „Szukaj” pokazują od razu całe strony wyników (20).
   - `server.py`: dozwolone też `tv|movie/{id}/recommendations` i `/similar` (więcej różnych propozycji).

Testy (serwer testowy 8002, konto testowe): Warszawa → 12 kin; Cinema City Arkadia — 35 filmów z godzinami, zmiana dnia, przejście do strony filmu („Lalka”) ✔; Multikino Złote Tarasy — komunikat + link do repertuaru ✔; „Dla Ciebie” — 60 propozycji z uzasadnieniem, po odświeżeniu 0/15 powtórzeń ✔; sekcje „Szukaj” różne przy kolejnych wejściach ✔; automatyczne doładowanie listy przy przewijaniu (20 → 40) ✔ (dodano też zapasowe sprawdzanie przy przewijaniu). Konto testowe usunięte.

Uwaga: zmienił się `server.py` — trzeba zamknąć okno serwera i uruchomić ponownie `start.bat`.

### 2026-11-04 — Polecenie 16
> (zrzut strony serialu Riverdale) 1. przejrzyj inne aplikacje i zmień to tak, żeby nie było takie surowe — ma być przyjemne dla oka i intuicyjne
> 2. opcja, żeby użytkownik mógł customizować wygląd aplikacji — np. 10 proponowanych wyglądów (głównie kolory) do przełączania
> 3. na stronie serialu linia postępu w poprzek; gdy obejrzane wszystko, ale wyjdą nowe odcinki — cała linia na zielono i „jesteś na bieżąco”; gdy obejrzane wszystko i więcej odcinków nie będzie — na czerwono i komunikat o zakończeniu

Inspiracje (wzorce z aplikacji do śledzenia seriali typu TV Time, Trakt, Letterboxd): jeden wyraźny pasek postępu z liczbą, karta „następny odcinek” z kadrem i jednym przyciskiem, zakładki zamiast jednej długiej strony, rzadkie akcje schowane w menu, ulubione jako serduszko na zdjęciu.

Zmiany:
1. **Nowa strona serialu**:
   - serduszko „ulubione” w rogu zdjęcia (zamiast osobnego przycisku);
   - pod zdjęciem tylko „✓ W moich serialach” + przycisk **„⋯”** otwierający menu: „Obejrzane wszystko”, „Przerwij/Wznów oglądanie”, „Usuń z moich seriali” (z potwierdzeniem — usuwa też zaznaczone odcinki i notatki); dla niedodanych — jeden szeroki przycisk „+ Dodaj do moich seriali”;
   - **karta postępu** (pkt 3) i **karta „Następny do obejrzenia”** z kadrem, tytułem, datą i ✓;
   - **zakładki: Odcinki / O serialu / Podobne** (Odcinki domyślnie dla dodanych seriali, O serialu dla niedodanych); „O serialu” = recenzja, opis z twórcami, zwiastun, gdzie obejrzeć, Wikipedia, obsada;
   - przy każdym sezonie mały pasek postępu, obejrzane odcinki przygaszone.
   - Strona filmu: serduszko na zdjęciu, dwa równe przyciski „Chcę obejrzeć później” / „Już obejrzany”; po obejrzeniu „✓ Obejrzany (data)” + „Cofnij”.
2. **10 motywów** (Profil → Ustawienia → Wygląd, podgląd kolorów na kafelkach): Krem (domyślny), Szałwia, Ocean, Lawenda, Pudrowy róż, Piasek, Mięta, oraz ciemne: Wieczór, Noc, Grafit. Wybór zapisywany w przeglądarce i na koncie (działa na każdym urządzeniu po zalogowaniu). Dawne „Jasny/Wieczorny” przechodzą automatycznie na „Krem/Wieczór”.
3. **Pasek postępu z kolorami** (strona serialu i lista „Moje seriale”):
   - w trakcie — kolor motywu, „Obejrzane 85% · zostało 20 odcinków · ok. 14 h”, liczba 117/137;
   - **na bieżąco** — cały pasek zielony, „Jesteś na bieżąco” + data następnego odcinka, jeśli znana;
   - **zakończony** — cały pasek czerwony, „Serial zakończony — obejrzane wszystkie odcinki, nowych już nie będzie” (status Ended/Canceled i brak zapowiedzianych odcinków);
   - przerwany — szary; jeszcze nie zaczęty — pusty.

Testy (serwer testowy 8002, konto testowe): Riverdale 117/137 → „Obejrzane 85%”, karta następnego odcinka S07E01, menu ⋯ ✔; Breaking Bad (wszystko obejrzane, zakończony) → czerwony „Serial zakończony” ✔; Hotel Paradise (wszystko obejrzane, emitowany) → zielony „Jesteś na bieżąco · Nowy odcinek S13E42 — jutro” ✔; zakładki Odcinki/O serialu ✔; 10 motywów — przełączanie i zapis na koncie ✔ (zrzuty: Krem, Noc, Mięta, Lawenda). Konto testowe usunięte.

### 2026-11-04 — Polecenie 17
> 1. czemu nie ma serialu The Originals
> 2. jak się wejdzie na kogoś z obsady, to można zobaczyć jego inne filmy lub seriale
> 3. dodaj więcej osób w obsadzie (jest tylko kilka), mogą być ich zdjęcia, żeby łatwiej było znaleźć
> → dopisane w trakcie: 4. w „Do obejrzenia” można też bezpośrednio wejść na film lub serial; 5. przy zaznaczaniu filmu/serialu w „Dla Ciebie” ekran ma się nie cofać, tylko zostać w tym samym miejscu

Ustalenia:
1. „The Originals” **jest** w bazie (TMDB 46896) — aplikacja pokazywała go pod polskim tytułem **„Pierwotni”**, bez oryginalnej nazwy, więc trudno go było rozpoznać. Teraz na każdej okładce pod polskim tytułem jest oryginalny (kursywą), gdy się różni — „Pierwotni / The Originals” jest 1. wynikiem dla „the originals”.

Zmiany:
2. **Strona osoby** (`#/person/ID`, kliknięcie w kogoś z obsady): zdjęcie, zawód, data i miejsce urodzenia, wiek, biografia po polsku (gdy brak — po angielsku z oznaczeniem), liczba seriali i filmów, rząd „Najbardziej znane” oraz siatki **„Seriale”** i **„Filmy”** (od najnowszych) z rolą „jako …”; pomijane są występy „jako on/ona sam(a)”. Każdy tytuł można od razu dodać „+”.
   - `server.py`: dozwolona ścieżka TMDB `person/{id}`.
3. **Pełna obsada ze zdjęciami**: seriale — obsada ze wszystkich sezonów (`aggregate_credits`, np. Pierwotni: 250 osób) z postacią i liczbą odcinków, posortowana wg liczby odcinków; filmy — cała obsada z postaciami. Przewijany rząd okrągłych zdjęć (ładowane w miarę przewijania).
4. **„Do obejrzenia”**: kliknięcie okładki lub tytułu serialu, albo przycisku **„Otwórz”**, otwiera stronę serialu; kliknięcie reszty karty nadal rozwija/zwija listę odcinków. W grupie filmów przy każdym filmie przycisk „Otwórz”.
5. **„Dla Ciebie” bez skakania ekranu**: propozycje są liczone raz na wejście w zakładkę (nie od nowa po każdym dodaniu), a dodany tytuł zostaje na swoim miejscu z ✓ — siatka się nie przesuwa i ekran zostaje w tym samym miejscu (sprawdzone: pozycja przewinięcia przed i po kliknięciu identyczna, 60/60 kafelków). Nowe propozycje — przycisk „↻ Inne propozycje” albo ponowne wejście w zakładkę.

Testy (serwer testowy 8002, konto testowe): wyszukiwanie „the originals” → „Pierwotni / The Originals” ✔; obsada Pierwotnych: 250 osób, zdjęcia, „Klaus Mikaelson · 92 odcinki” ✔; strona Josepha Morgana: biografia PL, 13 seriali, 13 filmów, role ✔; „Do obejrzenia”: rozwijanie, „Otwórz”, tytuł → strona serialu, film → strona filmu ✔; „Dla Ciebie”: dodanie z dołu listy bez przewinięcia ✔. Konto testowe usunięte.

Uwaga: zmienił się `server.py` — trzeba ponownie uruchomić `start.bat`.

### 2026-11-04 — Polecenie 18 (dopisane w trakcie)
> „daj koło każdego sezonu i odcinka, jeśli się nie obejrzało, opcję »nie obejrzę«, i żeby nie liczyło się to wtedy do paska, który liczy postęp w serialu — np. Hotel Paradise nie ma już pierwszych sezonów i nie będę go oglądać, bo nawet nie ma gdzie”
> „jak jest obsada, to niech będzie opcja »pokaż więcej« i wtedy się będzie rozwijać na dół lista aktorów”

Zmiany:
1. **„Nie obejrzę”** (nowe `state.skipped`):
   - przy każdym nieobejrzanym odcinku przycisk **⊘** (pominięty odcinek: przygaszony, przekreślony, dopisek „nie obejrzę”, przycisk **↺** przywraca);
   - przy każdym sezonie przycisk **⊘** „Nie obejrzę tego sezonu” → okienko z potwierdzeniem → pomija wszystkie nieobejrzane odcinki sezonu (także przyszłe); przy pominiętym sezonie **↺** przywraca; w nagłówku sezonu „pominięty” / „N pomin.”;
   - w karcie odcinka przycisk „⊘ Nie obejrzę” / „↺ Przywróć odcinek”;
   - pominięte odcinki **nie liczą się** do paska postępu, „Obejrzane X/Y”, „Do obejrzenia”, „Następny do obejrzenia”, „Obejrzane wszystko”, pytania o poprzednie odcinki, kalendarza i półek w Profilu; zaznaczenie odcinka jako obejrzanego automatycznie zdejmuje „nie obejrzę”.
   - Test: Hotel Paradise z obejrzanymi sezonami 12–13 → 91/623 (15%); po pominięciu sezonu 1 → 91/583; po pominięciu sezonów 1–11 → **„Jesteś na bieżąco” 91/91** (zielony pasek); przywrócenie 1 odcinka → 91/92; „Do obejrzenia” liczy tylko przywrócony odcinek ✔.
2. **Obsada „Pokaż więcej”**: domyślnie 12 osób w siatce ze zdjęciami; przycisk „Pokaż więcej (238)” rozwija w dół pełną listę (np. 250 osób w „Pierwotnych”), „Zwiń obsadę” chowa. (To wyjątek od wcześniejszej zasady „bez pokaż więcej” — na wyraźną prośbę użytkownika.)

Konto testowe usunięte.

### 2026-11-04 — Polecenie 19
> „powiedz mi, gdzie mogę postawić tę aplikację, żeby mieć ją na telefonie na iPhone”

Odpowiedź (bez zmian w kodzie) — możliwości:
1. **Sieć domowa (za darmo)**: `set HOST=0.0.0.0` + `python server.py` na komputerze, na iPhonie w Safari `http://<IP komputera>:8000` → „Udostępnij → Do ekranu początkowego”. Działa tylko w domowym Wi-Fi i gdy komputer jest włączony.
2. **Tailscale (za darmo)**: prywatna sieć VPN między komputerem a iPhonem — aplikacja dostępna z każdego miejsca (komórkowy internet też), bez wystawiania jej do internetu. Komputer musi być włączony.
3. **Hosting działający 24/7**: aplikacja potrzebuje Pythona i stałego dysku na `serialog.db` + HTTPS — np. Railway (z wolumenem), Fly.io (z wolumenem) albo mały serwer VPS (np. polski Mikrus, Hetzner, OVH) z Caddy jako HTTPS. Darmowe plany typu Render free się nie nadają (brak stałego dysku — konta by znikały).
Do zrobienia przy hostingu w internecie: HTTPS, ciasteczko sesji z flagą `Secure`, ikona i manifest, żeby aplikacja ładnie działała z ekranu początkowego iPhone'a.

### 2026-11-04 — Polecenie 20
> „a nie ma jakiejś darmowej strony, gdzie można to postawić, a potem udostępnić na ekran główny telefonu?”

Sprawdzono (lista dozwolonych stron PythonAnywhere, pythonanywhere.com/whitelist):
- **PythonAnywhere — plan darmowy**: adres `nazwa.pythonanywhere.com` z HTTPS, stały dysk (SQLite działa), bez karty płatniczej. Na darmowym planie serwer może łączyć się tylko z dozwolonymi stronami: `api.themoviedb.org` **jest** na liście (filmy, seriale, „gdzie obejrzeć”, polskie opisy działają), ale **Cinema City, Multikino i Helios nie** — zakładka Kino → Repertuar nie działałaby (reszta Kina tak). Wikipedia/Wikidata/YouTube łączą się z przeglądarki, więc działają. Raz na 3 miesiące trzeba kliknąć „przedłuż” w panelu. Wymaga przerobienia `server.py` na format WSGI.
- **Oracle Cloud „Always Free”**: darmowy serwer 24/7 bez ograniczeń (działa wszystko, także repertuar kin), ale wymaga weryfikacji kartą i więcej konfiguracji.
- **Tailscale + własny komputer**: za darmo, wszystko działa, ale komputer musi być włączony.

### 2026-11-04 — Polecenie 21
> „Tak, PythonAnywhere”

Zmiany:
1. **`server.py` przebudowany**: cała obsługa zapytań w jednej funkcji `handle()` (klasa `Request`, funkcja `route()`), z której korzystają dwa „wejścia”:
   - lokalny serwer (`start.bat` / `python server.py`) — jak dotąd;
   - **WSGI** — funkcja `application(environ, start_response)` dla hostingu (PythonAnywhere: plik WSGI z linią `from server import application`).
   - Przez HTTPS ciasteczko sesji ma flagę **`Secure`**; adres IP klienta za pośrednikiem hostingu brany z `X-Real-IP`/`X-Forwarded-For` (limit nieudanych logowań działa poprawnie); nieobsługiwane metody → 405; błędy wewnętrzne nie pokazują szczegółów.
   - Serwowane pliki: tylko `index.html`, `manifest.json` i ikony (baza, klucz i kod nadal niedostępne).
2. **Instalacja na telefonie**: `manifest.json`, ikony `icon-180/192/512.png` (wygenerowane skryptem — terakota + biały „play”), meta-tagi Apple (`apple-touch-icon`, `apple-mobile-web-app-capable`, tytuł, kolor) → z ekranu głównego iPhone'a aplikacja otwiera się na pełnym ekranie.
3. **Kino → Repertuar** na serwerze bez dostępu do stron kin (darmowy PythonAnywhere): czytelny komunikat + linki do stron Cinema City / Multikino / Helios zamiast pustej listy.
4. **Paczka do wgrania**: `serialog_pythonanywhere.zip` (index.html, server.py, manifest, ikony, tmdb_klucz.txt, serialog.db z kontem „julkar8”).
5. **`INSTRUKCJA_PYTHONANYWHERE.md`** — krok po kroku: konto Beginner → upload + unzip → Web app (Manual configuration) → plik WSGI → Force HTTPS → Reload → iPhone „Do ekranu początkowego”; przedłużanie co 3 miesiące, aktualizacje, logi błędów.

Testy:
- WSGI (na kopii aplikacji w folderze tymczasowym, z udawanymi nagłówkami hostingu): strona, manifest, ikony ✔; `/server.py`, `/serialog.db`, `/tmdb_klucz.txt`, `/../server.py` → 404 ✔; rejestracja, `/api/me`, zapis stanu ✔; TMDB przez pośrednika ✔, bez logowania 401 ✔; ciasteczko `Secure` przy HTTPS, bez — brak ✔; blokada po 10 złych hasłach dla IP z `X-Real-IP` ✔; DELETE → 405 ✔.
- Lokalnie (port 8002): logowanie, serial, Kino, manifest/ikona w nagłówku, zapis na koncie ✔. Konta testowe usunięte.

Do zrobienia przez użytkownika: założenie konta na PythonAnywhere i wykonanie kroków z instrukcji (konta za użytkownika nie zakładamy).

### 2026-11-04 — Polecenie 22
> „nie możesz tego jakoś przez GitHuba zrobić?”

Odpowiedź (bez zmian w kodzie):
- **GitHub sam nie uruchomi tej aplikacji** — GitHub Pages serwuje tylko pliki statyczne, a SeriaLog potrzebuje serwera (konta, baza, ukryty klucz TMDB, pośrednik do bazy filmów).
- GitHub może za to **ułatwić wgranie i aktualizacje na PythonAnywhere**: kod w prywatnym repozytorium → na PythonAnywhere `git clone` (raz), a każda aktualizacja to `git pull` + Reload, bez ręcznego wgrywania plików. Klucz TMDB i baza kont **nie trafiają** do repozytorium (`.gitignore`) — wgrywa się je raz osobno.
- Sprawdzono: na komputerze jest `git` i `gh` (GitHub CLI), ale `gh` nie jest zalogowany — logowanie do GitHuba musi wykonać użytkownik.

### 2026-11-04 — Polecenie 23
> „Tak, przygotuj” → „wolę, żebyś sam wysyłał tam pliki, a potem mówił mi, co muszę pisać w konsoli na PythonAnywhere”

Kroki:
1. Sprawdzono, że klucz TMDB występuje tylko w `tmdb_klucz.txt`.
2. Dodano `.gitignore` (wyklucza `tmdb_klucz.txt`, `serialog.db`, `*.zip`, `.claude/`), `tmdb_klucz.przyklad.txt` (wzór pliku z kluczem), `README.md`.
3. `git init` (gałąź `main`), pierwszy commit `b0b72e5` — 12 plików, bez klucza i bazy.
4. Uruchomiono logowanie do GitHuba (`gh auth login --web`) w terminalu użytkownika — logowanie wykonuje użytkownik.
5. Do decyzji: repozytorium publiczne (PythonAnywhere pobiera je jedną komendą) czy prywatne (na darmowym PythonAnywhere potrzebny wtedy token dostępu GitHub — darmowe konto nie łączy się z GitHubem przez SSH).

### 2026-11-04 — Polecenie 24
> „Prywatne” → zaraz potem: „zrób publiczne i powiedz jeszcze raz, jak zalogować się do GitHub”

- Decyzja: repozytorium **publiczne** (PythonAnywhere pobierze je bez tokena). Klucz TMDB i baza kont i tak nie trafiają do repozytorium.
- Logowanie do GitHuba czeka na użytkownika w terminalu (`gh auth login --web`).

### 2026-11-04 — Polecenie 25
> „już” (zalogowano do GitHuba)

1. Zalogowano jako **juliaradosz**.
2. Utworzono **publiczne** repozytorium **https://github.com/juliaradosz/serialog** i wysłano gałąź `main` (12 plików).
3. Sprawdzono przez API GitHuba: w repozytorium **nie ma** `tmdb_klucz.txt` ani `serialog.db`.
4. Przepisano `INSTRUKCJA_PYTHONANYWHERE.md` pod GitHub: `git clone https://github.com/juliaradosz/serialog.git` w konsoli Bash, ręczne wgranie 2 plików (klucz + baza) przez zakładkę Files, konfiguracja WSGI, Force HTTPS, Reload, iPhone; aktualizacje: `cd ~/serialog && git pull` + Reload.

### 2026-11-04 — Polecenie 26
> (zrzut: strona PythonAnywhere „Coming Soon!”)

- Diagnoza: konto i adres istnieją, ale nie utworzono jeszcze aplikacji WWW (zakładka Web → „Add a new web app”) albo otwierany jest adres innego regionu (konto EU ma adres `nazwa.eu.pythonanywhere.com`). Podano kroki 4–6 instrukcji ponownie.

### 2026-11-04 — Polecenie 27
> (log błędu PythonAnywhere) `ModuleNotFoundError: No module named 'server'` w `/var/www/julkar9_pythonanywhere_com_wsgi.py`

- Diagnoza: nazwa użytkownika na PythonAnywhere to **julkar9**; Python nie znalazł `server.py` pod ścieżką z pliku WSGI — albo w pliku została ścieżka z `TWOJA_NAZWA`, albo folder `/home/julkar9/serialog` nie istnieje (nie wykonano `git clone`). Podano gotowy plik WSGI z `path = '/home/julkar9/serialog'` i komendy sprawdzające.

### 2026-11-04 — Polecenie 28
> (zrzut pliku WSGI z ostrzeżeniem „'server.application' imported but unused”)

- Plik WSGI poprawny. Ostrzeżenie edytora jest niegroźne — PythonAnywhere sam używa zmiennej `application`. Dalej: Save → Reload → sprawdzić stronę/Error log.

### 2026-11-04 — Polecenie 29
> 1. na profilu przycisk na dole, który pokazuje edycję koloru tła itp. — można wybrać, który się chce, a jak coś nie będzie pasować, to jeszcze dopasować paskiem natężenie koloru itp.
> 2. usuń repertuar, skoro i tak nie działa
> 3. w „Dla Ciebie” zrób podział na filmy i seriale
> → dopisane w trakcie: dopasuj do telefonu — nie da się nic przybliżać/oddalać, od razu dopasowane do ekranu; zakładki Seriale i Filmy na dole mają najpierw otwierać wyszukiwanie nowych, a „Moje” przełącza się po prawej u góry

Zmiany:
1. **„Dostosuj wygląd”** — przycisk na dole Profilu (z podglądem kolorów) otwiera panel: (1) wybór jednego z 10 motywów, (2) suwaki: **Kolor akcentu** (tęcza), **Natężenie akcentu**, **Kolor tła** (tęcza), **Natężenie tła**, **Jasność tła**. Podgląd na żywo podczas przesuwania, zapis po puszczeniu suwaka (na koncie i w przeglądarce); „Przywróć kolory motywu”. Wybór innego motywu kasuje własne dopasowania. Kolory liczone osobno dla jasnych i ciemnych motywów, żeby zawsze był czytelny kontrast.
2. **Repertuar usunięty** — z aplikacji (zakładka, wybór kina, seanse, style) i z serwera (`/api/kina`, `/api/seanse`, kod pobierania z Cinema City/Multikina/Helios). Kino ma teraz: „Teraz w kinach” i „Wkrótce w kinach”.
3. **„Dla Ciebie”**: zakładki **Seriale / Filmy** (po 40 propozycji); przełączanie bez przeliczania propozycji.
4. **Telefon**: wyłączone przybliżanie (meta viewport `maximum-scale=1, user-scalable=no`, blokada gestu szczypania w Safari, `touch-action: manipulation` — bez przybliżania podwójnym stuknięciem), pola tekstowe 16 px (iPhone nie przybliża przy wpisywaniu), bez przewijania w bok, uwzględnione wcięcia ekranu iPhone'a (notch, pasek na dole).
5. **Dolne menu Seriale/Filmy** otwiera **„Szukaj”**; kolejność zakładek: Szukaj · Gatunki · **Moje seriale/filmy** (po prawej). Logo i adres startowy też prowadzą do wyszukiwania.

Testy (serwer testowy, widok telefonu 375 px): brak przewijania w bok na 10 ekranach (Seriale, serial, Filmy, Kino×2, Dla Ciebie, Do obejrzenia, Nadchodzące, Profil, aktor) ✔; „Dla Ciebie” Seriale/Filmy po 40, przełączanie bez ładowania ✔; „Dostosuj wygląd”: 10 motywów, 5 suwaków, zmiana koloru akcentu i tła na żywo + zapis na koncie ✔; Kino bez Repertuaru ✔; dolne menu → Szukaj, „Moje” po prawej ✔. Konta testowe usunięte.

Wysłano na GitHub — na PythonAnywhere: `cd ~/serialog && git pull` + Reload.
