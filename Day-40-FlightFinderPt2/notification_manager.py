import os
import smtplib
from twilio.rest import Client
from personal_info import *

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',
            body=message_body,
            to=f'whatsapp:{MY_NUMBER}'
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SMTP_MY_EMAIL, password=SMTP_APP_PASSWORD)
            for email in email_list:
                connection.sendmail(
                    from_addr=SMTP_MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )

