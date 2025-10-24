import pandas as pd
import requests

from utils import fetch_data_from_sql, store_data_to_sql, RAPID_API_KEY

def retrieve_and_send_data():
    cities_df = fetch_data_from_sql("cities")
    airports_df = fetch_population_data(cities_df)
    city_airport_df = create_city_airport_df(cities_df, airports_df)

    store_data_to_sql("airports", airports_df)
    store_data_to_sql("cities_airport", city_airport_df)
    
    return "Data has been updated"

def fetch_population_data(cities: pd.DataFrame):
    # API headers
    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
    }

    querystring = {"withFlightInfoOnly": "true"}

    # DataFrame to store results
    all_airports = []
    for _, city in cities.iterrows():
        lat, lon = city[["latitude", "longitude"]]

        # Construct the URL with the latitude and longitude
        url = f"https://aerodatabox.p.rapidapi.com/airports/search/location/{lat}/{lon}/km/50/16"

        # Make the API request
        response = requests.get(url, headers=headers, params=querystring)
        airports_data = response.json()

        for item in airports_data.get("items", []):
            airport_item = {
                "airport_icao": item["icao"],
                "airport_name": item["name"],
                "city": item["municipalityName"]
            }

            all_airports.append(airport_item)

    return pd.DataFrame(all_airports)

def create_city_airport_df(cities_df, airports_df):
    cities_airports_df = cities_df.merge(airports_df, on="city", how="inner")
    return cities_airports_df.loc[:, ["city_id", "airport_icao"]]
    

retrieve_and_send_data()