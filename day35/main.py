import datetime
import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Pirassununga lat lon
MY_LAT = -21.99
MY_LON = -47.42

load_dotenv()

# OpenWeather
API_KEY = os.environ.get("API_KEY")
URL = "https://api.openweathermap.org/data/2.5/forecast"

# Twilio
account_sid = "AC3f8e079798995ac045cd4a62c8b52189"
auth_token = os.environ.get("AUTH_TOKEN")
phone_number = "+14195065772"

users_sub = {"+5519999630766": "Mario"}

params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(URL, params)
response.raise_for_status()
weather_data = response.json()["list"]

today = datetime.datetime.today()
today_weather = [weather_hour["weather"][0] \
    for weather_hour in weather_data \
        if int(weather_hour["dt_txt"].split(" ")[0].split("-")[2]) == today.day]

will_rain = False
for weather in today_weather:
    condition_code = weather["id"]
    if condition_code < 700:
        will_rain = True

if True:
    client = Client(account_sid, auth_token)
    for phone, name in users_sub.items():
        message = client.messages.create(
            body=f"Heyy {name}, pegue a capa de chuva ☔",
            from_=phone_number,
            to=phone
        )
        print(message.status)