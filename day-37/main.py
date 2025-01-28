import requests
import os

PIXELA_SECRET = os.environ.get("PIXELA_SECRET")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_SECRET,
    "username": "kdleo",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)