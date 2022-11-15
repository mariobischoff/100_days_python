from time import sleep
import requests
from datetime import datetime
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

MY_LAT = -23.5506507
MY_LONG = -46.6333824


MY_EMAIL = os.getenv("DEV_EMAIL")
MY_PASSWORD = os.getenv("DEV_PASS")


def is_iss_overhead():
    """Return True if ISS lat and long <= 5º"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    reponse = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    reponse.raise_for_status()

    data = reponse.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise_hour = int(sunrise.split("T")[1].split(":")[0]) - 3
    sunset_hour = int(sunset.split("T")[1].split(":")[0]) - 3
    time_now = datetime.now()
    now_hour = time_now.hour
    if now_hour >= sunset_hour or now_hour <= sunrise_hour:
        return True


while True:
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        print(MY_EMAIL)
        print(MY_PASSWORD)
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )
    sleep(5*60)
