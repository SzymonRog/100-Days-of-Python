import pandas as pd
import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from project import Project

df = pd.DataFrame(columns=[
    'project_id', 'project_name', 'project_type', 'total_value',
    'cofinancing_value', 'country', 'regions',
    'beneficiary_name', 'currency'
])
current_index = 1

df.to_csv('eu_projects.csv', index=False)

categories_dict = {
    104: 'transport',
    105: 'administration',
    106: 'research and study',
    107: 'security',
    108: 'power engineering',
    109: 'cultural',
    110: 'environmental',
    111: 'work and social development',
    112: 'revitalization',
    113: 'development of the corporations',
    114: 'telecommunication and e-commerce',
    115: 'tourism',
    116: 'international cooperation',
    527: 'education'

}


driver = webdriver.Chrome()
driver.get("https://mapadotacji.gov.pl/projekty/?search-s=&search-voivodeship=128&search-county=&search-fund=&search-program=&search-number-name-activity=&search-beneficiary=&search-title-of-project=&search-theme=&search-years=29398")

time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

def find_and_format_project_data(html_page):

    global current_index
    all_projects = []
    soup = BeautifulSoup(html_page, "html.parser")

    rows = soup.select("tbody tr")
    for row in rows:
        projects_names_tag = row.select_one("td.second h3")
        beneficiary_name_tag = row.find(name="td", attrs={"style": "word-break:break-all;"})
        total_val_tag = row.find("td", class_="price", attrs={"class": lambda x: x == "price"})
        cofinancing_val_tag = row.find(name="td", class_="light-blue price")

        region_td = cofinancing_val_tag.find_next_sibling("td") if cofinancing_val_tag else None
        regions = region_td.text.strip().split(",") if region_td else []

        category_links_tag = row.select('td.smaller a.cat')
        categories = []
        for link in category_links_tag:
            try:
                theme_number = int(link.get("href").split("theme=")[-1].split("&")[0])
                categories.append(categories_dict.get(theme_number, "Unknown"))
            except:
                categories.append("Unknown")


        project_name = projects_names_tag.text.strip()
        beneficiary_name = beneficiary_name_tag.text.strip()
        total_value = float(total_val_tag.text.strip().split("zł")[0].replace(" ", "").replace(",", ".")) if total_val_tag else 0
        cofinancing_value = float(cofinancing_val_tag.text.strip().split("zł")[0].replace(" ", "").replace(",", ".")) if cofinancing_val_tag else 0
        region = regions
        category = categories


        project = {
            'project_id': current_index,
            'project_name': project_name,
            'project_type': category,
            'total_value': total_value,
            'cofinancing_value': cofinancing_value,
            'regions': region,
            'beneficiary_name': beneficiary_name,
            'currency': 'PLN',
           'country': 'Poland'
        }

        all_projects.append(project)
        current_index += 1

    return all_projects



def overwrite_csv(projects):
    df = pd.read_csv("eu_projects.csv")

    # Dodanie nowych wierszy
    df = pd.concat([df, pd.DataFrame(projects)], ignore_index=True)

    # Zapis do CSV (nadpisanie istniejącego)
    df.to_csv("eu_projects.csv", index=False)

# projects_amount = int(soup.find(name="span", class_="find-amount").text.split()[0])
# for i in range(0, 5):

html = driver.page_source
projects = find_and_format_project_data(html)
overwrite_csv(projects)


    # driver.execute_script(f"window.scrollTo(0, {i*100});")
    # time.sleep(1)
