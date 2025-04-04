# Jobs Dashboard - wykrywanie i wyróżnianie trendów na rynku pracy.

## Struktura

1. scrapping-worker - skrypt/program do scrapowania danych. 
2. dashboard-backend - serwis do przyjmowania danych ze scrappera, czyszczenia ich w bazie i serwowania do aplikacji webowej.
3. dashboard-frontend - serwis do wyświetlania dashboardu.

## Zasady

1. **NIE** commitujesz na **main**, tworzysz pull request ze swojego brancha.
2. Jeśli tworzysz brancha, rób to w taki sposób: [środowisko]/[część kodu nad którą pracujesz]/[nowa funkcjonalność / naprawa błędu], przykładowo:
    - dev/worker/fix
    - stg/frontend/trend-plot

TBA