from datetime import *  # For the output file.
import calendar
import time
import random

import palettes


def build_html_from_forecast(in_forecast, in_user):
    """
    This should take in a forecast instance and a user and return an HTML string containing the forecast for that
    user's sites.
    """

    my_palette = palettes.Palette('')  # Instantiate the color scheme from the palette module.

    html_forecast = ''  # Initialize the forecast to empty.
    html_forecast += '<html> <body bgcolor="' + my_palette.bdclr + '">'
    html_forecast += '<font style="face:Garamond;color:' + my_palette.text + '">'
    html_forecast +=  '<head> <p>Hello from your site forecast buddy!<p> </head> <body>'

    for this_site in in_forecast:
        if in_user['addr'] != 'server' and this_site.name not in in_user['sites']:  # if the user is not interested in this site...
            continue  # skip this site.

        # else... add this site's info to the HTML string

        # Add a table.
        html_forecast += '<table width="auto" border="1" bgcolor ="' + my_palette.bkgnd + '" style="color:' + my_palette.text + '" >'
        html_forecast += '<tr><th rowspan="2">'
        html_forecast += '<b style="color:' + my_palette.title + ';font-size:125%">' + this_site.name + '</b><br/>'
        html_forecast += '</th>'

        # List forecast creation info. and site info.  # TODO: Change this from UTC to PST.
        html_forecast += '<th colspan="25", rowspan="1"><span style="color:' + my_palette.desc + ';font-size:75%">'
        html_forecast += 'Forecast created: ' + this_site.forecast_creation_time + '<br/>'
        html_forecast += 'Desired Conditions: '
        html_forecast += this_site.windLower + ' to ' + this_site.windUpper + ' mph from '
        html_forecast += this_site.windDirLower + '° to ' + this_site.windDirUpper + '°'
        html_forecast += '</span></th></tr>'

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
        html_forecast += '<tr>'
        for d in this_site.forecast_days:
            html_forecast += '<th colspan="' + str(len(d.periods)) + '">' + d.valid_date + '</th>'
        html_forecast += '</tr>'

        # Time of Day --------------------------------------------------------------------------------------------------
        html_forecast += '<tr><th align="right">Time (UTC): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                html_forecast += '<td>' + p.validTime + '</td>'
        html_forecast += '</tr>'

        # Temperature --------------------------------------------------------------------------------------------------
        html_forecast += '<tr><th align="right">Temp (°F): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                html_forecast += '<td>' + p.temperature + '</td>'
        html_forecast += '</tr>'

        # Dewpoint -----------------------------------------------------------------------------------------------------
        if this_site.show_dewpoint or in_user['addr'] == 'server':  # If we typically list this info for this site...
            html_forecast += '<tr><th align="right">Dewpoint (°F): </th>'
            for d in this_site.forecast_days:
                for p in d.periods:
                    html_forecast += '<td>' + p.dewpoint + '</td>'
            html_forecast += '</tr>'

        # Relative Humidity --------------------------------------------------------------------------------------------
        if this_site.show_rh or in_user['addr'] == 'server':  # If we typically list this info for this site...
            html_forecast += '<tr><th align="right">Relative Humidity (%): </th>'
            for d in this_site.forecast_days:
                for p in d.periods:
                    html_forecast += '<td>' + p.rh + '</td>'
            html_forecast += '</tr>'

        # Sky Cover ----------------------------------------------------------------------------------------------------
        if this_site.show_skyCover or in_user['addr'] == 'server':  # If we typically list this info for this site...
            html_forecast += '<tr><th align="right">Sky Cover (%): </th>'
            for d in this_site.forecast_days:
                for p in d.periods:
                    html_forecast += '<td>' + p.skyCover + '</td>'
            html_forecast += '</tr>'

        # Chance of Precipitation --------------------------------------------------------------------------------------
        if this_site.show_pop or in_user['addr'] == 'server':  # If we typically list this info for this site...
            html_forecast += '<tr><th align="right">Chance of Precip. (%): </th>'
            for d in this_site.forecast_days:
                for p in d.periods:
                    if int(p.pop) > 30:  # TODO: Arbitrarily chose this threshold. Make a case for a better number.
                        html_forecast += '<td bgcolor =' + my_palette.warn + '>' + p.pop + '</td>'  # wet bad.
                    else:
                        html_forecast += '<td bgcolor =' + my_palette.good + '>' + p.pop + '</td>'  # dry good.
            html_forecast += '</tr>'

        # Precipitation ------------------------------------------------------------------------------------------------
        if this_site.show_qpf or in_user['addr'] == 'server':  # If we typically list this info for this site...
            html_forecast += '<tr><th align="right">Precipitation ("): </th>'
            for d in this_site.forecast_days:
                for p in d.periods:
                    if float(p.qpf) > 0.02:  # TODO: Arbitrarily chose this threshold. Make a case for a better number.
                        html_forecast += '<td bgcolor =' + my_palette.warn + '>' + p.qpf + '</td>'  # wet bad.
                    else:
                        html_forecast += '<td bgcolor =' + my_palette.good + '>' + p.qpf + '</td>'  # dry good.
            html_forecast += '</tr>'

        # Wind Speed ---------------------------------------------------------------------------------------------------
        html_forecast += '<tr><th align="right">Wind Speed (mph): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                if int(p.windSpeed) < int(this_site.windLower):
                    html_forecast += '<td bgcolor =' + my_palette.lame + '>' + p.windSpeed + '</td>'  # too slow
                elif int(p.windSpeed) > int(this_site.windUpper):
                    html_forecast += '<td bgcolor =' + my_palette.warn + '>' + p.windSpeed + '</td>'  # too fast
                else:
                    html_forecast += '<td bgcolor =' + my_palette.good + '>' + p.windSpeed + '</td>'  # juuuust right
        html_forecast += '</tr>'

        # Wind Direction -----------------------------------------------------------------------------------------------
        html_forecast += '<tr><th align="right">Wind Direction (°): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:

                # # Wind direction numerically, in degrees.
                # if int(this_site.windDirLower) < int(p.windDirection) < int(this_site.windDirUpper):
                #     html_forecast += '<td bgcolor =' + my_palette.good + '>' + p.windDirection + '</td>'  # good wind direction
                # elif (int(this_site.windDirLower) - 15) < int(p.windDirection) < (int(this_site.windDirUpper) + 15):
                #     html_forecast += '<td bgcolor =' + my_palette.lame + '>' + p.windDirection + '</td>'  # close to optimal wind direction
                # else:
                #     html_forecast += '<td bgcolor =' + my_palette.warn + '>' + p.windDirection + '</td>'  # far from optimal wind direction

                # Change wind direction in degrees to the appropriate arrow.
                # ← = &#x2190
                # ↑ = &#x2191
                # → = &#x2192
                # ↓ = &#x2193
                # ↖ = &#x2196
                # ↗ = &#x2197
                # ↙ = &#x2199
                # ↘ = &#x2198

                if 22.5 < int(p.windDirection) < 67.5:  # Wind from NE
                    wdir = '&#x2199'
                elif 67.5 < int(p.windDirection) < 112.5:  # Wind from E
                    wdir = '&#x2190'
                elif 112.5 < int(p.windDirection) < 157.5:  # Wind from SE
                    wdir = '&#x2196'
                elif 157.5 < int(p.windDirection) < 202.5:  # Wind from S
                    wdir = '&#x2191'
                elif 202.5 < int(p.windDirection) < 247.5:  # Wind from SW
                    wdir = '&#x2197'
                elif 247.5 < int(p.windDirection) < 292.5:  # Wind from W
                    wdir = '&#x2192'
                elif 292.5 < int(p.windDirection) < 337.5:  # Wind from NW
                    wdir = '&#x2198'
                else:  # Wind from N
                    wdir = '&#x2193'

                if int(this_site.windDirLower) < int(p.windDirection) < int(this_site.windDirUpper):
                    html_forecast += '<td bgcolor =' + my_palette.good + '>' + wdir + '</td>'  # good wind direction
                elif (int(this_site.windDirLower) - 15) < int(p.windDirection) < (int(this_site.windDirUpper) + 15):
                    html_forecast += '<td bgcolor =' + my_palette.lame + '>' + wdir + '</td>'  # close to optimal wind direction
                else:
                    html_forecast += '<td bgcolor =' + my_palette.warn + '>' + wdir + '</td>'  # far from optimal wind direction

        html_forecast += '</tr>'

        # Wind Gust ----------------------------------------------------------------------------------------------------
        html_forecast += '<tr><th align="right">Wind Gust (mph): </th>'
        for d in this_site.forecast_days:
            for p in d.periods:
                if int(p.windGust) < int(this_site.windLower):
                    html_forecast += '<td bgcolor =' + my_palette.lame + '>' + p.windGust + '</td>'  # too slow
                elif int(p.windGust) > int(this_site.windUpper):
                    html_forecast += '<td bgcolor =' + my_palette.warn + '>' + p.windGust + '</td>'  # too fast
                else:
                    html_forecast += '<td bgcolor =' + my_palette.good + '>' + p.windGust + '</td>'  # juuuust right
        html_forecast += '</tr>'

        # Snow Amount --------------------------------------------------------------------------------------------------
        if this_site.show_snowAmt or in_user['addr'] == 'server':  # If we typically list this info for this site...
            html_forecast += '<tr><th align="right">Snow Amount ("): </th>'
            for d in this_site.forecast_days:
                for p in d.periods:
                    html_forecast += '<td>' + p.snowAmt + '</td>'
            html_forecast += '</tr>'

        # Snow Level ---------------------------------------------------------------------------------------------------
        if this_site.show_snowLevel or in_user['addr'] == 'server':  # If we typically list this info for this site...
            html_forecast += '<tr><th align="right">Snow Level (ft): </th>'
            for d in this_site.forecast_days:
                for p in d.periods:
                    html_forecast += '<td>' + p.snowLevel + '</td>'
            html_forecast += '</tr>'

        # Close the table.
        html_forecast += '</table><p>'
    html_forecast += '</p></body></html>'  # Close the HTML.

    if in_user['addr'] == 'server':  # Also save a full copy of the forecast to the server.
        print('        Saving the full forecast to an HTML file on the server...')
        with open('forecast' + str(date.today()) + '.html', 'w') as file:
            file.write(html_forecast)

    return html_forecast