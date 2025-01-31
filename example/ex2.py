import requests
import pprint

lat = 43.0620958  # 삿포로 위도

lon = 141.3543763  # 삿포로 경도

API_KEY = '0f7f67c5ea1fd29d484b8582a76e36a2'  # API KEY

URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'

data = requests.get(URL).json()

pprint.pprint(data)