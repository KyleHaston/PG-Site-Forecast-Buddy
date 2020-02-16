# This takes in some HTML and a destination and sends an email
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import *
import credentials

import send_mail

def send_html_email_to_user(in_html, in_destination):
    smtp_server = 'smtp.gmail.com'
    sender = 'paraglidingSiteForecastBuddy@gmail.com'

    username = credentials.this_login
    password = credentials.this_password
    try:
        send_mail.send_mail(sender, in_destination, 'asdf', 'asdf', files=['output.html'], server=smtp_server, port=587, username=credentials.this_login, password=credentials.this_password)

    except:
        print('        ERROR: mail failed to: ' + in_destination)  # give an error message
