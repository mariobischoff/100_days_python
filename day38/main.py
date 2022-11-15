from os import environ
import gspread
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"


def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list) + 1)


gc = gspread.oauth()
sh = gc.open("My Workouts")
worksheet = sh.sheet1

headers = {
    "x-app-id": environ.get("NUTRITIONIX_ID"),
    "x-app-key": environ.get("NUTRITIONIX_KEY"),
}

q = input("Tell me what exercises you did: ").lower()

body = {
    "query": q,
    "gender": "male",
    "weight_kg": 63.5,
    "height_cm": 170.64,
    "age": 29,
}

r = requests.post(NUTRITIONIX_URL, headers=headers, json=body)
r.raise_for_status()
data = r.json()

now = datetime.now()
date_now = now.strftime("%d/%m/%Y")
time_now = now.strftime("%H:%H:%S")

for data in data["exercises"]:
    duration = data["duration_min"]
    calories = data["nf_calories"]
    name = data["name"]
    next_row = next_available_row(worksheet)
    cell_list = worksheet.range(f"A{next_row}:E{next_row}")
    cell_values = [date_now, time_now, name, duration, calories]

    for i, val in enumerate(cell_values):
        cell_list[i].value = val

    worksheet.update_cells(cell_list)
