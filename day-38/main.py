import requests
import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

GENDER = "male"
WEIGHT_KG = 170
HEIGHT_CM = 178
AGE = 31

APP_ID =  os.environ.get("APP_ID")
NUTRITION_API_KEY = os.environ.get("NUTRITION_API_KEY")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": NUTRITION_API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url=exercise_endpoint,  headers=headers, json=parameters)
result = response.json()

print(f"Nutritionix API call: \n {result} \n")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

GOOGLE_SHEET_NAME = "workouts"

for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


    sheet_response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_inputs,
        auth=(
            SHEETY_USERNAME,
            SHEETY_PASSWORD,
        )
    )

    print(f"Sheety Response: \n {sheet_response.text}")


