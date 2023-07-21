import requests
from dotenv import load_dotenv
from dataclasses import dataclass
import os

load_dotenv()
api_key = os.getenv('API_KEY')

# define class object

@dataclass
class WeatherData:
    pass



def get_lat_lon(city_name, state_code, country_code, api_keys):
    resp = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_keys}').json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon


def get_current_weather(lat, lon, api_keys):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_keys}').json()
    print(resp)


if __name__ == '__main__':
    lat, lon = get_lat_lon('Toronto', 'ON', 'Canada', api_key)
    get_current_weather(lat, lon, api_key)
