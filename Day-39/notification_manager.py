from twilio.rest import Client
import os
from datetime import *
class NotificationManager:
    def __init__(self):
        self.client_number = os.getenv("CLIENT_PHONE")
        self.user_number = os.getenv("USER_PHONE")
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")

        self.client = Client(self.account_sid, self.twilio_auth_token)


    def generate_message(self, data):
        date = data["date"].split("T")[0]
        until_date = data["until"].split("T")[0]

        message = (
            f"-Low price alert!\n"
            f"Only {data['price']} {data['currency']} to fly "
            f"from {data['from']} to {data['to']}, "
            f"on {date} until {until_date}."
        )

        print(message)
        self.send_sms(message)
        return message


    def send_sms(self, message):
        response_message = self.client.messages.create(
            to=self.user_number,
            from_=self.client_number,
            body=message,
        )

