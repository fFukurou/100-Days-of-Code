#PriceCheck Project

import smtplib
import requests
from bs4 import BeautifulSoup
from personal_info import *
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()


url = "https://www.amazon.com/ASUS-Gaming-GeForce-Graphics-DisplayPort/dp/B0C7JYX6LN/ref=sr_1_1?dib=eyJ2IjoiMSJ9.7FjxgMhjTX_jg74IFb8Zh-qmRLoUe2tbNZL9OVaxXW-IBRwVgPKQk2AC1qSvnDpHGrYB54e3ZFdaq-LPJd5JmaRcv4AYHAZlA2hm59TybnXTT8TyxOPH8HZKaPgfGZ_-jWXJKnizDGvlfJ5LlpI4MiZjYV1xEAZ6kaaCA6surp2yL_AOsrMQNtRBWwh11BDzaCHR7h20Zfy_x5pV9Qm_s9QeeoPkpAaS1GZwmERmaBE.3whZI1YQfwFbBTGL9m76Mwhyv4hiLPrcoaDpUNZYSfs&dib_tag=se&keywords=rtx%2B4090&qid=1721912779&sr=8-1&th=1"

web_page = requests.get(url, headers={"Accept-Language":"en-US", "User-Agent":os.environ["USER_AGENT"]}).text

target_price = 1900

soup = BeautifulSoup(web_page, "html.parser")
price_html = soup.find(name="span", class_="aok-offscreen").getText() #type: ignore
price = round(float(price_html.replace("$", "").replace(",", "").strip()), 2)

product_name = soup.find(name="span", id="productTitle").getText().strip() #type: ignore


def send_email():
    with smtplib.SMTP(SMTP_TYPE) as connection:
        connection.starttls()
        connection.login(user=os.environ['MY_EMAIL'], password=os.environ['APP_PASSWORD'])
        connection.sendmail(from_addr=os.environ['MY_EMAIL'], to_addrs=os.environ['TARGET_EMAIL'], msg=f"Subject:Amazon Price Alert\n\n{product_name} \nis now ${price}\n{url}".encode("utf-8"))
        
if price < target_price:
    send_email()

