# This takes in some HTML and a destination and sends an email
import sys
import yagmail
from datetime import *
import credentials


def send_html_email_to_user(in_html, in_destination):
    try:
        yag = yagmail.SMTP(credentials.this_login, credentials.this_password)
        yag.send(in_destination, 'Site Forecast for: ' + str(date.today()), contents=in_html)
        print('        E-mail sent to: ' + in_destination)

    except:
        print('        ERROR: mail failed to: ' + in_destination)  # give an error message
