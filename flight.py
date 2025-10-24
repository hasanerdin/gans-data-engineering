import functions_framework
import pandas as pd
import requests
from pytz import timezone
from datetime import datetime, timedelta

from utils import *

@functions_framework.http
def retrieve_and_send_data(request):
  airports_df = fetch_data_from_sql("airports")
  flights_df = fetch_flight_data(airports_df)
  store_data_to_sql("flights", flights_df)
  return "Data has been updated"

def fetch_flight_data(airports_df: pd.DataFrame):
    berlin_timezone = timezone('Europe/Berlin')
    today = datetime.now(berlin_timezone).date()
    tomorrow = (today + timedelta(days=1))

    all_flights = []
    for _, airport in airports_df.iterrows():
        times = [["00:00","11:59"],["12:00","23:59"]]
        icao = airport["airport_icao"]

        for time in times:
            url = f"https://aerodatabox.p.rapidapi.com/flights/airports/icao/{icao}/{tomorrow}T{time[0]}/{tomorrow}T{time[1]}"

            querystring = {"direction":"Arrival","withCancelled":"false"}

            headers = {
                "X-RapidAPI-Key": RAPID_API_KEY,
                "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
                }

            response = requests.request("GET", url, headers=headers, params=querystring)
            if response.status_code != 200:
                continue

            flights_data = response.json()

            for item in flights_data.get("arrivals", []):
                flight_item = {
                    "flight_number": item["number"],
                    "departure_icao": item["movement"]["airport"].get("icao", None),
                    "arrival_icao": icao,
                    "arrival_time": item["movement"]["scheduledTime"]["local"],
                    "data_retrieved_on": pd.to_datetime(today)
                }
            
                # fixing arrival_time
                flight_item["arrival_time"] = flight_item["arrival_time"].split("+")[0]

                all_flights.append(flight_item)

    return pd.DataFrame(all_flights)
