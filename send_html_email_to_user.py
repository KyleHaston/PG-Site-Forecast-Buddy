# This takes in some HTML and a destination and sends an email
import sys
from email.mime.text import MIMEText
from smtplib import SMTP_SSL as SMTP

from datetime import *
import credentials

def send_html_email_to_user(in_html, in_destination):
    smtp_server = 'smtp.gmail.com'
    sender = 'paraglidingSiteForecastBuddy@gmail.com'

    username = credentials.this_login
    password = credentials.this_password

    try:
        msg = MIMEText(in_html, 'html')
        msg['Subject'] = 'Site Forecast for: ' + str(date.today())
        msg['From'] = sender  # some SMTP servers will do this automatically, not all
        msg['To'] = in_destination

        conn = SMTP(smtp_server)
        conn.set_debuglevel(False)
        conn.login(username, password)
        try:
            conn.sendmail(sender, in_destination, msg.as_string())
        finally:
            conn.quit()
        print('        E-mail sent to: ' + in_destination)

    except:
        print('        ERROR: mail failed to: ' + in_destination)  # give an error message
