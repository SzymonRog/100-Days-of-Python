import requests
import os
from dotenv import load_dotenv
from datetime import *


load_dotenv()

client_id = os.getenv("AMADEUS_API_KEY")
client_secret = os.getenv("AMADEUS_SECRET")

token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
token_response = requests.post(
    token_url,
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    data={
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
)
token_response.raise_for_status()
access_token = token_response.json()["access_token"]
print(access_token)




amadeus_url = "https://test.api.amadeus.com/v1/shopping/flight-offers"
sheety_url = "https://api.sheety.co/43bf237a6f3477c1249d373d9f9d9bf4/flightDealsPython/prices"

amadeus_headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(sheety_url)
response.raise_for_status()


data = response.json()["prices"]

from_time = datetime.now()
to_time = from_time + timedelta(days=332)

deal_found = []
for row in data:
    print(f"Searching flight deal for: {row['iataCode']}")
    query = {
        "originLocationCode": "WRO",
        "destinationLocationCode": row["iataCode"],
        "departureDate": from_time.strftime("%Y-%m-%d"),
        "returnDate": to_time.strftime("%Y-%m-%d"),
        "adults": 1,
        "nonStop": "true",
        "currencyCode": "USD",
        "max": "10",
    }

    response = requests.get(url=amadeus_url, params=query, headers=amadeus_headers)
    response.raise_for_status()

    flight_data = response.json()
    if flight_data["meta"]["count"] > 0:
        for offer in flight_data["data"]:
            deal_found.append(offer)


print(deal_found)



