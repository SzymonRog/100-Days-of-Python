import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()


class FlightData:
    """Class responsible for structuring and fetching flight data."""

    def __init__(self):
        self.client_id = os.getenv("AMADEUS_API_KEY")
        self.client_secret = os.getenv("AMADEUS_SECRET")
        self.access_token = None
        self.amadeus_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.sheety_url = "https://api.sheety.co/43bf237a6f3477c1249d373d9f9d9bf4/flightDealsPython/prices"

        # Authenticate on initialization
        self._authenticate()

    def _authenticate(self):
        """Authenticate with Amadeus API and store access token."""
        token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"

        token_response = requests.post(
            token_url,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret
            }
        )
        token_response.raise_for_status()
        self.access_token = token_response.json()["access_token"]
        print(f"Authentication successful. Token: {self.access_token}")

    def _get_amadeus_headers(self):
        """Return headers for Amadeus API requests."""
        return {"Authorization": f"Bearer {self.access_token}"}

    def get_destination_codes(self):
        """Fetch destination IATA codes from Sheety API."""
        response = requests.get(self.sheety_url)
        response.raise_for_status()
        return response.json()["prices"]

    def search_flights(self, destination_code, origin_code="WAW", days_from_now=7, days_until=14, max_price=1):
        """
        Search for flight offers to a specific destination.

        Args:
            destination_code: IATA code of destination
            origin_code: IATA code of origin (default: WAW)
            days_from_now: Days from now for departure (default: 0)
            days_until: Days from now for return (default: 7)

        Returns:
            List of flight offers
        """
        from_time = datetime.now() + timedelta(days=days_from_now)
        to_time = datetime.now() + timedelta(days=days_until)

        query = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "currencyCode": "PLN",
            "maxPrice": max_price,
            "max": "10",
        }

        print(f"Searching flight deals for: {destination_code}")

        response = requests.get(
            url=self.amadeus_url,
            params=query,
            headers=self._get_amadeus_headers()
        )
        response.raise_for_status()

        flight_data = response.json()

        print(f"Found {flight_data['meta']['count']} offers.")

        if flight_data["meta"]["count"] > 0:
            return flight_data["data"]
        return []

    def find_all_deals(self, origin_code="WAW", days_from_now=7, days_until=14):
        """
        Search for flight deals to all destinations from Sheety.

        Args:
            origin_code: IATA code of origin (default: WAW)
            days_from_now: Days from now for departure (default: 0)
            days_until: Days from now for return (default: 332)

        Returns:
            List of all flight offers found
        """
        destinations = self.get_destination_codes()
        all_deals = []

        for destination in destinations:
            iata_code = destination["iataCode"]
            offers = self.search_flights(
                destination_code=iata_code,
                origin_code=origin_code,
                days_from_now=days_from_now,
                days_until=days_until,
                max_price=int(destination["lowestPrice"]),
            )
            all_deals.extend(offers)

        print(f"Found {len(all_deals)} total deals.")
        print(all_deals)
        return all_deals