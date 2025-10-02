import requests


class UserMenager:
    def __init__(self):
        self.sheety_url = "https://api.sheety.co/43bf237a6f3477c1249d373d9f9d9bf4/flightDealsPython/users"
        self.users = []


        self.fetch_users()



    def fetch_users(self):
        response = requests.get(self.sheety_url)
        response.raise_for_status()
        data = response.json()["users"]
        self.users = [
            {
            "first_name": user["whatIsYourFirstName?"],
            "last_name": user["whatIsYourLastName?"],
            "email": user["whatIsYourEmail?"],
            } for user in data
        ]
        return self.users

