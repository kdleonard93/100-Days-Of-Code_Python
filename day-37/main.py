import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

PIXELA_SECRET = os.environ.get("PIXELA_SECRET")
USERNAME = "kdleo"
DATETIME = datetime.datetime.now()
GRAPH_ID = "graph1"



if not PIXELA_SECRET:
    raise ValueError("PIXELA_SECRET is not set in the .env file.")

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
post_endpoint =  f"{graph_endpoint}/{GRAPH_ID}"
put_endpoint = f"{post_endpoint}/20250127"

user_params = {
    "token": PIXELA_SECRET,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_params = {
    "id": "graph1",
    "name": "meditation-graph",
    "unit": "minutes",
    "type": "int",
    "color": "momiji",
}

post_params = {
    "date": DATETIME.strftime("%Y%m%d"),
    "quantity": "3000",
}

put_params = {
    "quantity": "1000"
}

headers = {
    "X-USER-TOKEN": PIXELA_SECRET
}

response = requests.post(url=pixela_endpoint, json=user_params)
graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
post_response = requests.post(url=post_endpoint, json=post_params, headers=headers)
put_response = requests.put(url=put_endpoint, json=put_params, headers=headers)
print(response.text)
print(graph_response.text)
print(post_response.text)
print(put_response.text)

