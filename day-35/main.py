import requests
from os import environ
from dotenv import load_dotenv
from twilio.rest import Client 

load_dotenv()  

OWM_API = environ.get("OWM_API_KEY")
TWILIO_API = environ.get("TWILIO_API_KEY")
TWILIO_SID = environ.get("TWILIO_SID_KEY")


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"


params = {
    "lat": 41.881832,
    "lon": -87.623177,
    "cnt": 4,
    "appid": OWM_API,
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
    client = Client(TWILIO_SID, TWILIO_API)
    message = client.messages.create(
        body="☔️IT'S GON RAIN!☔️",
        from_="+18885998708",
        to="+16302012552"
    )
    print(message.status)
else:
    client = Client(TWILIO_SID, TWILIO_API)
    message = client.messages.create(
        body="☀️Sunny ma boi!☀️",
        from_="+18885998708",
        to="+16302012552"
    )
    print(message.status)