# Kyle Haston
# Feb 2020
# Script to download weather forecast for different paragliding sites and email it to me.

from fetch_forecast import *
from email_the_users import *

DEBUG = False  # True for debug mode (less sites, no email)

if __name__ == "__main__":
    forecast_data = fetch_all_forecasts(DEBUG)
    email_the_users(forecast_data, DEBUG)
