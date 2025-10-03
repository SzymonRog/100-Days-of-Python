from datetime import *
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

    def write_email(self):
        email = input("Enter your email: ")
        confirm_email = input("Confirm your email: ")

        while email != confirm_email:
            print("Emails do not match!")
            email = input("Enter your email: ")
            confirm_email = input("Confirm your email: ")

        return email

    def add_user(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = self.write_email()
        timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        new_user = {
            "timestamp": timestamp,
            "whatIsYourFirstName?": first_name,
            "whatIsYourLastName?": last_name,
            "whatIsYourEmail?": email
        }


        response = requests.post(self.sheety_url, json={"user": new_user})
        response.raise_for_status()
        print("User added successfully!")

