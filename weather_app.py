import requests
from pprint import pprint

API_Key = 'masukkan_api_key_anda_disini'
city = input("Masukkan nama kota: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

weather_data = requests.get(base_url).json()
pprint(weather_data)
