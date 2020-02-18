# For weather gathering
import requests  # used to fetch the web page
from bs4 import BeautifulSoup
import datetime

import site_data  # Our own site data.
import site_forecast  # Our custom class definitions
import calendar

from tzwhere import tzwhere
import pytz

def build_forecast():
    full_forecast = []
    for site in site_data.sites:
        print('    Building forecast for site: ' + site['Name'] + '...')

        # Fetch XML data
        r = requests.get('https://www.wrh.noaa.gov/forecast/xml/xml.php?duration=96&interval=4&' + 'lat=' + site['lat'] + '&lon=' + site['lon'])

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

        site4cast.show_dewpoint = site['show_dewpoint']
        site4cast.show_rh = site['show_rh']
        site4cast.show_skyCover = site['show_skyCover']
        site4cast.show_pop = site['show_pop']
        site4cast.show_qpf = site['show_qpf']
        site4cast.show_snowAmt = site['show_snowAmt']
        site4cast.show_snowLevel = site['show_snowLevel']

        site4cast.latitude = float(site['lat'])
        site4cast.longitude = float(site['lon'])

        site4cast.timezone_str = site['timezone_str']
        if site4cast.timezone_str == '':  # If we don't have the timezone string in the site data...
            print('        ERROR: Timezone string for this site not in site data. Will try to resolve it.')
            site4cast.timezone_str = tzwhere.tzwhere().tzNameAt(site4cast.latitude, site4cast.longitude)

        for day in soup.find_all('forecastday'):  # for each day...s
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
                        try:
                            this_p.snowLevel = str(round(float(p.find('snowlevel').text)))  # Silly casting to get rid of silly data.
                        except:
                            try:  # This fixed a random bug that appeared while programming. TODO: Need better error handling b/c it's weather data.
                                this_p.snowLevel = str(round(float(p.find('snowlevel').text)))  # Silly casting to get rid of silly data.
                            except:
                                this_p.snowLevel = '0.00'

                        # To ease time conversion (based on timezone) later, create a datetime from this period's info.
                        yr = datetime.datetime.now().year
                        m = list(calendar.month_abbr).index(this_date.split()[0])
                        d = int(this_date.split()[1])
                        hr = int(this_p.validTime)
                        this_p.datetime = datetime.datetime(yr, m, d, hr)  # UTC datetime

                        local_tz = pytz.timezone(site4cast.timezone_str)
                        this_p.local_dt = this_p.datetime + local_tz.utcoffset(this_p.datetime)  # local datetime

                        this_day.periods.append(this_p)  # Append this period to the day we created one level above.

                site4cast.forecast_days.append(this_day)
        full_forecast.append(site4cast)
    return full_forecast
