import os
import re
import sys
import json

from AdvancedHTMLParser import IndexedAdvancedHTMLParser,AdvancedTag

def parse_offers(input_dir, output_file):
    offers_list = []

    for offer_path in os.listdir(input_dir):
        print(offer_path)

        parser = IndexedAdvancedHTMLParser()
        parser.parseFile(os.path.join(input_dir, offer_path))

        salary_element = parser.getElementsByXPath("//html/div[6]/div[1]/div[1]/div[1]/span[1]")
        if not salary_element:
            salary = "Undisclosed salary"
        else:
            salary = re.sub(r"<!--\s*-->", "", salary_element[0].textContent)

        offer = {
            "Details": {
                skill.getElementsByXPath("//div/div[2]/div[1]")[0].textContent: skill.getElementsByXPath("//div/div[2]/div[2]")[0].textContent
                for skill in parser.getElementsByXPath("//html/div[2]/div")
            },
            "Tech stack": {
                skill.getElementsByXPath("//div[1]/h4[1]")[0].textContent: skill.getElementsByXPath("//div[1]/span[1]")[0].textContent
                for skill in parser.getElementsByXPath("//html/div/div[1]/ul[1]/div")
            },
            "Salary": salary,
        }

        offers_list.append(offer)
    json.dump(offers_list, open(output_file, "w", encoding="utf-8"))

def main():
    args = sys.argv

    INPUT_DIR = args[1]
    OUTPUT_FILE = args[2]

    # do testowania
    # INPUT_DIR = "./offers"
    # OUTPUT_FILE = "./offers.json"

    parse_offers(INPUT_DIR, OUTPUT_FILE)

if "__main__" == __name__:
    main()