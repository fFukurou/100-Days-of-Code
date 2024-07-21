import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from personal_info import *
from pprint import pprint


class DataManager:

    def __init__(self):
        self._user = SHEETY_USRERNAME
        self._password = SHEETY_PASSWORD
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        self.headers = {
            "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}",
            "Content-Type": "application/json"
        }
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        return self.destination_data

    # updating the Google Sheet with the IATA codes.
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                } 
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers,
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.headers)
        data = response.json()
        self.customer_data = data["users"]
        print(self.customer_data)
        return self.customer_data
    


headers = {
            "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}",
            "Content-Type": "application/json"
        }
