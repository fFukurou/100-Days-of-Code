import smtplib
from personal_info import *


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_password)
    connection.sendmail(from_addr=my_email, to_addrs=target_email, msg="Subject:Testing\n\nTesting my email sender bruh")

