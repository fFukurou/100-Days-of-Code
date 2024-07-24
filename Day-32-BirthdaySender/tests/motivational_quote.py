import datetime as dt
from personal_info import *
import pandas as pd
import random
import smtplib

quotes = []

now = dt.datetime.now()

if now.weekday() == 1:
    with open("Day-32-BirthdaySender/tests/quotes.txt", "r") as file:
        for line in file:
            quotes.append(line)

    chosen_quote = random.choice(quotes)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email, to_addrs=target_email, msg=f"Subject:Monday Motivation\n\n{chosen_quote}")


