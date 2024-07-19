#Workout Tracker Project
from personal_info import *
import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = "54"
HEIGHT_CM = "175"
AGE = "20"


today = datetime.now()
formatted_today = today.strftime("%d/%m/%Y")
formatted_hour = today.strftime("%H:%M:%S")

exercise = input("What was your exercise today?")
# exercise = "ran 10 minutes and cycled for 30 minutes"


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": f"Bearer {TOKEN}"
}

params = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(exercise_endpoint, headers=headers, json=params)
data = response.json()

exercise_list = []
total_duration = 0
total_calories = 0

for exercise in data['exercises']:
    exercise_list.append(exercise['name'])
    total_duration += exercise["duration_min"]
    total_calories += exercise["nf_calories"]

formatted_exercises = ", ".join(exercise_list)

exercise_dict = {
    "workout": {
        "date": formatted_today,
        "time": formatted_hour,
        "exercise": formatted_exercises,
        "duration": total_duration,
        "calories": total_calories
    }
}


sheety_endpoint = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"


#Create a Row
response = requests.post(sheety_endpoint, json=exercise_dict)
print(response.json())

#Delete a Row
# row_to_be_deleted = 3
# response = requests.delete(f"{sheety_endpoint}/{row_to_be_deleted}")