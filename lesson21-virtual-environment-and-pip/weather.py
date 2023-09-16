import requests
from dotenv import load_dotenv  # Help us get the environment variable
import os
from pprint import pprint

# Parse a .env file and then load all the variables found as environment variables.
load_dotenv()


def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')

    city = 'kansas city'
    # city = input('\nPlease enter a city name:\n')
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"

    weather_data = requests.get(request_url).json()
    pprint(weather_data)  # Test

    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nThe temp is {weather_data["main"]["temp"]}')
    print(
        f'\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.')


if __name__ == '__main__':
    get_current_weather()
