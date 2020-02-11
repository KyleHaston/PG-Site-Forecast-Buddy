# Kyle Haston
# Feb 2020
# Script to download weather forecast for different paragliding sites and email it to me.

# For weather gathering
import requests  # used to fetch the web page
from bs4 import BeautifulSoup, NavigableString
import gc

# For email
import sys
import os
import re
from email.mime.text import MIMEText
from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# For the output file.
import datetime
import time
import random


def get_the_forecast():
    sites = [{'Name': 'Yaquina Head', 'coords': 'lat=44.67640&lon=-124.07810', 'windDirLower': 270, 'windDirUpper': 0, 'windLower': 7, 'windUpper': 12},  # TODO: Fix wind data
             {'Name': 'Cliffside', 'coords': 'lat=45.724844&lon=-120.726470', 'windDirLower': 45, 'windDirUpper': 135, 'windLower': 7, 'windUpper': 12},  # TODO: Fix wind data
             {'Name': 'Cape Kiwanda', 'coords': 'lat=44.690&lon=-123.459', 'windDirLower': 270, 'windDirUpper': 0, 'windLower': 7, 'windUpper': 18},  # TODO: Fix wind data
             {'Name': 'Crestwood', 'coords': 'lat=45.333&lon=-122.940', 'windDirLower': 225, 'windDirUpper': 270, 'windLower': 7, 'windUpper': 12}]  # TODO: Fix wind data

    buddies = ['☆*:. o(≧▽≦)o .:*☆', '໒( ͡ᵔ ▾ ͡ᵔ )७', '(⊙ᗜ⊙)', 'ლ(ʘ̆〰ʘ̆)ლ', '✿*∗˵╰༼✪ᗜ✪༽╯˵∗*✿', 'ᕦ( ヘ (oo) ヘ )ᕤ',
               '[ ⇀ ‿ ↼ ]', 'o͡͡͡╮໒( •̀ ‿ •́ )७╭o͡͡͡', '(}༼⊙-◞౪◟-⊙༽{)', 'o͡͡͡╮⁞ ^ ▃ ^ ⁞╭o͡͡͡, ', '٩(◕‿◕｡)۶', '୧(=ʘ͡ᗜʘ͡=)୨',
               'o͡͡͡╮░ O ◡ O ░╭o͡͡͡,', '໒( ◔ ▽ ◔ )७', '୧༼ ヘ ᗜ ヘ ༽୨', '╚═╏ ⇀ ͜ر ↼ ╏═╝', 'o͡͡͡╮໒( * ☯ ◞౪◟ ☯ * )७╭o͡͡͡',
               '୧〳 ” ʘ̆ ᗜ ʘ̆ ” 〵୨', '/╲/╭( •̀ ᗜ •́ )╮/╱﻿,', 'ᕙ░ ʘ̆ ᗜ ʘ̆ ░ᕗ', 'ԅ༼ ◔ ڡ ◔ ༽ง', '໒( ” •̀ ᗜ •́ ” )७',
               '୧༼ʘ̆ںʘ̆༽୨', 'ヽ(”`▽´)ﾉ', 'ʘ ͜ʖ ʘ', '༼ ༽ ლ(́◉◞౪◟◉‵ლ)', 'ლ(́◉◞౪◟◉‵ლ)']

    report = []
    forecast = ''  # Initialize the forecast to empty.
    random.seed(time.localtime().tm_sec)
    forecast += '<html><head></head><body><p>Hello from your site forecast buddy! '
    # forecast += buddies[random.randrange(len(buddies))]
    for site in sites:  # TODO: Get buddies working.
        forecast += '<p>Here\'s the report for ' + site['Name'] + ':'

        # Fetch XML data
        r = requests.get('https://www.wrh.noaa.gov/forecast/xml/xml.php?duration=71&interval=4&' + site['coords'])

        soup = BeautifulSoup(r.text, 'lxml')

        # Add a table.
        forecast += '<table width="auto" border="1">'

        # Create column headers. One for each day.
        forecast += '<tr><th></th>'  # One deliberate, empty column.
        for gf in soup.find_all('griddedforecast'):  # There can be only one.
            for fd in gf.find_all('forecastday'):
                for vd in fd.find_all('validdate'):
                    forecast += '<th colspan="6">' + vd.text + '</th>'
        forecast += '</tr>'

        # Create a home for each time interval.
        forecast += '<tr><th>Time (UTC): </th>'
        for gf in soup.find_all('griddedforecast'):
            for fd in gf.find_all('forecastday'):
                for vd in fd.find_all('validdate'):
                    for vt in fd.find_all('validtime'):
                        forecast += '<td>' + vt.text + '</td>'
        forecast += '</tr>'

        # Create a home for each temperature.
        forecast += '<tr><th>Temp (°F): </th>'
        for gf in soup.find_all('griddedforecast'):
            for fd in gf.find_all('forecastday'):
                for vd in fd.find_all('validdate'):
                    for vt in fd.find_all('temperature'):
                        if vt.text == '-999':
                            forecast += '<td>-</td>'
                        else:
                            forecast += '<td>' + vt.text + '</td>'
        forecast += '</tr>'

        # Create a home for each wind direction.
        forecast += '<tr><th>Wind Direction (°): </th>'
        for gf in soup.find_all('griddedforecast'):
            for fd in gf.find_all('forecastday'):
                for vd in fd.find_all('validdate'):
                    for wd in fd.find_all('winddirection'):
                        if wd.text == '-999':
                            forecast += '<td>-</td>'
                        else:
                            forecast += '<td'
                            if site['windDirLower'] < int(wd.text) < site['windDirUpper']:
                                forecast += ' bgcolor ="#ccffcc"'  # good wind direction
                            if (site['windDirLower'] - 15) < int(wd.text) < (site['windDirUpper'] + 15):
                                forecast += ' bgcolor ="#cccccc"'  # close to optimal wind direction
                            else:
                                forecast += ' bgcolor ="#ffcccc"'  # far from optimal wind direction
                            forecast += '>' + wd.text + '</td>'

        # Create a home for each wind speed.
        forecast += '<tr><th>Wind Speed (mph): </th>'
        for gf in soup.find_all('griddedforecast'):
            for fd in gf.find_all('forecastday'):
                for vd in fd.find_all('validdate'):
                    for ws in fd.find_all('windspeed'):
                        if ws.text == '-1149':
                            forecast += '<td>-</td>'
                        else:
                            forecast += '<td'
                            if int(ws.text) < site['windLower']:
                                forecast += ' bgcolor ="#cccccc"'  # too slow
                            elif int(ws.text) > site['windUpper']:
                                forecast += ' bgcolor ="#ffcccc"'  # too fast
                            else:
                                forecast += ' bgcolor ="#ccffcc"'   # juuuust right
                            forecast += '>' + ws.text + '</td>'
        forecast += '</tr>'

        # Close the table.
        forecast += '</table><p>'
    forecast += '</p></body></html>'  # Close the HTML.
    return forecast


def write_the_html_file(in_string):
    with open('forecast' + str(datetime.date.today()) + '.html', 'w') as file:
        file.write(in_string)


def email_the_thing(in_string):
    print('email not working yet!')
    # SMTPserver = 'smtp.mail.com'
    # sender = 'paraglidingSiteForecastBuddy@mail.com'
    # destination = ['microfarads@gmail.com']
    #
    # USERNAME = "paraglidingSiteForecastBuddy"
    # PASSWORD = ";kj2345./,dsgf098"
    #
    # # typical values for text_subtype are plain, html, xml
    # text_subtype = 'plain'
    #
    # content = """\
    # Test message
    # """
    #
    # subject = "Sent from Python"
    #
    # try:
    #     msg = MIMEText(content, text_subtype)
    #     msg['Subject'] = subject
    #     msg['From'] = sender  # some SMTP servers will do this automatically, not all
    #
    #     conn = SMTP(SMTPserver)
    #     conn.set_debuglevel(False)
    #     conn.login(USERNAME, PASSWORD)
    #     try:
    #         conn.sendmail(sender, destination, msg.as_string())
    #     finally:
    #         conn.quit()
    #
    # except:
    #     sys.exit("mail failed; %s" % "CUSTOM_ERROR")  # give an error message


if __name__ == "__main__":
    the_forecast = get_the_forecast()
    write_the_html_file(the_forecast)
    # email_the_thing(the_forecast)
