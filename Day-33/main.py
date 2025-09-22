import time
import requests
from datetime import datetime
import smtplib

MY_EMAIL = "YOUR_EMAIL"
MY_PASSWORD = "YOUR_PASSWORD"
MY_TEST_EMAIL = "YOUR_EMAIL"
MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude


def is_iss_overhead():
    """Check if the ISS is overhead (+/- 5 degrees)."""
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=10)
        response.raise_for_status()
        data = response.json()
        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and \
            (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)
    except Exception as e:
        print(f"Error checking ISS position: {e}")
        return False


def is_it_dark():
    """Check if it's currently dark at your location."""
    try:
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, timeout=10)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        time_now = datetime.utcnow().hour  # Use UTC to match the API

        return time_now >= sunset or time_now <= sunrise
    except Exception as e:
        print(f"Error checking light condition: {e}")
        return False


def send_email():
    """Send an email notification."""
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # Change if you're not using Gmail
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_TEST_EMAIL,
                msg="Subject:Look up👆\n\nThe ISS is above you in the sky!"
            )
        print("Email sent!")
    except Exception as e:
        print(f"Error sending email: {e}")


# MAIN LOOP
while True:
    if is_iss_overhead() and is_it_dark():
        send_email()
        break  # Exit after sending email
    time.sleep(60)
