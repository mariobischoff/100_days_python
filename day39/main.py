from dotenv import load_dotenv

load_dotenv()
from flight_search import FlightSearch
from data_manager import DataManager


data_manager = DataManager()

# data_manager.fill_iata_code()

fs = FlightSearch()
fs.cheapest_flight()
