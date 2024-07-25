import smtplib
import requests
from bs4 import BeautifulSoup
from personal_info import *
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()


url = "https://appbrewery.github.io/instant_pot/"

web_page = requests.get(url, headers={"Accept-Language":"en-US", "User-Agent":os.environ["USER_AGENT"]}).text

target_price = 100

soup = BeautifulSoup(web_page, "html.parser")
price_html = soup.find(name="span", class_="aok-offscreen").getText() #type: ignore
price = float(price_html.replace("$", ""))

product_name = soup.find(name="span", id="productTitle").getText().strip() #type: ignore


def send_email():
    with smtplib.SMTP(SMTP_TYPE) as connection:
        connection.starttls()
        connection.login(user=os.environ['MY_EMAIL'], password=os.environ['APP_PASSWORD'])
        connection.sendmail(from_addr=os.environ['MY_EMAIL'], to_addrs=os.environ['TARGET_EMAIL'], msg=f"Subject:Amazon Price Alert\n\n{product_name} \nis now ${price}\n{url}".encode("utf-8"))
        
if price < target_price:
    send_email()

