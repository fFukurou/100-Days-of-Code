# Birthday Sender Project
import datetime as dt
import pandas as pd
import random
import smtplib
import sys
from personal_info import *

# -------------------- GETTING TODAY'S DATE --------------------- #

today_date = dt.datetime.now()
today = (today_date.month, today_date.day)


# -------------------- READING FROM CSV FILE --------------------- #

dataframe = pd.read_csv("Day-32/birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in dataframe.iterrows()}

# -------------------- COMPARING DATES / GENERATING LETTER --------------------- #

if today in birthdays_dict:
    letter_nmb = random.randint(1, 3)
    with open(f"Day-32/letter_templates/letter_{letter_nmb}.txt", "r") as file:
        letter = file.read()
        formatted_letter = letter.replace("[NAME]", f"{birthdays_dict[today]["name"]}")


# -------------------- SENDING LETTER --------------------- #

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_password)
    connection.sendmail(from_addr=my_email, to_addrs=birthdays_dict[today]["email"], msg=f"Subject:Happy Birthday!\n\n{formatted_letter}")


