import requests
from datetime import datetime

parameters = {
    "lat":51.507351,
    "lng":-0.127758,
    "formatted":0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]

time_now = datetime.now().hour

print(time_now)
print(sunrise_hour)
print(sunset_hour)