# Kyle Haston
# Feb 2020
# Script to download weather forecast for different paragliding sites and email it to me.
# TODO: Get rid of missing data that is early in the forecast.

# For weather gathering
import requests  # used to fetch the web page
from bs4 import BeautifulSoup

# For email
import sys
from email.mime.text import MIMEText
from smtplib import SMTP_SSL as SMTP

# For the output file.
from datetime import *
import calendar
import time
import random

from site_data import sites  # Our own site data.


def get_the_forecast():
    report = []
    forecast = ''  # Initialize the forecast to empty.
    random.seed(time.localtime().tm_sec)
    forecast += '<html> <font face="Garamond"> <head> <p>Hello from your site forecast buddy! <p> </head> <body>'
    for site in sites:
        # Fetch XML data
        r = requests.get('https://www.wrh.noaa.gov/forecast/xml/xml.php?duration=96&interval=4&' + site['coords'])

        soup = BeautifulSoup(r.text, 'lxml')

        # Add a table.
        forecast += '<table width="auto" border="1">'
        forecast += '<tr><th rowspan="2">'
        forecast += '<b style="color:blue;font-size:125%">' + site['Name'] + '</b><br/>'
        forecast += '</th>'

        # List forecast creation info. and site info.  # TODO: Change this from UTC to PST.
        for gf in soup.find_all('griddedforecast'):  # There can be only one.
            for ft in gf.find_all('forecastcreationtime'):
                forecast += '<th colspan="25", rowspan="1"><span style="color:grey;font-size:75%">'
                forecast += 'Forecast created: ' + ft.text + '<br/>'
                forecast += 'Desired Conditions: '
                forecast += str(site['windLower']) + ' to ' + str(site['windUpper']) + ' mph from '
                forecast += str(site['windDirLower']) + '° to ' + str(site['windDirUpper']) + '°'
                forecast += '</span></th></tr>'

        # Convert dates and times from UTC to PST ----------------------------------------------------------------------
        date_times = []  # This will hold the datetime instances for each time interval in the XML data

        # Get the year
        year = ''  # initialize here for scope reasons
        for fct in soup.find_all('forecastcreationtime'):
            year = fct.text.split()[4]  # Is this poor form? It works at this moment in time...

        # Get the month abbreviations in lowercase.
        lower_month_abbr = list(calendar.month_abbr)
        for idx, val in enumerate(lower_month_abbr):
            lower_month_abbr[idx] = val.lower()

        # Instantiate a datetime for each moment in the XML data.
        for fd in soup.find_all('forecastday'):
            for vd in fd.find_all('validdate'):
                month = lower_month_abbr.index(vd.text.split()[0].lower())  # Get the month. I know this is ugly.
                day = vd.text.split()[1]  # Get the day. I know this is ugly too.
                for vt in fd.find_all('validtime'):
                    date_times.append(datetime(int(year), month, int(day), hour=int(vt.text), tzinfo=timezone.utc))

        # Subtract 7 hrs to convert from UTC to PST
        for idx, val in enumerate(date_times):
            date_times[idx] = date_times[idx] - timedelta(hours=7)

        # Distill a list of dates for the next part.
        dates = []
        times = []
        for d in date_times:
            dates.append(calendar.month_abbr[d.month] + ' ' + str(d.day))
            times.append(d.hour)

        # Create a column header for each date. It should span the correct number of columns.
        ordered_date_set = sorted(set(dates), key=dates.index)
        for idx, val in enumerate(ordered_date_set):  # For unique entries only...
            cols = dates.count(ordered_date_set[idx])  # get column span from the # of occurrences of this date
            forecast += '<th colspan="' + str(cols) + '">' + ordered_date_set[idx] + '</th>'
        forecast += '</tr>'

        # Time of Day --------------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Time (PST): </th>'
        for t in times:
            forecast += '<td>' + str(t).zfill(2) + '</td>'  # zfill lends the leading zero where appropriate
        forecast += '</tr>'

        # Temperature --------------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Temp (°F): </th>'
        for vt in soup.find_all('temperature'):
            if vt.text == '-999':
                forecast += '<td>-</td>'
            else:
                forecast += '<td>' + vt.text + '</td>'
        forecast += '</tr>'

        # Sky Cover ----------------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Sky Cover (%): </th>'
        for vt in soup.find_all('skycover'):
            if vt.text == '-999':
                forecast += '<td>-</td>'
            else:
                forecast += '<td>' + vt.text + '</td>'
        forecast += '</tr>'

        # Chance of Precipitation --------------------------------------------------------------------------------------
        if site['pop']:  # If we usually show this data for this site...
            forecast += '<tr><th align="right">Chance of Precip. (%): </th>'
            for vt in soup.find_all('pop'):
                if vt.text == '-999':
                    forecast += '<td>-</td>'
                else:
                    forecast += '<td'
                    if int(vt.text) > 30:  # TODO: Arbitrarily chose this threshold. Make a case for a better number.
                        forecast += ' bgcolor ="#ffcccc"'  # wet bad.
                    else:
                        forecast += ' bgcolor ="#ccffcc"'  # dry good.
                    forecast += '>' + vt.text + '%</td>'
            forecast += '</tr>'

        # Precipitation ------------------------------------------------------------------------------------------------
        if site['qpf']:  # If we usually show this data for this site...
            forecast += '<tr><th align="right">Precipitation ("): </th>'
            for vt in soup.find_all('qpf'):
                if vt.text == '-999.00':
                    forecast += '<td>-</td>'
                else:
                    forecast += '<td'
                    if float(vt.text) > 0.02:  # TODO: Arbitrarily chose this threshold. Make a case for a better number.
                        forecast += ' bgcolor ="#ffcccc"'  # wet bad.
                    else:
                        forecast += ' bgcolor ="#ccffcc"'  # dry good.
                    forecast += '>' + vt.text + '</td>'
            forecast += '</tr>'

        # Wind Direction -----------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Wind Direction (°): </th>'
        for wd in soup.find_all('winddirection'):
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

        # Wind Speed ---------------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Wind Speed (mph): </th>'
        for ws in soup.find_all('windspeed'):
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

        # Wind Gust ----------------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Wind Gust (mph): </th>'
        for ws in soup.find_all('windgust'):
            if ws.text == '-999':
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
    with open('forecast' + str(date.today()) + '.html', 'w') as file:
        file.write(in_string)


def email_the_thing(in_html):
    smtp_server = 'smtp.gmail.com'
    sender = 'paraglidingSiteForecastBuddy@gmail.com'
    destinations = ['microfarads@gmail.com']

    username = "paraglidingSiteForecastBuddy"
    password = "pgsite4castbuddy2468..../"

    # typical values for text_subtype are plain, html, xml
    text_subtype = 'plain'

    for recipient in destinations:
        try:
            msg = MIMEText(in_html, 'html')
            msg['Subject'] = 'Site Forecast for: ' + str(date.today())
            msg['From'] = sender  # some SMTP servers will do this automatically, not all
            msg['To'] = recipient

            conn = SMTP(smtp_server)
            conn.set_debuglevel(False)
            conn.login(username, password)
            try:
                conn.sendmail(sender, recipient, msg.as_string())
            finally:
                conn.quit()
            print('mail sent to: ' + recipient)

        except:
            sys.exit('ERROR: mail failed to: ' + recipient)  # give an error message


if __name__ == "__main__":
    the_forecast = get_the_forecast()
    write_the_html_file(the_forecast)
    # email_the_thing(the_forecast)
