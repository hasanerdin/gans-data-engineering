from flask import Request
import json
 
from weather import retrieve_and_send_data as fetch_weather
from flight import retrieve_and_send_data as fetch_flight

# Simulate request data
request_data = {}
request = Request.from_values(data=json.dumps(request_data))
 
# Call the function and print the response
weather_response = fetch_weather(request)
print(weather_response)

flight_response = fetch_flight(request)
print(flight_response)