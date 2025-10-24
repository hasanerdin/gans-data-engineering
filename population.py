import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime # to get today's date

from utils import fetch_data_from_sql, store_data_to_sql

def retrieve_and_send_data():
  cities_df = fetch_data_from_sql("cities")
  population_df = fetch_population_data(cities_df)
  store_data_to_sql("populations", population_df)
  return "Data has been updated"

def fetch_population_data(cities: pd.DataFrame):
    today = datetime.today().strftime("%d.%m.%Y")

    population_data = []
    for _, city in cities.iterrows():
        city_name = city["city"]

        url = f"https://www.wikipedia.org/wiki/{city_name}"
        headers = {'User-Agent': 'Chrome/134.0.0.0'}

        response = requests.get(url, headers=headers)
        city_soup = BeautifulSoup(response.content, 'html.parser')

        # extract the relevant information
        city_population = city_soup.find(string="Population").find_next("td").get_text()
        city_population_clean = int(city_population.replace(",", ""))

        # keep track of data per city
        population_data.append({"city_id": city["city_id"],
                        "Population": city_population_clean,
                        "Timestamp_Population": pd.to_datetime(today)
                        })

    return pd.DataFrame(population_data)

retrieve_and_send_data()