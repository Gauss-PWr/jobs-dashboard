# SCRAPPING WORKER

### Uruchamianie (justjoin.it)

#### 1. Skrypt pobierający linki do ofert

Aby uruchomić skrypt, trzeba mieć zainstalowane selenium. Możemy je zainstalować komendą (będąc w folderze `scrapping-worker`):

```pip install -r requirements.txt```

Musimy mieć też zainstalowanego Firefoxa, ale z tym raczej nie powinno być problemu.

Skrypt bierze dwa argumenty: url i ścieżkę wyjściową. Przykładowe uruchomienie:

```py ./justjoinit/scrape_urls.py https://justjoin.it/job-offers/all-locations/data ./justjoinit/offers_urls.txt```

W podanej ścieżce wyjściowej zostanie zapisana lista linków do ofert, która może zostać podana do drugiego skryptu

#### 2. Skrypt pobierający pełne oferty

Wymagania do uruchomienia są takie same. Jako argumenty podajemy plik wejścia z listą linków i folder wyjściowy, np.:

```py ./justjoinit/scrape_full_offers.py ./justjoinit/offers_urls.txt ./justjoinit/offers```

Skrypt pobiera strony ofert i zapisuje je do plików html w podanym folderze. Po odpaleniu pliku html w przeglądarce nie wygląda on tak samo jak na stronie, jednak są w nim zawarte wszystkie potrzebne informacje.

#### 3. Skrypt parsujący oferty do JSONa

Do uruchomienia skryptu potrzebna jest biblioteka AdvancedHTMLParser, jeżeli nie jest ona zainstalowana, należy ponownie wykonać (z folderu `scrapping-worker`) komendę:

```pip install -r requirements.txt```

Jako argumenty do skryptu podajemy ścieżkę do folderu z HTMLami ofert oraz ścieżkę do pliku wyjściowego JSON, np:

```py ./justjoinit/parser.py ./justjoinit/offers ./justjoinit/offers.json```

Skrypt wyciągnie z HTMLów ofert przydatne informacje i zapisze je w JSONie.

### TODO: pracuj.pl / inne strony z ofertami