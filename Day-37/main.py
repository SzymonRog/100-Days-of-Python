import datetime

import requests
import dotenv
import os

dotenv.load_dotenv()
pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "szymonrogala"
GRAPH_ID = "graph1"

user_params = {
    "token": os.getenv("PIXELA_TOKEN"),
    "username": "szymonrogala",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=params)
# response.raise_for_status()
# print(response.text)

graph_params = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": os.getenv("PIXELA_TOKEN")
}

# response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs", json=graph_params,headers=headers)
# response.raise_for_status()
# print(response.text)
def ask_for_input():
    while True:
        try:
            quantity = float(input("How many Km did you run?: "))
        except ValueError:
            print("Please enter a number!")
            pass
        else:
            return str(quantity)

def ask_for_date():
    input_date = input("Enter a date (YYYYMMDD) or enter now to select current date: ").lower()
    if input_date == "now":
        return datetime.datetime.now().strftime("%Y%m%d")
    else:
        return input_date

chooice = input("What you want to do (create/update/delete): ").lower()


if chooice == "create":
    quantity = ask_for_input()
    date = datetime.datetime.now().strftime("%Y%m%d")

    create_pixel_params = {
        "date": date,
        "quantity": str(quantity)
    }

    response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}", json=create_pixel_params,
                             headers=headers)
    response.raise_for_status()
    print(response.text)
elif chooice == "update":
    date = ask_for_date()
    quantity = ask_for_input()

    update_pixel_params = {
        "quantity": str(quantity)
    }
    response = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}", json=update_pixel_params,
                            headers=headers)
    response.raise_for_status()
    print(response.text)

elif chooice == "delete":
    date = ask_for_date()

    response = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}", headers=headers)
    response.raise_for_status()
    print(response.text)







print(f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}")


