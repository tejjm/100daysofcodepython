import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from pathlib import Path
load_dotenv()
def send_mail(message):
    EMAIL = os.getenv("SENDER_EMAIL")
    PASSWORD = os.getenv("SENDER_PASSWORD")
    msg = EmailMessage()
    msg["From"] = EMAIL
    msg["To"] = "johnbeenrecruiting@gmail.com"
    msg["Subject"] = "Price Reduction"
    msg.set_content(message)
    with smtplib.SMTP("smtp.gmail.com",587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL,PASSWORD)
        smtp.send_message(msg)

