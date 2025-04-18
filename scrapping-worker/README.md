# SCRAPPING WORKER

_Wpisujcie tu TODO, pomysły żeby nie zapomnieć, jak uruchomić projekt_

### Uruchamianie (justjoin.it)

#### 1. Skrypt pobierający linki do ofert

Aby uruchomić skrypt, trzeba mieć zainstalowane selenium. Możemy je zainstalować komendą (będąc w folderze `scrapping-worker`):

```pip install -r requirements.txt```

Musimy mieć też zainstalowanego Firefoxa, ale z tym raczej nie powinno być problemu.

Skrypt bierze dwa argumenty: url i plik  wyjściowy. Przykładowe uruchomienie:

```py ./justjoinit/scrape_urls.py https://justjoin.it/job-offers/all-locations/data offers_urls.txt```

#### 2. Skrypt pobierający pełne oferty

Wymagania do uruchomienia są takie same. Jako argumenty podajemy plik wejścia z listą linków i folder wyjściowy, np.:

```py ./justjoinit/scrape_full_offers.py ./offers_urls.txt ./offers```