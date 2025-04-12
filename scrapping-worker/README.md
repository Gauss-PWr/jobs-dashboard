# SCRAPPING WORKER

_Wpisujcie tu TODO, pomysły żeby nie zapomnieć, jak uruchomić projekt_

### Uruchamianie (justjoin.it)

Aby uruchomić skrypt scrapujący oferty, trzeba mieć zainstalowane selenium. Możemy je zainstalować komendą (będąc w folderze `scrapping-worker`):

```pip install -r requirements.txt```

Musimy mieć też zainstalowanego Firefoxa, ale z tym raczej nie powinno być problemu.

Skrypt bierze dwa argumenty: url i plik wyjściowy. Przykładowe uruchomienie:

```py ./justjoinit/scraper.py https://justjoin.it/job-offers/all-locations/data offers.xml```