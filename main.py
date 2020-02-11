# Kyle Haston
# Feb 9th, 2020
# I want a script to download the weather forecast for different paragliding sites and email it to me at the appropriate times.

# TODO: Instead of using the HTML data, download the XML (better for several reasons) and format into an HTML email.
# TODO: pretend this is a bug and fix it with a subsequent commit.

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

sites = [{'Name': 'Yaquina Head', 'coords': 'lat=44.67640&lon=-124.07810', 'goodWindDir': ['N', 'NW'], 'windLower': 7, 'windUpper': 12},  # TODO: Fix wind data
         {'Name': 'Cliffside', 'coords': 'lat=45.724844&lon=-120.726470', 'goodWindDir': ['E', 'NE', 'SE'], 'windLower': 7, 'windUpper': 12},  # TODO: Fix wind data
         {'Name': 'Cape Kiwanda', 'coords': 'lat=44.690&lon=-123.459', 'goodWindDir': ['N', 'NW'], 'windLower': 7, 'windUpper': 18},  # TODO: Fix wind data
         {'Name': 'Crestwood', 'coords': 'lat=45.333&lon=-122.940', 'goodWindDir': ['W', 'SW'], 'windLower': 7, 'windUpper': 12}]  # TODO: Fix wind data

report = []
for site in sites:
    r = requests.get('https://www.wrh.noaa.gov/forecast/wxtables/index.php?' + site['coords'] + '&table=custom&duration=3&interval=4')

    soup = BeautifulSoup(r.text, 'html.parser')
    temp = soup.body.contents

    tables = soup.find_all('table')
    for table in tables:
        if 'id' in table.attrs:
            # print(table.attrs)
            if table.attrs['id'] == 'mainTable':
                # We've found the data for this site that we want to include in the report.
                # print(site['Name'])
                # print(table.parent.parent)  # This is the droid we're looking for.
                report.append(table.parent.parent)

for idx, val in enumerate(report):
    # print(site)
    # Touch up the info. a bit.

    # Left-align the blue thingy.
    for tag in report[idx]:
        if not isinstance(tag, NavigableString):
            if 'style' in tag.attrs:
                if 'margin-left' in tag.attrs['style']:
                    tag.attrs['style'] = tag.attrs['style'].replace('margin-left: auto', 'margin-left: 0px')
                    tag.attrs['style'] = tag.attrs['style'].replace('width:600', 'width:auto')
                    # print('asdf')

    # Use site name chosen by user.
    tables = report[idx].find_all('table')
    for table in tables:
        trs = table.find_all('tr')
        for tr in trs:
            if 'Forecast For' in str(tr):
                tempStr = str(tr.contents[0].contents[0])
                newStr = tempStr.split('For Lat/Lon')[0] + 'for ' + sites[idx]['Name']
                tr.contents[0].contents = [NavigableString(newStr)]
                # Note: We're also getting rid of the next line. ex: "3 Miles NNW Newport OR"

    # Remove some info.
    caps = report[idx].find_all('caption')
    for cap in caps:
        cap.decompose()

    gc.collect()

    ths = report[idx].find_all('th')
    for th in ths:
        # if 'Weather' in th:
        #     th.decompose()
        if 'Dewpoint' in th:
            th.parent.decompose()
            # elif 'Snow Ratio' in th:  # TODO: Figure out how to remove all the random snow info.
            #     # th.decompose()
            #     # th.parent.contents = []
            #     temp = th
            #     print(temp)
            #     print('asdf')
            #
            #     temp = th.parent
            #     print(temp)
            #     print('asdf')
            # elif '12-hr Snow Total' in str(th):
            #     th.parent.decompose()
        elif 'Snow Level (ft)' in th:
            th.parent.decompose()
        elif 'Relative Humidity' in th:
            th.parent.decompose()
        elif 'Daily-Temp' in th:
            th.contents[0] = NavigableString('Daily-Temp (°F)')  # Add units
        elif 'Temp' in th:
            th.contents[0] = NavigableString('Temp (°F)')  # Add units
        elif 'Wind' in th:
            th.contents[0] = NavigableString('Wind (mph)')  # Add units
            # Color code wind DIRECTION based on site info.
            for cell in th.parent.contents:
                if 'td bgcolor' in str(cell):
                    dir = str(cell).split('>')[1].split('<')[0]  # I know you won't like this black magic, but it yields the wind direction.
                    if dir in sites[idx]['goodWindDir']:
                        cell.attrs['bgcolor'] = '#99ff66'
                    elif dir != '':
                        cell.attrs['bgcolor'] = '#ff5050'

            # # Color code wind SPEED based on site info.  # TODO: Get wind speed coloring figured out.
            # for cell in th.parent.parent.contents:
            #     if 'td bgcolor' in str(cell):
            #         speed = str(cell).split('>')[1].split('<')[0]  # I know you won't like this black magic, but it yields the wind direction.
            #         if speed != '' and speed != '\n':
            #             speed = int(speed)
            #             if speed > sites[idx]['windUpper']:  # If it's too fast...
            #                 cell.attrs['bgcolor'] = '#ff5050'
            #             elif speed < sites[idx]['windLower']:  # If it's too slow...
            #                 cell.attrs['bgcolor'] = '#b3cce6'
            #             else:  # If it's juuuuust right   :)
            #                 cell.attrs['bgcolor'] = '#99ff66'

    print(report[idx])

SMTPserver = 'smtp.mail.com'
sender = 'paraglidingSiteForecastBuddy@mail.com'
destination = ['microfarads@gmail.com']

USERNAME = "paraglidingSiteForecastBuddy"
PASSWORD = ";kj2345./,dsgf098"

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'

content = """\
Test message
"""

subject = "Sent from Python"

try:
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = subject
    msg['From'] = sender  # some SMTP servers will do this automatically, not all

    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(sender, destination, msg.as_string())
    finally:
        conn.quit()

except:
    sys.exit("mail failed; %s" % "CUSTOM_ERROR")  # give an error message
