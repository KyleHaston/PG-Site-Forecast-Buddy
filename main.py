# Kyle Haston
# Feb 2020
# Script to download weather forecast for different paragliding sites and email it to me.

from build_forecast import *
from email_the_uesrs import  *


if __name__ == "__main__":
    forecast_data = build_forecast()
    email_the_users(forecast_data)
