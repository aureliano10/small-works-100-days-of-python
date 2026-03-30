import requests
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()

USERNAME = "aureliano"
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint, json= parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name" : "Programming Graph",
    "unit" : "minutes",
    "type" : "int",
    "color" : "shibafu",
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# requests.post(url= graph_endpoint, json= graph_params, headers= headers)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today =datetime.now()

pixel_parameters = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "160",

}

# response = requests.post(url= pixel_endpoint, json= pixel_parameters, headers= headers)
# print(response)

pixel_update_parameters = {
    "quantity" : "160",
}

# response = requests.put(url= f"{pixel_endpoint}/{pixel_parameters["date"]}", json= pixel_update_parameters, headers= headers)
# print(response)

delete_pixel_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url= delete_pixel_url, headers= headers)
print(response.text)