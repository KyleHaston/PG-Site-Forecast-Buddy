# Kyle Haston
# Feb 2020
# Script to download weather forecast for different paragliding sites and email it to me.
# TODO: Get rid of missing data that is early in the forecast. (Filter out <wx> -999 </wx>)
# TODO Take out sky cover for Mustang

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

import site_data  # Our own site data.
import user_data  # Our own user data.
import site_forecast  # Our custom class definitions


def build_forecast():
    full_forecast = []
    for site in site_data.sites:
        print('    Building forecast for site: ' + site['Name'] + '...')

        # Fetch XML data
        r = requests.get('https://www.wrh.noaa.gov/forecast/xml/xml.php?duration=96&interval=4&' + site['coords'])

        soup = BeautifulSoup(r.text, 'lxml')

        # Create a new instance of site_forecast (custom class) for this site.
        site4cast = site_forecast.SiteForecast(site['Name'])

        # Put the XML info. into our custom format.
        site4cast.forecast_creation_time = soup.find('forecastcreationtime').text
        site4cast.location = soup.find('location').text
        site4cast.duration = soup.find('duration').text
        site4cast.interval = soup.find('interval').text

        site4cast.windLower = str(site['windLower'])
        site4cast.windUpper = str(site['windUpper'])
        site4cast.windDirLower = str(site['windDirLower'])
        site4cast.windDirUpper = str(site['windDirUpper'])

        for day in soup.find_all('forecastday'):  # for each day...
            this_date = day.find('validdate').text  # get the validdate

            # Bug fix: Only add this day to the forecast if it has at least one period with valid data in it.
            add_me = False
            for p in day.find_all('period'):  # for each period during this day...
                if p.find('wx').text != ' -999 ':  # Only if there is valid data for this period...
                    add_me = True

            if add_me:
                this_day = site_forecast.ForecastDay(this_date)  # initialize a forecastday with this date
                for p in day.find_all('period'):  # for each period during this day...
                    if p.find('wx').text != ' -999 ':  # Only if there is valid data for this period...
                        this_p = site_forecast.Period()  # initialize an empty period (custom class)
                        # fill in the period data
                        this_p.validTime = p.find('validtime').text
                        this_p.temperature = p.find('temperature').text
                        this_p.dewpoint = p.find('dewpoint').text
                        this_p.rh = p.find('rh').text
                        this_p.skyCover = p.find('skycover').text
                        this_p.windSpeed = p.find('windspeed').text
                        this_p.windDirection = p.find('winddirection').text
                        this_p.windGust = p.find('windgust').text
                        this_p.pop = p.find('pop').text
                        this_p.qpf = p.find('qpf').text
                        this_p.snowAmt = p.find('snowamt').text
                        this_p.snowLevel = str(round(float(p.find('snowlevel').text)))  # Silly casting to get rid of silly data.

                        # try:  # This fixed a random bug that appeared while programming. TODO: Need better error handling b/c it's weather data.
                        #     this_p.snowLevel = str(round(float(p.find('snowlevel').text)))  # Silly casting to get rid of silly data.
                        # except:
                        #     this_p.snowLevel = '0.00'

                        this_day.periods.append(this_p)  # Append this period to the day we created one level above.

                site4cast.forecast_days.append(this_day)
        full_forecast.append(site4cast)
    return full_forecast


def write_the_html_file(in_string):
    with open('forecast' + str(date.today()) + '.html', 'w') as file:
        file.write(in_string)


def save_the_full_forecast_on_the_server(in_full_forecast):  # Yep. That's what I'm calling it.
    print('')
    print('    Saving the full forecast to the server...')

    forecast = ''  # Initialize the forecast to empty.
    forecast += '<html> <font face="Garamond"> <head> <p>Hello from your site forecast buddy! <p> </head> <body>'
    for this_site in in_full_forecast:

        # Add a table.
        forecast += '<table width="auto" border="1">'
        forecast += '<tr><th rowspan="2">'
        forecast += '<b style="color:blue;font-size:125%">' + this_site.name + '</b><br/>'
        forecast += '</th>'

        # List forecast creation info. and site info.  # TODO: Change this from UTC to PST.
        forecast += '<th colspan="25", rowspan="1"><span style="color:grey;font-size:75%">'
        forecast += 'Forecast created: ' + this_site.forecast_creation_time + '<br/>'
        forecast += 'Desired Conditions: '
        forecast += this_site.windLower + ' to ' + this_site.windUpper + ' mph from '
        forecast += this_site.windDirLower + '° to ' + this_site.windDirUpper + '°'
        forecast += '</span></th></tr>'

        # TODO: Convert to user's preferred time zone.
        # # Convert dates and times from UTC to PST ----------------------------------------------------------------------
        # date_times = []  # This will hold the datetime instances for each time interval in the XML data
        #
        # # Get the year
        # year = ''  # initialize here for scope reasons
        # for fct in soup.find_all('forecastcreationtime'):
        #     year = fct.text.split()[4]  # Is this poor form? It works at this moment in time...
        #
        # # Get the month abbreviations in lowercase.
        # lower_month_abbr = list(calendar.month_abbr)
        # for idx, val in enumerate(lower_month_abbr):
        #     lower_month_abbr[idx] = val.lower()
        #
        # # Instantiate a datetime for each moment in the XML data.
        # for fd in soup.find_all('forecastday'):
        #     for vd in fd.find_all('validdate'):
        #         month = lower_month_abbr.index(vd.text.split()[0].lower())  # Get the month. I know this is ugly.
        #         day = vd.text.split()[1]  # Get the day. I know this is ugly too.
        #         for vt in fd.find_all('validtime'):
        #             date_times.append(datetime(int(year), month, int(day), hour=int(vt.text), tzinfo=timezone.utc))
        #
        # # Subtract 7 hrs to convert from UTC to PST
        # for idx, val in enumerate(date_times):
        #     date_times[idx] = date_times[idx] - timedelta(hours=7)
        #
        # # Distill a list of dates for the next part.
        # dates = []
        # times = []
        # for d in date_times:
        #     dates.append(calendar.month_abbr[d.month] + ' ' + str(d.day))
        #     times.append(d.hour)
        #
        # # Create a column header for each date. It should span the correct number of columns.
        # ordered_date_set = sorted(set(dates), key=dates.index)
        # for idx, val in enumerate(ordered_date_set):  # For unique entries only...
        #     cols = dates.count(ordered_date_set[idx])  # get column span from the # of occurrences of this date
        #     forecast += '<th colspan="' + str(cols) + '">' + ordered_date_set[idx] + '</th>'
        # forecast += '</tr>'
        #
        # # Time of Day --------------------------------------------------------------------------------------------------
        # forecast += '<tr><th align="right">Time (PST): </th>'
        # for t in times:
        #     forecast += '<td>' + str(t).zfill(2) + '</td>'  # zfill lends the leading zero where appropriate
        # forecast += '</tr>'

        # Dates --------------------------------------------------------------------------------------------------
        forecast += '<tr>'
        for d in this_site.forecast_days:
            forecast += '<th colspan="' + str(len(d.periods)) + '">' + d.valid_date + '</th>'
        forecast += '</tr>'

        # Time of Day --------------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Time (UTC): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                forecast += '<td>' + p.validTime + '</td>'
        forecast += '</tr>'

        # Temperature --------------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Temp (°F): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                forecast += '<td>' + p.temperature + '</td>'
        forecast += '</tr>'

        # Dewpoint -----------------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Dewpoint (°F): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                forecast += '<td>' + p.dewpoint + '</td>'
        forecast += '</tr>'

        # Relative Humidity --------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Relative Humidity (%): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                forecast += '<td>' + p.rh + '</td>'
        forecast += '</tr>'

        # Sky Cover ----------------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Sky Cover (%): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                forecast += '<td>' + p.skyCover + '</td>'
        forecast += '</tr>'

        # Wind Speed ---------------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Wind Speed (mph): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                if int(p.windSpeed) < int(this_site.windLower):
                    forecast += '<td bgcolor ="#cccccc">' + p.windSpeed + '</td>'  # too slow
                elif int(p.windSpeed) > int(this_site.windUpper):
                    forecast += '<td bgcolor ="#ffcccc">' + p.windSpeed + '</td>'  # too fast
                else:
                    forecast += '<td bgcolor ="#ccffcc">' + p.windSpeed + '</td>'  # juuuust right
        forecast += '</tr>'

        # Wind Direction -----------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Wind Direction (°): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                if int(this_site.windDirLower) < int(p.windDirection) < int(this_site.windDirUpper):
                    forecast += '<td bgcolor ="#ccffcc">' + p.windDirection + '</td>'  # good wind direction
                elif (int(this_site.windDirLower) - 15) < int(p.windDirection) < (int(this_site.windDirUpper) + 15):
                    forecast += '<td bgcolor ="#cccccc">' + p.windDirection + '</td>'  # close to optimal wind direction
                else:
                    forecast += '<td bgcolor ="#ffcccc">' + p.windDirection + '</td>'  # far from optimal wind direction
        forecast += '</tr>'

        # Wind Gust ----------------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Wind Gust (mph): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                if int(p.windGust) < int(this_site.windLower):
                    forecast += '<td bgcolor ="#cccccc">' + p.windGust + '</td>'  # too slow
                elif int(p.windGust) > int(this_site.windUpper):
                    forecast += '<td bgcolor ="#ffcccc">' + p.windGust + '</td>'  # too fast
                else:
                    forecast += '<td bgcolor ="#ccffcc">' + p.windGust + '</td>'  # juuuust right
        forecast += '</tr>'

        # Chance of Precipitation --------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Chance of Precip. (%): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                if int(p.pop) > 30:  # TODO: Arbitrarily chose this threshold. Make a case for a better number.
                    forecast += '<td bgcolor ="#ffcccc">' + p.pop + '</td>'  # wet bad.
                else:
                    forecast += '<td bgcolor ="#ccffcc">' + p.pop + '</td>'  # dry good.
        forecast += '</tr>'

        # Precipitation ------------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Precipitation ("): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                if float(p.qpf) > 0.02:  # TODO: Arbitrarily chose this threshold. Make a case for a better number.
                    forecast += '<td bgcolor ="#ffcccc">' + p.qpf + '</td>'  # wet bad.
                else:
                    forecast += '<td bgcolor ="#ccffcc">' + p.qpf + '</td>'  # dry good.
        forecast += '</tr>'

        # Snow Amount --------------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Snow Amount ("): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                forecast += '<td>' + p.snowAmt + '</td>'
        forecast += '</tr>'

        # Snow Level ---------------------------------------------------------------------------------------------------
        forecast += '<tr><th align="right">Snow Level (ft): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                forecast += '<td>' + p.snowLevel + '</td>'
        forecast += '</tr>'

        # Close the table.
        forecast += '</table><p>'
    forecast += '</p></body></html>'  # Close the HTML.

    write_the_html_file(forecast)


def email_the_users(in_forecast_data):
    print('')
    for user in user_data.users:
        print('    Emailing: ' + user['addr'])


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
    forecast_data = build_forecast()
    save_the_full_forecast_on_the_server(forecast_data)
    email_the_users(forecast_data)
