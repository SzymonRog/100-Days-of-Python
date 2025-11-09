import pandas as pd


df = pd.read_csv("eu_projects.csv", header=None)

# Dodanie nazw kolumn
df.columns = [
    'project_id', 'project_name', 'project_type', 'total_value',
    'cofinancing_value', 'regions', 'beneficiary_name', 'currency',
    'country', 'years'
]


df.to_csv("eu_projects.csv", index=False)