from datetime import datetime, timedelta
from os import environ
import requests


URL = "https://api.tequila.kiwi.com"
HEADER = {"apiKey": environ.get("TEQUILA_KEY")}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):

        pass

    def get_iata_code(self, city):
        params = {"term": city, "location_types": "city"}
        response = requests.get(f"{URL}/locations/query", params=params, headers=HEADER)
        response.raise_for_status()
        data = response.json()
        return data["locations"][0]["code"]

    def cheapest_flight(self):
        date_from = datetime.now()
        date_to = date_from + timedelta(6 * 30)

        date_from = date_from.strftime("%d/%m/%Y")
        date_to = date_to.strftime("%d/%m/%Y")

        params = {
            "fly_from": "LGA",
            "fly_to": "MIA",
            "date_from": "07/10/2022",
            "date_to": "02/12/2022",
        }
        HEADER["Accept-Encoding"] = "gzip"
        response = requests.get(f"{URL}/v2/search", params=params, headers=HEADER)
        response.raise_for_status()
        data = response.json()
        print(data)
