import requests


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "7b23a84e98f9cd37635be245ee371a18"

params = {
    "lat": 41.881832,
    "lon": -87.623177,
    "cnt": 4,
    "appid": API_KEY,
}

response = requests.get(OWM_ENDPOINT, params=params)
response.raise_for_status()
data = response.json()
five_day_forecast = data

will_rain = False

for forecast in five_day_forecast['list']:
    weather_id = forecast["weather"][0]["id"]
    
    if int(weather_id) < 700:
        will_rain = True
        
if will_rain:
    print("Bring an unbrella")
else:
    print("All Clear")