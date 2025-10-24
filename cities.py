import pandas as pd
import requests
from bs4 import BeautifulSoup
from lat_lon_parser import parse    # for decimal coordinates

from utils import store_data_to_sql

def retrieve_and_send_data(cities):
  cities_df = fetch_cities_data(cities)
  store_data_to_sql("cities", cities_df)
  return "Data has been updated"

def fetch_cities_data(cities):
  city_data = []
  for city in cities:
    url = f"https://www.wikipedia.org/wiki/{city}"
    headers = {'User-Agent': 'Chrome/134.0.0.0'}

    response = requests.get(url, headers=headers)
    city_soup = BeautifulSoup(response.content, 'html.parser')

    # extract the relevant information
    city_latitude = city_soup.find(class_="latitude").get_text()
    city_longitude = city_soup.find(class_="longitude").get_text()
    country = city_soup.find(class_="infobox-data").get_text()

    # keep track of data per city
    city_data.append({"City": city,
                    "Country": country,
                    "Latitude": parse(city_latitude), # latitude in decimal format
                    "Longitude": parse(city_longitude), # longitude in decimal format
                    })

  return pd.DataFrame(city_data)

cities = ["Berlin", "Hamburg", "Munich"]
retrieve_and_send_data(cities)