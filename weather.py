import requests
from dotenv import load_dotenv

import os

load_dotenv()
api_key = os.getenv('API_KEY')


def get_lat_lon(city_name, state_code, country_code, api_keys):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_keys}')
    print(resp)


get_lat_lon('Toronto', 'ON', 'Canada', api_key)
