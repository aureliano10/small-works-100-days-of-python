import requests
from datetime import datetime

MY_LAT = -31.870001
MY_LONG = -62.720089

#requests se utiliza para hacer llamados a la API
#
# #METODO para obtener los datos
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (latitude, longitude)
# print(iss_position)

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(f"sunrise: {sunrise}, sunset: {sunset}")

time_now = datetime.now()
print(time_now)

