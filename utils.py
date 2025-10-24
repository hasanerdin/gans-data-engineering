import pandas as pd

RAPID_API_KEY = "YOUR_API_KEY"
WEATHER_API_KEY = "YOUR_API_KEY"

WEATHER_URL = "https://api.openweathermap.org/data/2.5/forecast"
GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"

def get_connection_string():
    schema = "YOUR_SCHEMA"
    host = "GCP_IP_ADDRESS"
    port = 3306
    user = "root"
    password = "YOUR_GCP_PASSWORD"

    con_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{schema}"
    return con_string 

def fetch_data_from_sql(table_name):
    return pd.read_sql(table_name, con=get_connection_string())

def store_data_to_sql(table_name, data):
    data.to_sql(table_name, 
                if_exists='append',
                con=get_connection_string(),
                index=False)