import functions_framework
import pandas as pd
import requests
from pytz import timezone
from datetime import datetime

from utils import *

@functions_framework.http
def retrieve_and_send_data(request):
  cities_df = fetch_data_from_sql("cities")
  weather_df = fetch_weather_data(cities_df)
  store_data_to_sql("weathers", weather_df)
  return "Data has been updated"

def fetch_weather_data(cities_df):
  berlin_timezone = timezone('Europe/Berlin')
  retrieval_time = datetime.now(berlin_timezone).strftime("%Y-%m-%d %H:%M:%S")
  
  weather_items = []
  for _, city in cities_df.iterrows():
      latitude = city["latitude"]
      longitude = city["longitude"]
      city_id = city["city_id"]

      weather_params = {
         "lat": latitude,
         "lon": longitude,
         "appid": WEATHER_API_KEY,
         "units": "metric"
      }
      response = requests.get(WEATHER_URL, params=weather_params)
      weather_data = response.json()

      for item in weather_data["list"]:
          weather_item = {
              "city_id": city_id,
              "forecast_time": item.get("dt_txt"),
              "temperature": item["main"].get("temp"),
              "forecast": item["weather"][0].get("main"),
              "rain_in_last_3h": item.get("rain", {}).get("3h", 0),
              "wind_speed": item["wind"].get("speed"),
              "data_retrieved_at": retrieval_time
          }
          weather_items.append(weather_item)

  weather_df = pd.DataFrame(weather_items)
  weather_df["forecast_time"] = pd.to_datetime(weather_df["forecast_time"])
  weather_df["data_retrieved_at"] = pd.to_datetime(weather_df["data_retrieved_at"])

  return weather_df
