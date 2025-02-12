from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
import time

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()