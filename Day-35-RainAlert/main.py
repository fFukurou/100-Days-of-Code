#Rain Alert Project
#CAUTION !!! Running this file will subtract dollars from the Twilio free trial account... IF it is raining at the LAT and LNG provided.

import smtplib
import requests
from personal_info import *
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

LAT = 42.525860
LNG = -71.760132

weather_params = {
    "lat": LAT,
    "lon": LNG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

def check_weather():
    for snapshot in weather_data["list"]:
        for weather in snapshot["weather"]:
            if weather["id"] < 700:
                return True

if check_weather():
    client = Client(account_sid, auth_token)
    # message = client.messages.create(body="You're gonna need an umbrella...", from_=twilio_number, to=my_number) #SMS
    message = client.messages.create(from_=f"whatsapp:{twilio_whatsapp_number}", body="It's going to rain today. Remember to bring an umbrella 🌂.",to=f"whatsapp:{my_number}") # WhatsApp

print(message.status)

