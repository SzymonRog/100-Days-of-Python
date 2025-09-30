from datetime import datetime
import dotenv
import requests
import os

dotenv.load_dotenv()
API_KEY = os.getenv("NUTRITIONIX_API_KEY")
APP_ID = os.getenv("NUTRITIONIX_APP_ID")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = "https://api.sheety.co/43bf237a6f3477c1249d373d9f9d9bf4/myWorkoutsPython/workouts"

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

user_input = input("Tell me what exercise you did: ")

data = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 56,
    "height_cm": 172,
    "age": 16
}

response = requests.post(NUTRITIONIX_URL, headers=nutritionix_headers, json=data)
response.raise_for_status()

new_date = datetime.now().strftime("%d/%m/%Y")
new_time = datetime.now().strftime("%X")

total_calories = 0

for exercise in response.json()["exercises"]:
    name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    total_calories += calories

    body = {
        "workout": {
            "date": new_date,
            "time": new_time,
            "exercise": name,
            "duration": duration,
            "calories": calories
        }
    }

    sheety_response = requests.post(SHEETY_URL, json=body, headers=sheety_headers)
    sheety_response.raise_for_status()
    print(f"{name}: {duration} minutes, {calories} calories")

print(f"Total calories burned: {round(total_calories,1)}")
