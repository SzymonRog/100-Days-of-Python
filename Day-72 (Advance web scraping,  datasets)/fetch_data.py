import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

current_index = 1
categories_dict = {104: 'transport', 105: 'administration', 106: 'research and study',
                   107: 'security', 108: 'power engineering', 109: 'cultural',
                   110: 'environmental', 111: 'work and social development', 112: 'revitalization',
                   113: 'development of the corporations', 114: 'telecommunication and e-commerce',
                   115: 'tourism', 116: 'international cooperation', 527: 'education'}

def find_and_format_project_data(html_page):
    global current_index
    soup = BeautifulSoup(html_page, "html.parser")
    projects_list = []

    for row in soup.select("tbody tr"):
        projects_names_tag = row.select_one("td.second h3")
        beneficiary_name_tag = row.find(name="td", attrs={"style": "word-break:break-all;"})
        total_val_tag = row.find("td", class_="price")
        cofinancing_val_tag = row.find("td", class_="light-blue price")

        region_td = cofinancing_val_tag.find_next_sibling("td") if cofinancing_val_tag else None
        regions = region_td.text.strip().split(",") if region_td else []

        category_links_tag = row.select('td.smaller a.cat')
        categories = []
        for link in category_links_tag:
            try:
                theme_number = int(link.get("href").split("theme=")[-1].split("&")[0])
                categories.append(categories_dict.get(theme_number, "Other"))
            except:
                categories.append("Other")

        project = {
            'project_id': current_index,
            'project_name': projects_names_tag.text.strip(),
            'project_type': categories if categories else ['Other'],
            'total_value': float(total_val_tag.text.strip().split("zł")[0].replace(" ", "").replace(",", ".")) if total_val_tag else 0,
            'cofinancing_value': float(cofinancing_val_tag.text.strip().split("zł")[0].replace(" ", "").replace(",", ".")) if cofinancing_val_tag else 0,
            'regions': regions,
            'beneficiary_name': beneficiary_name_tag.text.strip(),
            'currency': 'PLN',
            'country': 'Poland',
            'years':  '2014-2020'
        }

        projects_list.append(project)
        current_index += 1

    return projects_list


# zbieramy wszystkie projekty w jednej liście
all_projects = []
file_path = 'eu_projects.csv'
batch_size = 500
first_write = not os.path.exists(file_path)
for i in range(1,200):
    response = requests.get(f"https://mapadotacji.gov.pl/projekty/?search-years=526&page_no={i}")
    response.raise_for_status()
    html = response.text
    projects = find_and_format_project_data(html)
    all_projects.extend(projects)

    if i % batch_size == 0:
        df = pd.DataFrame(all_projects)
        df.to_csv(file_path, mode='a', index=False, header=first_write)
        all_projects = []  # czyścimy pamięć po zapisaniu
        first_write = False  # kolejne zapisy bez nagłówka

    # zapis pozostałych projektów po ostatnim batchu
if all_projects:
    df = pd.DataFrame(all_projects)
    df.to_csv(file_path, mode='a', index=False, header=first_write)
