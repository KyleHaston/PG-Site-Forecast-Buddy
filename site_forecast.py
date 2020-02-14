# Kyle Haston
# Feb 2020
# To supoprt users and user preferences, we need these custom structures.
# They will allow us to download all the data once, and create custom reports for each user.
# TODO: Don't assume units; pull them from the XML data. Or at least check them and email admin if they disagree.


class Period:
    """
    This class is a custom container for the following example XML data from NOAA:
        <period>
            <validTime timezone="UTC">00</validTime>
            <temperature units="degrees F">-999</temperature>
            <dewpoint units="degrees F">-999</dewpoint>
            <rh units="percent">-999</rh>
            <skyCover units="percent">-999</skyCover>
            <windSpeed units="mph">-1149</windSpeed>
            <windDirection units="angular degrees">-999</windDirection>
            <windGust units="mph">-999</windGust>
            <pop units="percent">-999</pop>
            <qpf units="inches">-999.00</qpf>
            <snowAmt units="inches">-999.00</snowAmt>
            <snowLevel units="feet"> -999</snowLevel>
            <wx> -999 </wx>
        </period>
    """
    def __init__(self, in_time=''):
        self.validTime = in_time
        self.temperature = ''
        self.dewpoint = ''
        self.rh = ''
        self.skyCover = ''
        self.windSpeed = ''
        self.windDirection = ''
        self.windGust = ''
        self.pop = ''
        self.qpf = ''
        self.snowAmt = ''
        self.snowLevel = ''
        # self.wx = ''  # This info denotes valid data.


class ForecastDay:
    """
    This class is a custom container for the following example XML data from NOAA:
        <forecastDay>
            <validDate>Feb 12</validDate>
            <period>
                (Our custom container for this info is above.)
            </period>
        </forecastDay>
    """
    def __init__(self, in_day=''):
        self.valid_date = in_day
        self.periods = []  # List of custom class defined above.


class SiteForecast:
    """
    This class is a custom container for the following example XML data from NOAA:
        <griddedForecast duration="168 hours">
            <forecastCreationTime>Wed Feb 12 21:24:16 2020 UTC</forecastCreationTime>
            <latitude units="degrees">31.698 </latitude>
            <longitude units="degrees">-110.495 </longitude>
            <elevation units="feet above mean sea-level">5197 </elevation>
            <location>7 Miles NNE Elgin AZ</location>
            <duration>168</duration>
            <interval>6</interval>
            <forecastDay>
                (Our custom container for this info is above.)
            </forecastDay>
        </griddedForecast>
    """
    def __init__(self, in_name=''):
        self.name = in_name
        self.forecast_creation_time = ''
        self.latitude = ''
        self.longitude = ''
        self.elevation = ''
        self.location = ''
        self.duration = ''
        self.interval = ''
        self.forecast_days = []  # List of custom class defined above.

        # This stuff we copy from our site knowledge data for ease of creating the HTML later.
        self.windLower = ''
        self.windUpper = ''
        self.windDirLower = ''
        self.windDirUpper = ''

        # Initialize these to true, but individual sites can override. Ex: don't show snow level for southern AZ sites.
        self.show_dewpoint = True
        self.show_rh = True
        self.show_skyCover = True
        self.show_pop = True
        self.show_qpf = True
        self.show_snowAmt = True
        self.show_snow = True
