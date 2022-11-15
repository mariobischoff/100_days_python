import json
from urllib import response
import requests

from flight_search import FlightSearch


SHEETY_ENDPOINT = (
    "https://api.sheety.co/e05c0e83d065490fb9741c97e47a6800/flightPrices/prices"
)


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.locations = []
        self.load_data()
        self.flight_service = FlightSearch()

    def load_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        response.raise_for_status()
        self.locations = response.json()["prices"]
        # print(self.locations)

    def get_city(self):
        """Return all cities from Google Sheet Flight Prices"""
        cities = [location["city"] for location in self.locations]
        return cities

    def fill_iata_code(self):
        if not self.locations[0]["iataCode"]:
            for location in self.locations:
                code = self.flight_service.get_iata_code(location["city"])
                location["iataCode"] = code
                data = {"price": location}
                response = requests.put(
                    f"{SHEETY_ENDPOINT}/{location['id']}", json=data
                )
                response.raise_for_status()
