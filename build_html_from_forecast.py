from datetime import *  # For the output file.
import time
from typing import List, Any

import pytz
from tzwhere import tzwhere
import numpy
from site_forecast import *

import palettes
import dropdown

from bs4 import BeautifulSoup
import datetime
import time
from collections import OrderedDict


def in_bounds(in_dir, in_lower, in_upper, in_margin):
    """
    For this to work, we travel the copass in the clowise direction.
    The lower bound is indicated first, and the upper is indicated second.
    For example, for NW to NE wind, 315° is lower bound and 45° is upper bound.
    :param in_dir:
    :param in_lower:
    :param in_upper:
    :param in_margin:
    :return:
    """
    try:
        # cast to float to handle all sorts of weirdness
        in_dir = float(in_dir)
        in_lower = max(float(in_lower) - float(in_margin), 0)
        in_upper = min(float(in_upper) + float(in_margin), 360)
        if in_lower < in_dir < in_upper or \
                in_upper <= in_lower < in_dir <= 360 or \
                0 <= in_dir < in_upper <= in_lower:
            return True
        else:
            return False
    except:
        print('        ERROR: Problem checking wind direction! Calling it bad by default.')
        return False


def build_summary(in_forecast, in_user):
    """
    So much data to parse that I want a concise version at the top.
    :param in_forecast:
    :param in_user:
    :return:
    """

    # Build me a summary table worthy of Mordor.

    # First we will trim down the incoming forecast so it only includes the sites that the user is interested in.
    slim_forecast: List[SiteForecast] = []  # container to hold only the sites that the user is interested in.
    for site_forecast in in_forecast:
        if in_user['addr_hash'] == 'server' or site_forecast.name in in_user['sites']:  # user is interested in this site...
            slim_forecast.append(site_forecast)  # append this site to the "slim" forecast

    number_of_sites = 0  # init to zero
    number_of_periods = 0  # init to zero
    site_names = []
    summary = [['']]
    dates = []  # dates for which we have data will be added to this container
    date_times = []  # periods for which we have data will be added to this container

    # First we get a handle on which time periods we have data for.
    for site_forecast in slim_forecast:
        site_names.append(site_forecast.name)
        # this_summary_row = [site_forecast.name]
        # number_of_sites += 1
        # temp_num_periods = 0  # some sites yield more periods than others, so we have to be a little tricky
        for day in site_forecast.forecast_days:
            # temp_num_periods += len(day.periods)
            if day.valid_date not in dates:
                dates.append(day.valid_date)
            for period in day.periods:
                if period.local_dt not in date_times:
                    date_times.append(period.local_dt)
        # number_of_periods = max(number_of_periods, temp_num_periods)
        # summary.append(this_summary_row)
    dates.sort()  # nice library bro
    date_times.sort()  # nice library bro
    date_times.insert(0, '')

    summary = [date_times.copy()]  # note: use .copy() due to mutable lists
    for name in site_names:
        temp = [False] * (len(date_times) - 1)
        temp.insert(0, name)
        summary.append(temp)

    # Then we add content to our summary.
    for site_forecast in slim_forecast:
        this_summary_row = [site_forecast.name]
        # number_of_sites += 1
        # temp_num_periods = 0  # some sites yield more periods than others, so we have to be a little tricky
        for day in site_forecast.forecast_days:
            # temp_num_periods += len(day.periods)
            for period in day.periods:
                if period.local_dt in date_times:
                    date_times.append(period.local_dt)
        # number_of_periods = max(number_of_periods, temp_num_periods)
        # summary.append(this_summary_row)

    # Turn some of the False flags to True if the conditions favor flying.
    for site_forecast in slim_forecast:
        row = site_names.index(site_forecast.name) + 1  # Add one to skip the first row which holds other info.
        # number_of_sites += 1
        # temp_num_periods = 0  # some sites yield more periods than others, so we have to be a little tricky
        for day in site_forecast.forecast_days:
            # temp_num_periods += len(day.periods)
            for p in day.periods:
                col = date_times.index(p.local_dt)
                # print('row: ' + str(row) + ', col: ' + str(col))

                # Good conds: >33F, <30% chance of precipitation, <0.02" rain, wind speed/gusts/direction ok.
                if int(p.temperature) > 33 and int(p.pop) < 30 and float(p.qpf) < 0.02 \
                        and int(site_forecast.windLower) <= int(p.windSpeed) <= int(site_forecast.windUpper) \
                        and int(site_forecast.windLower) <= int(p.windGust) <= int(site_forecast.windUpper) \
                        and in_bounds(p.windDirection, site_forecast.windDirLower, site_forecast.windDirUpper, 0):
                    summary[row][col] = True
                #     print('good time to fly: row: ' + str(row) + ', col: ' + str(col) + ' ' + str(p.local_dt))
                # else:
                #     print(' - poor time to fly: row: ' + str(row) + ', col: ' + str(col) + ' ' + str(p.local_dt))
                #     if int(p.temperature) > 33 and int(p.pop) < 30 and float(p.qpf) < 0.02:
                #         print(' -     first 3 ok')
                #     if in_bounds(p.windSpeed, site_forecast.windLower, site_forecast.windUpper, 0):
                #         print(' -     wind speed ok')
                #     if in_bounds(p.windGust, site_forecast.windLower, site_forecast.windUpper, 0):
                #         print(' -     gust speed ok')
                #     if in_bounds(p.windDirection, site_forecast.windDirLower, site_forecast.windDirUpper, 0):
                #         print(' -     wind dir ok')

    # Remove any rows (sites) that are entirely "no-fly"
    summary[1:] = [row for row in summary[1:] if (True in row)]  # notice we keep the top row (containing date-times)

    # Next, sort the summary based on what's working (best at the top).
    sorted_summary = [summary[0]]  # First row needs to stay put.
    sorted_summary.extend(sorted(summary[1:], key=lambda x: x.count(True), reverse=True))  # This's a powerful line.
    return sorted_summary


def print_html_summary(in_summary, in_palette):
    """
    Take in the summary and spit out an HTML representation.
    :param in_summary:
    :param in_palette:
    :return:
    """

    # Create an HTML table.
    html_summary = '<table width="auto" border="1" bgcolor ="' + in_palette.bkgnd + '" style="color:' + in_palette.text + '; text-align:center" >'

    for row in in_summary:
        # print(row)
        html_summary += '<tr>'  # Open the row.
        if row[0] == '':  # Treat the first row differently
            html_summary += '<td rowspan=2></td>'  # Add an empty cell for the upper-left corner.
            # html_summary += '<td></td>'  # Add an empty cell for the upper-left corner.

            # We want to give the date once (spanning multiple columns) for each unique date.
            # So we need to get a little tricky... sorry.
            html_date_row = ''  # initialize an empty container
            dates = []
            for dt in row[1:]:
                # print(dt.strftime("%a %b %d"))
                dates.append(dt.strftime("%a %b %d"))
            for d in dates:
                if d in html_date_row:
                    continue  # If we reach this, we've already added this date to the html string
                else:
                    num = dates.count(d)
                    html_date_row += '<td colspan="' + str(num) + '">' + d + '</td>'
                    # ex: datetime.datetime.now().strftime("%a %b %d")
            html_summary += html_date_row
            html_summary += '</tr>'  # Close the row.

            # Next add the hour for each fly/no-fly indicator.
            # TODO: This assumes all site forecasts have data on the same hour-marks. This is probably a bug.
            html_summary += '<tr>'
            for dt in row[1:]:
                # print(dt.strftime("%a %b %d"))
                html_summary += '<td>' + str(dt.hour) + '</td>'
            html_summary += '</tr>'  # Close the row.

        else:
            # For each time period, add the info.
            html_summary += '<td white-space: nowrap>' + row[0] + '</td>'  # Add the site name first.
            for col in row[1:]:  # Add the fly/no-fly indicator based on True/False flags.
                if col:  # True means it's go time bebe.
                    html_summary += '<td bgcolor="' + in_palette.good + '">&#128077;</td>'
                else:
                    # html_summary += '<td bgcolor="' + in_palette.warn + '">&#128078;</td>'
                    html_summary += '<td bgcolor="' + in_palette.warn + '"></td>'
            html_summary += '</tr>'  # Close the row.

    # Close the table and add a blank line.
    html_summary += '</table><p/><br/>'

    return html_summary


def build_html_from_forecast(in_forecast, in_user):
    """
    inputs: site and forecast
    returns: an HTML string
    """

    my_palette = palettes.Palette('')  # Instantiate the color scheme from the palette module.

    html_forecast = ''  # Initialize the forecast to empty.
    html_forecast += '<!DOCTYPE html> <html> <head>'

    # Add style for the collapsible stuff (site info button, etc.?)
    html_forecast += '<meta name="viewport" content="width=device-width, initial-scale=1">'
    html_forecast += '<style>'

    # Add the drop-down site info. stuff.
    for s in dropdown.style_defs:
        html_forecast += s

    html_forecast += '</style>'

    html_forecast += '<body bgcolor="' + my_palette.bdclr + '">'
    # html_forecast += '<font style="face:Garamond;color:' + my_palette.text + '">'
    html_forecast += '<font style="color:' + my_palette.text + '">'
    html_forecast += '<meta charset="character_set"> <p>Hello from your site forecast buddy!'
    html_forecast += '<p> </head> <body>'

    # TODO: get summary working again
    # # As of August 2020, I've decided I need a summary table at the top of the report that simplifies the readout.
    # summary = build_summary(in_forecast, in_user)  # create the summary
    # html_forecast += print_html_summary(summary, my_palette)  # append the summary to the HTML we have so far.

    # Next, carry on with detailed, individual forecasts.
    for this_site in in_forecast:
        if in_user['addr_hash'] != 'server' and this_site.name not in in_user['sites']:  # if not interested in this site...
            continue  # skip this site.
        # else... add this site's info to the HTML string

        # Add a table.
        html_forecast += '<table width="auto" border="1" bgcolor ="' + my_palette.bkgnd + '" style="color:' + my_palette.text + '" >'
        html_forecast += '<tr><th rowspan="2">'
        html_forecast += '<b style="color:' + my_palette.title + ';font-size:125%">'
        html_forecast += '<a href="' + this_site[0]['link'] + '"><u> ' + this_site[0]['Name'] + '</u></a>'
        html_forecast += '</b>'
        html_forecast += '<span style="color:' + my_palette.desc + ';font-size:75%"><div>Region: ' + this_site[0]['Region'] + '</div>'
        html_forecast += '<br/></th>'

        # DATES and TIMES ----------------------------------------------------------------------------------------------
        TLs = this_site[1].findAll('time-layout')  # collect all the time-layouts
        DTs = []  # array of datetimes
        for TL in TLs:
            SVTs = this_site[1].findAll('start-valid-time')
            for SVT in SVTs:
                # print(SVT.get_text())
                DT = datetime.datetime.fromisoformat(SVT.get_text())
                # print(DT)
                DTs.append(DT)

        DTs = sorted(DTs)  # put the datetimes in sequential order
        DTs = list(OrderedDict.fromkeys(DTs))  # remove duplicate entries

        days = []
        for DT in DTs:
            days.append(str(DT.strftime('%d %b<br>%a')))

        uniqueDays = []
        [uniqueDays.append([str(x.strftime('%d %b<br>%a')), 0]) for x in DTs if [str(x.strftime('%d %b<br>%a')), 0] not in uniqueDays]  # remove duplicate entries
        for uD in uniqueDays:
            uD[1] = days.count(uD[0])  # add count of entries for each day

        # # List forecast creation info. and site info.  # TODO: Change this from UTC to PST.
        html_forecast += '<th colspan="' + str(len(DTs)) + '", rowspan="1"><span style="color:' + my_palette.desc + ';font-size:75%">'
        html_forecast += 'Forecast created: ' + this_site[1].find('creation-date').text
        html_forecast += '</span></th></tr></tr></tr>'
        for uD in uniqueDays:
            html_forecast += '<td align="center" colspan="' + str(uD[1]) + '">' + uD[0] + '</td>'
        html_forecast += '<tr/>'

        html_forecast += '<tr align="center"><th nowrap>Time (local???): </th>'  # TODO: convert to local times
        for DT in DTs:
            html_forecast += '<td>' + str(DT.hour) + '</td>'
        html_forecast += '</tr>'

        # (Redundant)
        # html_forecast += '<tr><th align="right" nowrap>Day: </th>'
        # for uD in uniqueDays:
        #     html_forecast += '<td align="center" colspan="' + str(uD[1]) + '">' + str(uD[0]) + '</td>'
        # html_forecast += '</tr>'

        # Wind Speed ---------------------------------------------------------------------------------------------------
        dataset = this_site[1].find_all('wind-speed')
        for spd in dataset:  #
            if spd['type'] == 'sustained':
                html_forecast += '<tr><th align="right" nowrap>Wind Speed (' + spd['units'] + '): </th>'
            elif spd['type'] == 'gust':
                html_forecast += '<tr><th align="right" nowrap>Wind Speed Gust (' + spd['units'] + '): </th>'
            else:
                break

            thisTLkey = spd['time-layout']
            thisDTs = []
            for tl in TLs:
                if tl.find('layout-key').text == thisTLkey:
                    # print(str(tl.contents))
                    SVTs = tl.findAll('start-valid-time')
                    for SVT in SVTs:
                        # print(SVT.get_text())
                        DT = datetime.datetime.fromisoformat(SVT.get_text())
                        # print(DT)
                        thisDTs.append(DT)

            vals = spd.find_all('value')
            for DT in DTs:
                if DT in thisDTs:
                    i = thisDTs.index(DT)
                    html_forecast += '<td align="center" bgcolor ='
                    val = vals[i].text
                    if int(val) < int(this_site[0]['windLower']):
                        html_forecast += my_palette.lame  # too slow
                    elif int(val) > int(this_site[0]['windUpper']):
                        html_forecast += my_palette.warn  # too fast
                    else:
                        html_forecast += my_palette.good  # juuuust right
                    html_forecast += '>' + val + '</td>'
                else:
                    html_forecast += '<td/>'
            html_forecast += '</tr>'

        # Temperature --------------------------------------------------------------------------------------------------
        temps = this_site[1].find_all('temperature')
        for t in temps:
            # print(t['type'])
            if t['type'] == 'apparent':
                html_forecast += '<tr><th align="right" nowrap>Apparent Temp. (°' + t['units'] + '): </th>'
            elif t['type'] == 'dew point':
                html_forecast += '<tr><th align="right" nowrap>Dew Point (°' + t['units'] + '): </th>'
            else:
                break

            thisTLkey = t['time-layout']
            thisDTs = []
            for tl in TLs:
                if tl.find('layout-key').text == thisTLkey:
                    # print(str(tl.contents))
                    SVTs = tl.findAll('start-valid-time')
                    for SVT in SVTs:
                        # print(SVT.get_text())
                        DT = datetime.datetime.fromisoformat(SVT.get_text())
                        # print(DT)
                        thisDTs.append(DT)

            vals = t.find_all('value')
            for DT in DTs:
                if DT in thisDTs:
                    i = thisDTs.index(DT)
                    html_forecast += '<td align="center" '
                    val = vals[i].text
                    if int(val) < 36:  # threshold slightly above freezing
                        html_forecast += '<td bgcolor =' + my_palette.rain  # near freezing.
                    else:
                        html_forecast += '<td'  # warm enough
                    html_forecast += '>' + val + '</td>'
                else:
                    html_forecast += '<td/>'
            html_forecast += '</tr>'

        html_forecast += '<br/>'

    html_forecast += '</body></html>'  # Close the HTML.

    if in_user['addr_hash'] == 'server':  # Also save a full copy of the forecast to the server.
        print('\t\tSaving the full forecast to an HTML file on the server...')
        with open('forecasts/forecast ' + time.asctime().replace(':', '-') + '.html', 'w') as file:
            file.write(html_forecast)

    return html_forecast




    # TODO: Everything below here deprecated?


    #     # Relative Humidity --------------------------------------------------------------------------------------------
    #     if this_site.show_rh or in_user['addr_hash'] == 'server':  # If we typically list this info for this site...
    #         html_forecast += '<tr><th align="right" nowrap>Relative Humidity (%): </th>'
    #         for d in this_site.forecast_days:
    #             for p in d.periods:
    #                 html_forecast += '<td>' + p.rh + '</td>'
    #         html_forecast += '</tr>'
    #
    #     # Sky Cover ----------------------------------------------------------------------------------------------------
    #     if this_site.show_skyCover or in_user['addr_hash'] == 'server':  # If we typically list this info for this site...
    #         html_forecast += '<tr><th align="right" nowrap>Sky Cover (%): </th>'
    #         for d in this_site.forecast_days:
    #             for p in d.periods:
    #                 html_forecast += '<td>' + p.skyCover + '</td>'
    #         html_forecast += '</tr>'
    #
    #     # Chance of Precipitation --------------------------------------------------------------------------------------
    #     if this_site.show_pop or in_user['addr_hash'] == 'server':  # If we typically list this info for this site...
    #         html_forecast += '<tr><th align="right" nowrap>Chance of Precip. (%): </th>'
    #         for d in this_site.forecast_days:
    #             for p in d.periods:
    #                 if int(p.pop) > 30:  # TODO: Arbitrarily chose this threshold. Make a case for a better number.
    #                     html_forecast += '<td bgcolor =' + my_palette.rain + '>' + p.pop + '</td>'  # wet bad.
    #                 else:
    #                     html_forecast += '<td bgcolor =' + my_palette.good + '>' + p.pop + '</td>'  # dry good.
    #         html_forecast += '</tr>'
    #
    #     # Precipitation ------------------------------------------------------------------------------------------------
    #     if this_site.show_qpf or in_user['addr_hash'] == 'server':  # If we typically list this info for this site...
    #         html_forecast += '<tr><th align="right" nowrap>Precipitation ("): </th>'
    #         for d in this_site.forecast_days:
    #             for p in d.periods:
    #                 if float(p.qpf) > 0.02:  # TODO: Arbitrarily chose this threshold. Make a case for a better number.
    #                     html_forecast += '<td bgcolor =' + my_palette.rain + '>' + p.qpf + '</td>'  # wet bad.
    #                 else:
    #                     html_forecast += '<td bgcolor =' + my_palette.good + '>' + p.qpf + '</td>'  # dry good.
    #         html_forecast += '</tr>'
    #


    #
    #     # Wind Direction -----------------------------------------------------------------------------------------------
    #     html_forecast += '<tr><th align="right" nowrap>Wind Direction (°): </th>'
    #     for d in this_site.forecast_days:
    #         for p in d.periods:
    #
    #             # # Wind direction numerically, in degrees.
    #             # if int(this_site.windDirLower) < int(p.windDirection) < int(this_site.windDirUpper):
    #             #     html_forecast += '<td bgcolor =' + my_palette.good + '>' + p.windDirection + '</td>'  # good wind direction
    #             # elif (int(this_site.windDirLower) - 15) < int(p.windDirection) < (int(this_site.windDirUpper) + 15):
    #             #     html_forecast += '<td bgcolor =' + my_palette.lame + '>' + p.windDirection + '</td>'  # close to optimal wind direction
    #             # else:
    #             #     html_forecast += '<td bgcolor =' + my_palette.warn + '>' + p.windDirection + '</td>'  # far from optimal wind direction
    #
    #             # Change wind direction in degrees to the appropriate arrow.
    #             # ← = &#x2190; &larr;
    #             # ↑ = &#x2191; &uarr;
    #             # → = &#x2192; &rarr;
    #             # ↓ = &#x2193; &darr;
    #             # ↖ = &#x2196; &nwarr;
    #             # ↗ = &#x2197; &nearr;
    #             # ↙ = &#x2199; &swarr;
    #             # ↘ = &#x2198; &searr;
    #
    #             # Also, here's an example of embedding an image:
    #             # html_forecast += '<img alt="Embedded Image" width="8" height="8" src="http://icons.primail.ch/arrows/tl43.gif" />'
    #
    #             if 22.5 < int(p.windDirection) < 67.5:  # Wind from NE
    #                 wdir = '&#x2199;'
    #             elif 67.5 < int(p.windDirection) < 112.5:  # Wind from E
    #                 wdir = '&larr;'
    #             elif 112.5 < int(p.windDirection) < 157.5:  # Wind from SE
    #                 wdir = '&#x2196;'
    #             elif 157.5 < int(p.windDirection) < 202.5:  # Wind from S
    #                 wdir = '&uarr;'
    #             elif 202.5 < int(p.windDirection) < 247.5:  # Wind from SW
    #                 wdir = '&#x2197;'
    #             elif 247.5 < int(p.windDirection) < 292.5:  # Wind from W
    #                 wdir = '&rarr;'
    #             elif 292.5 < int(p.windDirection) < 337.5:  # Wind from NW
    #                 wdir = '&#x2198;'
    #             else:  # Wind from N
    #                 wdir = '&darr;'
    #
    #             if in_bounds(p.windDirection, this_site.windDirLower, this_site.windDirUpper, 0):
    #                 html_forecast += '<td bgcolor =' + my_palette.good + '>' + wdir + '</td>'  # good wind direction
    #             elif in_bounds(p.windDirection, this_site.windDirLower, this_site.windDirUpper, 30):
    #                 html_forecast += '<td bgcolor =' + my_palette.lame + '>' + wdir + '</td>'  # close to optimal wind direction
    #             else:
    #                 html_forecast += '<td bgcolor =' + my_palette.warn + '>' + wdir + '</td>'  # far from optimal wind direction
    #
    #     html_forecast += '</tr>'
    #
    #     # Wind Gust ----------------------------------------------------------------------------------------------------
    #     html_forecast += '<tr><th align="right" nowrap>Wind Gust (mph): </th>'
    #     for d in this_site.forecast_days:
    #         for p in d.periods:
    #             if int(p.windGust) < int(this_site.windLower):
    #                 html_forecast += '<td bgcolor =' + my_palette.lame + '>' + p.windGust + '</td>'  # too slow
    #             elif int(p.windGust) > int(this_site.windUpper):
    #                 html_forecast += '<td bgcolor =' + my_palette.warn + '>' + p.windGust + '</td>'  # too fast
    #             else:
    #                 html_forecast += '<td bgcolor =' + my_palette.good + '>' + p.windGust + '</td>'  # juuuust right
    #     html_forecast += '</tr>'
    #
    #     # Snow Amount --------------------------------------------------------------------------------------------------
    #     if this_site.show_snowAmt or in_user['addr_hash'] == 'server':  # If we typically list this info for this site...
    #         html_forecast += '<tr><th align="right" nowrap>Snow Amount ("): </th>'
    #         for d in this_site.forecast_days:
    #             for p in d.periods:
    #                 html_forecast += '<td>' + p.snowAmt + '</td>'
    #         html_forecast += '</tr>'
    #
    #     # Snow Level ---------------------------------------------------------------------------------------------------
    #     if this_site.show_snowLevel or in_user['addr_hash'] == 'server':  # If we typically list this info for this site...
    #         html_forecast += '<tr><th align="right" nowrap>Snow Level (ft): </th>'
    #         for d in this_site.forecast_days:
    #             for p in d.periods:
    #                 html_forecast += '<td>' + p.snowLevel + '</td>'
    #         html_forecast += '</tr>'
    #
    #     # Site Description/ Site Guide Information in Collapsible Box Format!
    #     html_forecast += '<tr><th colspan="' + str(table_cols) + '">'
    #     html_forecast += '<div class="dropdown">'
    #     html_forecast += '  <button class="dropbtn">Site Info.</button>'
    #     html_forecast += '  <div class="dropdown-content">'
    #
    #     # Link to the NOAA 7 day forecast
    #     html_forecast += '<a style="color:blue" href="https://forecast.weather.gov/MapClick.php?lon=' + str(this_site.longitude) + '&lat=' + str(this_site.latitude) + '"><u> NOAA 7 Day Forecast</u></a>'
    #
    #     html_forecast += '<br/>Desired Conditions: '
    #     html_forecast += this_site.windLower + ' to ' + this_site.windUpper + ' mph from '
    #     html_forecast += this_site.windDirLower + '° to ' + this_site.windDirUpper + '°'
    #     html_forecast += '<br/>' + this_site.info  # TODO: Get site guide/info. for sites.
    #     html_forecast += '  </div>'
    #     html_forecast += '</div>'
    #     html_forecast += '</div></th></tr>'  # end row
    #
    #     # Close the table.
    #     html_forecast += '</table><p>'
    #     html_forecast += '<br>'  # Add a blank row between site forecasts.
    #     html_forecast += '</p>'
    #
    # html_forecast += '</body></html>'  # Close the HTML.
    #
    # if in_user['addr_hash'] == 'server':  # Also save a full copy of the forecast to the server.
    #     print('        Saving the full forecast to an HTML file on the server...')
    #     with open('forecasts/forecast ' + time.asctime().replace(':', '-') + '.html', 'w') as file:
    #         file.write(html_forecast)
    #
    # return html_forecast
