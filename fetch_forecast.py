# For weather gathering
import requests  # used to fetch the web page
from bs4 import BeautifulSoup
import datetime
import time

import site_data  # Our own site data.
import site_data_OR_kiting
import site_data_WA
import site_data_OR_test_sites
import site_data_AZ

import site_forecast  # Our custom class definitions
import calendar

from tzwhere import tzwhere
import pytz


def fetch_all_forecasts(in_debug):
    full_forecast = []
    skipped_sites = []

    # Stitch all sites into a big list ---------------------------------------------------------------------------------
    if not in_debug:
        sites = site_data.sites
        for s in site_data_OR_kiting.OR_kiting_sites:
            sites.append(s)
        for s in site_data_WA.WA_sites:
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
        this_forecast = fetch_forecast(site)
        if this_forecast != -1:
            full_forecast.append(this_forecast)
        else:
            skipped_sites.append(site)  # Save for later.
            print('\t\tSkipping ' + site['Name'])

    print('\n\tLooping back to get forecasts for skipped sites:')
    for site in skipped_sites:
        print('\t\t' + site['Name'])
    print('\n')

    for site in skipped_sites:
        # Service was probably down for these sites, so wait some time between repeated requests.
        num_tries = 5  # try to fetch forecast his many times, then bail
        while num_tries > 0:
            num_tries -= 1
            wait = 120
            print('\tSleeping for ' + str(wait) + ' socnds before requesting: ' + site['Name'])
            time.sleep(wait)

            this_forecast = fetch_forecast(site)
            if this_forecast != -1:
                full_forecast.append(this_forecast)
                break

            if num_tries == 0:
                print('\t\tSkipping site: ' + site['Name'] + ' since forecast service seems disrupted.')
                continue  # Just skip this site.

    return full_forecast


def fetch_forecast(in_site):
    print('\tFetching forecast for site: ' + in_site['Name'] + '...')

    # Get the date and time right meow. Rounded 'back' 'to nearest hour.
    begin = datetime.datetime.today().isoformat().split('.')[0].split(':')[0] + ':00:00'
    delta = datetime.timedelta(hours=96)
    end = (datetime.datetime.today() + delta).isoformat().split('.')[0].split(':')[0] + ':00:00'

    # Example link: https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?lat=38.99&lon=-77.01&product=time-series&begin=2021-02-14T10:11:46&end=2021-02-17T10:11:46
    link = 'https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?' \
           'lat=' + in_site['lat'] + '&lon=' + in_site['lon'] + \
           '&product=time-series&begin=' + begin + '&end=' + end + \
           '&Unit=e&appt=appt&dew=dew&pop12=pop12&qpf=qpf&snow=snow&sky=sky&rh=rh&wspd=wspd&wdir=wdir&wx=wx' \
           '&wgust=wgust&sky_r=sky_r&td_r=td_r&wdir_r=wdir_r&wspd_r=wspd_r' \
           '&iceaccum=iceaccum&icons=icons&Submit=Submit'

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

    r = -1
    try:
        r = requests.get(link, timeout=2)
        # print(r.text)
    except:
        return -1  # tell the level above that we should skip this one for now.

    soup = BeautifulSoup(r.text, 'xml')
    return [in_site, soup]
