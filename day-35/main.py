import requests


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "7b23a84e98f9cd37635be245ee371a18"

params = {
    "lat": 41.881832,
    "lon": -87.623177,
    "appid": API_KEY,
}

response = requests.get(OWM_ENDPOINT, params=params)
response.raise_for_status()
data = response.json()
five_day_forecast = data["list"]
print(five_day_forecast)