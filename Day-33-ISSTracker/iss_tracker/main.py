# ISS Tracker Project

import requests
from datetime import datetime
import smtplib
from personal_info import *
import time

MY_LAT = -45
MY_LONG = 135

#Your position is within +10 or -10 degrees of the ISS position.

def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude <= MY_LAT+10 and iss_latitude >= MY_LAT-10:
        if iss_longitude <= MY_LONG+10 and iss_longitude >= MY_LONG-10:
            return True


def is_dark():
    parameters = {
    "lat": MY_LAT, 
    "lng": MY_LONG,
    "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now <= sunrise or time_now >= sunset:
        return True


while True:
    if is_iss_close() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_password)
            connection.sendmail(from_addr=my_email, to_addrs=target_email, msg=f"Subject:Look Up!\n\nISS Satellite is currently flying above you :O")
    time.sleep(30)

    


