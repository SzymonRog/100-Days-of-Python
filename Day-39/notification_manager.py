from twilio.rest import Client
import smtplib
from email.message import EmailMessage

import os
from datetime import *

class NotificationManager:
    def __init__(self):
        self.client_number = os.getenv("CLIENT_PHONE")
        self.client_email = os.getenv("CLIENT_EMAIL")
        self.user_number = os.getenv("USER_PHONE")
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")

        self.client = Client(self.account_sid, self.twilio_auth_token)

        self.smtp_host = "smtp.gmail.com"
        self.smtp_port = 587
        self.username = os.getenv("GMAIL_USERNAME")
        self.password = os.getenv("GMAIL_PASSWORD")


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
        # self.send_sms(message)
        return message

    def send_emails(self, user_data,data):
        for user in user_data:
            msg = EmailMessage()
            msg["Subject"] = "Flight - Low price alert!"
            msg["From"] = self.client_email
            msg["To"] = user["email"]
            msg.set_content(self.generate_message(data))

        with smtplib.SMTP(self.smtp_host, self.smtp_port) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(self.username, self.password)
            smtp.send_message(msg)



    def send_sms(self, message):
        response_message = self.client.messages.create(
            to=self.user_number,
            from_=self.client_number,
            body=message,
        )



