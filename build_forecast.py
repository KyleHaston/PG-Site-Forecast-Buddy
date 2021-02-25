# For weather gathering
import requests  # used to fetch the web page
from bs4 import BeautifulSoup
import datetime
import time

import site_data  # Our own site data.
import site_data_OR_kiting
import site_data_WA
import site_data_Willamette_Valley
import site_data_OR_test_sites
import site_data_AZ

import site_forecast  # Our custom class definitions
import calendar

from tzwhere import tzwhere
import pytz


def build_all_forecasts(in_debug):
    full_forecast = []
    skipped_sites = []

    # Stitch all sites into a big list ---------------------------------------------------------------------------------
    if not in_debug:
        sites = site_data.sites
        for s in site_data_OR_kiting.OR_kiting_sites:
            sites.append(s)
        for s in site_data_WA.WA_sites:
            sites.append(s)
        for s in site_data_Willamette_Valley.OR_Willamette_Valley_sites:
            sites.append(s)
        for s in site_data_OR_test_sites.OR_test_sites:
            sites.append(s)
        for s in site_data_AZ.sites_AZ:
            sites.append(s)
    else:
        sites = site_data.sites[2:4]  # use a short list of sites for debugging
        # sites = [site_data.sites[4]]  # use a short list of sites for debugging

    # Get forecast for each site ---------------------------------------------------------------------------------------
    for site in sites:
        this_forecast = build_forecast(site)
        if this_forecast != -1:
            full_forecast.append(this_forecast)
        else:
            skipped_sites.append(site)  # Save for later.

    print('\n    Looping back to get forecasts for skipped sites:')
    for site in skipped_sites:
        print('        ' + site['Name'])
    print('\n')

    for site in skipped_sites:
        # Service was probably down for these sites, so wait some time between repeated requests.
        num_tries = 5  # try to fetch forecast his many times, then bail
        while num_tries > 0:
            num_tries -= 1
            print('    Sleeping a bit before requesting: ' + site['Name'])
            time.sleep(120)

            this_forecast = build_forecast(site)
            if this_forecast != -1:
                full_forecast.append(this_forecast)
                break

            if num_tries == 0:
                print('        Skipping site: ' + site['Name'] + ' since forecast service seems disrupted.')
                continue  # Just skip this site.

    return full_forecast


def build_forecast(in_site):
    print('    Building forecast for site: ' + in_site['Name'] + '...')

    # Sometimes the server returns and empty forecast, so let's check for that.
    # If we get an empty one, let's tack the site to the end of the list and carry on.

    # Fetch the weather data

    # Get the date and time now. Rounded 'back' 'to nearest hour.
    begin = datetime.datetime.today().isoformat().split('.')[0].split(':')[0] + ':00:00'
    delta = datetime.timedelta(hours=96)
    end = (datetime.datetime.today() + delta).isoformat().split('.')[0].split(':')[0] + ':00:00'

    # https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?lat=38.99&lon=-77.01&product=time-series&begin=2021-02-14T10:11:46&end=2021-02-17T10:11:46
    link = 'https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?' \
           'lat=' + in_site['lat'] + '&lon=' + in_site['lon'] + \
           '&product=time-series&begin=' + begin + '&end=' + end + \
           '&Unit=e&appt=appt&dew=dew&pop12=pop12&qpf=qpf&snow=snow&sky=sky&rh=rh&wspd=wspd&wdir=wdir&wx=wx' \
           '&wgust=wgust&precipa_r=precipa_r&sky_r=sky_r&td_r=td_r&temp_r=temp_r&wdir_r=wdir_r&wspd_r=wspd_r&wwa=wwa' \
           '&iceaccum=iceaccum&Submit=Submit'

            # https://graphical.weather.gov/xml/docs/elementInputNames.php
                # NDFD Parameter                                                Input Name
                # Apparent Temperature                                          appt
                # Dewpoint Temperature                                          dew
                # 12 Hour Probability of Precipitation                          pop12
                # Liquid Precipitation Amount                                   qpf
                # Snowfall Amount                                               snow
                # Cloud Cover Amount                                            sky
                # Relative Humidity                                             rh
                # Wind Speed                                                    wspd
                # Wind Direction                                                wdir
                # Weather                                                       wx
                # Wind Gust                                                     wgust
                # Real-time Mesoscale Analysis Precipitation                    precipa_r
                # Real-time Mesoscale Analysis GOES Effective Cloud Amount      sky_r
                # Real-time Mesoscale Analysis Dewpoint Temperature             td_r
                # Real-time Mesoscale Analysis Temperature                      temp_r
                # Real-time Mesoscale Analysis Wind Direction                   wdir_r
                # Real-time Mesoscale Analysis Wind Speed                       wspd_r
                # Watches, Warnings, and Advisories                             wwa
                # Ice Accumulation                                              iceaccum

    r = requests.get(link)
    print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')
    forecast_creation_time = soup.find('creation-date').text
    numDays = len(soup.find_all('forecastday'))
    if numDays != 5:
        print('        Got an empty forecast.')

        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'lxml')
        numDays = len(soup.find_all('forecastday'))
        if numDays != 5:
            print('        Got an empty forecast using modified longitude: ' + link)  # for manual debugging
            return -1
        # else:
        #     print('        Success with link: ' + link)  # for manual debugging

    # Create a new instance of site_forecast (custom class) for this site.
    site4cast = site_forecast.SiteForecast(in_site['Name'])

    # Add the region name and info.
    site4cast.region = in_site['Region']
    site4cast.info = in_site['Info']

    # Put the XML info. into our custom format.
    site4cast.forecast_creation_time = soup.find('creation-date').text
    site4cast.location = soup.find('location').text
    site4cast.duration = soup.find('duration').text
    site4cast.interval = soup.find('interval').text

    site4cast.windLower = str(in_site['windLower'])
    site4cast.windUpper = str(in_site['windUpper'])
    site4cast.windDirLower = str(in_site['windDirLower'])
    site4cast.windDirUpper = str(in_site['windDirUpper'])

    site4cast.show_dewpoint = in_site['show_dewpoint']
    site4cast.show_rh = in_site['show_rh']
    site4cast.show_skyCover = in_site['show_skyCover']
    site4cast.show_pop = in_site['show_pop']
    site4cast.show_qpf = in_site['show_qpf']
    site4cast.show_snowAmt = in_site['show_snowAmt']
    site4cast.show_snowLevel = in_site['show_snowLevel']

    site4cast.latitude = float(in_site['lat'])
    site4cast.longitude = float(in_site['lon'])
    site4cast.link = in_site['link']

    site4cast.timezone_str = in_site['timezone_str']
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
                    yr = datetime.datetime.now().year  # TODO: might fart out around new year
                    m = list(calendar.month_abbr).index(this_date.split()[0])
                    d = int(this_date.split()[1])
                    hr = int(this_p.validTime)
                    this_p.datetime = datetime.datetime(yr, m, d, hr)  # UTC datetime

                    local_tz = pytz.timezone(site4cast.timezone_str)
                    this_p.local_dt = this_p.datetime + local_tz.utcoffset(this_p.datetime)  # local datetime

                    this_day.periods.append(this_p)  # Append this period to the day we created one level above.

            site4cast.forecast_days.append(this_day)
    if len(site4cast.forecast_days) < 3:
        print('Found a bad one.')
        return -1
    else:
        return site4cast
