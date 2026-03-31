import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

basic = HTTPBasicAuth(os.environ.get("USER_AUTH_SHEETY"), os.environ.get("PASS_AUTH_SHEETY"))

headers = {
    "x-app-id": os.environ.get("ID_API_NUTRITION"),
    "x-app-key": os.environ.get("KEY_API_NUTRITION")
}

url_base_nutrition = "https://app.100daysofpython.dev"

parameters_post = {
    "query": input("que hiciste hoy?"),
    "gender": "male",
    "age": 21,
    "weight_kg": 93,
    "height_cm": 169,
}

response = requests.post(url=f"{url_base_nutrition}/v1/nutrition/natural/exercise",
                         headers= headers,
                         json= parameters_post
                         )
response.raise_for_status()
data = response.json()

# header_for_sheety ={
#     "Content-Type": "application/json"
# }

url_base_sheety = "https://api.sheety.co/e4e6df698ea802c3f100b18d0c993344/misEntrenamientos/workouts"

time = datetime.now()

parameters_sheety = {
    "workout": {
        "date": time.strftime("%d/%m/%Y"),
        "time": time.strftime("%H:%M:%S"),
        "exercise": data["exercises"][0]["name"].title(),
        "duration": data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"]
    }
}

response_sheety = requests.post(url= url_base_sheety,
                                headers= header_for_sheety,
                                json= parameters_sheety,
                                auth= basic
                                )
response_sheety.raise_for_status()
