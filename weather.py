import requests
from dotenv import load_dotenv

import os

load_dotenv()
api_key = os.getenv('API_KEY')


def get_lat_lon(city_name, state_code, country_code, api_keys):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_keys}').json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon



print(get_lat_lon('Toronto', 'ON', 'Canada', api_key))
