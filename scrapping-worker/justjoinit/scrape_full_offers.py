from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import sys
import os
import time
from tqdm import tqdm

def scrape_full_offers(input_path, output_dir):
    options = FirefoxOptions()
    options.add_argument("--headless") # żeby okienka nie było, można wyłączyć do testowania
    driver = webdriver.Firefox(options=options)
    time.sleep(10)  # czekamy aż strona się załaduje

    offers_urls = set(open(input_path).read().strip().split())

    def scrape_full_offer_info(offer_url):
        driver.get(offer_url)
        time.sleep(1)
        return driver.find_element(By.XPATH, "//body/div[2]/div/div/div/div[2]/div[2]").get_attribute("innerHTML")

    print("Pobieranie ofert...")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    old_files = set(os.listdir(output_dir))
    for iter_url in tqdm(offers_urls):
        file_name = f"{output_dir}/{iter_url.split('/')[-1]}.html"
        if file_name not in old_files:
            file = open(file_name, "w", encoding="utf-8")
            file.write(f"<html>\n{scrape_full_offer_info(iter_url)}\n</html>")
            file.close()

    driver.close()

def main():
    args = sys.argv

    INPUT_PATH = args[1]
    OUTPUT_DIR = args[2]

    # # do testowania
    # INPUT_PATH = "./offers_urls.txt"
    # OUTPUT_DIR = "./offers"

    scrape_full_offers(INPUT_PATH, OUTPUT_DIR)

if "__main__" == __name__:
    main()