import requests
import os
from dotenv import load_dotenv
import datetime


load_dotenv()

GENDER = "male"
WEIGHT_KG = 170
HEIGHT_CM = 178
AGE = 31

APP_ID =  os.environ.get("APP_ID")
NUTRITION_API_KEY = os.environ.get("NUTRITION_API_KEY")
SHEETY_API = os.environ.get("SHEETY_API")

workout_slug = "myWorkouts/workouts"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{SHEETY_API}/{workout_slug}"

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "X-APP-ID": APP_ID,
    "X-APP-KEY": NUTRITION_API_KEY
}


response = requests.post(url=exercise_endpoint,  headers=headers, json=parameters)
result = response.json()

print(result)

