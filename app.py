import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file.
load_dotenv()

# Loads local endpoint for REST API.
api_url = os.environ.get("API_URL")

def fetch_weather(city):
  # Set parameters.
  params = {"city": city}

  # Make Request to REST API.
  try:
    response = requests.get(url=api_url, params=params)
    response_data = response.json()
    if len(response_data['data']) != 0:
      # Grab relevent data.
      weather = response_data['data'][0].get("weather", [])
      main = response_data['data'][0].get("main", {})
      wind = response_data['data'][0].get("wind", {})

      print(f"Weather in {city}:")
      if weather:
        print(f"\tCondition: {weather[0]['main']}")
        print(f"\tDescription: {weather[0]['description']}")
        if wind:
          print(f"\tWind Speed: {wind.get('speed', 0)}mph")
      if main:
        print("\nTemperature: ")
        print(f"\tHigh: {main['temp_max']}")
        print(f"\tLow: {main['temp_min']}")
        print(f"\tFeels like: {main['feels_like']}")
        print(f"\tCurrent: {main['temp']}F")
    else:
      # If there is an error, display it here.
      error_data = response.json()
      print(f"Failed to fetch weather data for {city}.\nStatus code: {error_data['status']}\nMessage: {error_data['message']}")
  except Exception as e:
    print("There was an unexpected event that accured. Check connection to REST API.")
    print(e)

# Runs function to continuously until specified other wise.
def main():
  while True:
    city = input("Enter a city name (or 'quit' to exit): ")
    if city.lower() == 'quit':
      break
    fetch_weather(city)

if __name__ == "__main__":
  main()