import time
import requests
from datetime import datetime
import smtplib

MY_EMAIL = "eichhornaureliano.gmz@gmail.com"
MY_PASSWORD = "fvdl xpfe nvlm usyz"

def send_mail(name, email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user= MY_EMAIL,
            password= MY_PASSWORD
        )
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs= email,
            msg=f"Subject: HI {name}!!\n\n"
                f"You should go outside"
        )


MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude



#Your position is within +5 or -5 degrees of the ISS position.
def is_up_to_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5):
        if (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
            return True

    return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def can_see_iss():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False




#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    if is_up_to_me() and can_see_iss():
        send_mail("Marucha", "eichhornaureliano@gmail.com")
        break
    time.sleep(60)


