from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import sys
import time

def scrape_all_offers(url, output_file):
    """
    Funkcja pobiera oferty z justjoin.it pod podanym adresem poprzez przescrollowanie listy ofert i zapisanie elementów html.
    Muszą być one zapisywane na bieżąco bo tylko kilka ofert jest widocznych na raz
    """
    print("Pobieranie ofert...")

    options = FirefoxOptions()
    options.add_argument("--headless")  # żeby okienka nie było
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(10)  # czekamy aż strona się załaduje

    def scroll(start_height, scroll_amount, step=200):
        for height in range(start_height + step, start_height + scroll_amount + step, step):
            driver.execute_script(f"window.scrollTo(0, {height});")
            time.sleep(0.2)

    # będziemy zapisywać oferty po indeksach żeby nie było powtórek
    offers = {}

    expected_height = 0
    while 1:
        scroll(start_height=expected_height, scroll_amount=1000)
        expected_height += 1000

        # dodajemy do offers
        elements = driver.find_elements(By.XPATH, "//div[@data-test-id='virtuoso-item-list']/div")
        for element in elements:
            index = int(element.get_attribute("data-index"))
            if index not in offers.keys():
                offers[index] = element.get_attribute("outerHTML")

        # jak zjedzie o mniej niż chcieliśmy to znaczy że zjechaliśmy do końca
        if driver.execute_script("return document.body.scrollHeight") < expected_height:
            break

    # zapisujemy oferty do pliku oddzielone enterami
    file = open(output_file, "w", encoding="utf-8")
    file.write("<offers>\n" + "\n".join(offers.values()) + "\n</offers>")  # musimy mieć jednego roota w xmlu
    file.close()

    driver.close()

def main():
    args = sys.argv

    URL = args[1]
    OUTPUT_FILE = args[2]

    scrape_all_offers(URL, OUTPUT_FILE)

if "__main__" == __name__:
    main()