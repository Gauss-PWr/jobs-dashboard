from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import sys
import time

def scrape_offers_urls(url, output_dir):
    print("Pobieranie listy ofert...")

    options = FirefoxOptions()
    options.add_argument("--headless") # żeby okienka nie było, można wyłączyć do testowania
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(10)  # czekamy aż strona się załaduje

    def scroll(start_height, scroll_amount, step=200):
        for height in range(start_height + step, start_height + scroll_amount + step, step):
            driver.execute_script(f"window.scrollTo(0, {height});")
            time.sleep(0.2)

    offers_urls = set()

    expected_height = 0
    while 1:
        scroll(start_height=expected_height, scroll_amount=1000)
        expected_height += 1000

        # dodajemy do offers
        link_elements = driver.find_elements(By.XPATH, "//div[@data-test-id='virtuoso-item-list']/div/div/a")
        for link_element in link_elements:
            offers_urls.add(link_element.get_attribute("href"))

        # jak zjedzie o mniej niż chcieliśmy to znaczy że zjechaliśmy do końca
        if driver.execute_script("return document.body.scrollHeight") < expected_height:
            break

    open("offers_urls.txt", "w").write("\n".join(offers_urls))

    driver.close()

def main():
    args = sys.argv

    URL = args[1]
    OUTPUT_FILE = args[2]

    # # do testowania
    # URL = "https://justjoin.it/job-offers/all-locations/data"
    # OUTPUT_FILE = "offers_urls.txt"

    scrape_offers_urls(URL, OUTPUT_FILE)

if "__main__" == __name__:
    main()