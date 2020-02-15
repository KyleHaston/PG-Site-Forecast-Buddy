# For weather gathering
import requests  # used to fetch the web page
from bs4 import BeautifulSoup

import site_data  # Our own site data.
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

        site4cast.show_dewpoint = site['show_dewpoint']
        site4cast.show_rh = site['show_rh']
        site4cast.show_skyCover = site['show_skyCover']
        site4cast.show_pop = site['show_pop']
        site4cast.show_qpf = site['show_qpf']
        site4cast.show_snowAmt = site['show_snowAmt']
        site4cast.show_snowLevel = site['show_snowLevel']

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
                        try:
                            this_p.snowLevel = str(round(float(p.find('snowlevel').text)))  # Silly casting to get rid of silly data.
                        except:
                            try:  # This fixed a random bug that appeared while programming. TODO: Need better error handling b/c it's weather data.
                                this_p.snowLevel = str(round(float(p.find('snowlevel').text)))  # Silly casting to get rid of silly data.
                            except:
                                this_p.snowLevel = '0.00'

                        this_day.periods.append(this_p)  # Append this period to the day we created one level above.

                site4cast.forecast_days.append(this_day)
        full_forecast.append(site4cast)
    return full_forecast
