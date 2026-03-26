import requests
from dotenv import load_dotenv
import os
from  twilio.rest  import  Client
load_dotenv()

account_sid  = os.environ.get("TWILIO_ACCOUNT_SID")
# token_autenticacion  =  "9553b5c4ddae1d307119ae2e27686a18"
token_autenticacion  = os.environ.get("TWILIO_TOKEN_AUTH")

client  =  Client(account_sid, token_autenticacion)

API_KEY = "9282f55ce6afacda94fb8672e150861b"

parameters = {
    "lat" : 43.653225,
    "lon" : -79.383186,
    "appid" : API_KEY,
    "cnt" : 4,

}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params= parameters)
response.raise_for_status()
data = response.json()

def check_rain():
    for weather in data["list"]:
        if weather["weather"][0]["id"] < 700:
            return True
    return False

print(check_rain())
if check_rain():
    message = client.messages.create(
        body="Hoy va a llover, usa paraguas!!☔",
        from_="+14786063927",
        to="+543533686671",
    )
    print(message.sid)

# print(["traer paraguas" if weather["weather"][0]["id"] < 700 else "no hace falta paraguas" for weather in data["list"]])