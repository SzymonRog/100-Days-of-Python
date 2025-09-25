import os
import dotenv
import requests
from twilio.rest import Client   # <-- poprawka tutaj

dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
LON = float(os.getenv("LON"))
LAT = float(os.getenv("LAT"))
Client_number = os.getenv("CLIENT_PHONE")
User_number = os.getenv("USER_PHONE")

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

client = Client(account_sid, auth_token)

params = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4,
    "units": "metric"
}

response = requests.get(url=OWM_Endpoint, params=params)
response.raise_for_status()
data = response.json()
forecasts = data["list"]

is_it_going_to_rain = any(int(forecast["weather"][0]["id"]) < 700 for forecast in forecasts)

for forecast in forecasts:
    print(forecast["weather"][0]["id"])

if is_it_going_to_rain:
    print("Bring an umbrella")
    message = client.messages.create(
        to=User_number,
        from_=Client_number,
        body="Take umbrella with you!! It's going to rain today"
    )
    print(message.status)
