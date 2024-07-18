#Habit Tracker Project
from personal_info import *
import requests
from datetime import datetime

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
     "notMinor": "yes",
}

pixela_endpoint = "https://pixe.la/v1/users"


# Create User
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "hours",
    "type": "float",
    "color": 'ajisai',
    

}

# Create Graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
formatted_today = today.strftime("%Y%m%d")

yesterday = datetime(year=2024, month=7, day=17)
formatted_yesterday = yesterday.strftime("%Y%m%d")

point_config = {
    "date": formatted_yesterday,
    "quantity": "3",
}

update_config = {
    "quantity": "4",
}

# Create Pixel
response = requests.post(url=f"{graph_endpoint}/{graph_config['id']}", json=point_config, headers=headers)
print(response.text)

#Update Pixel
# response = requests.put(url=f"{graph_endpoint}/{graph_config['id']}/{formatted_yesterday}", json=update_config, headers=headers)
# print(response.text)

#Delete Pixel
# response = requests.delete(url=f"{graph_endpoint}/{graph_config['id']}/{formatted_yesterday}", headers=headers)
# print(response.text)
