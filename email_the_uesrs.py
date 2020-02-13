import user_data  # Our own user data.
from send_html_email_to_user import *  # our function for emailing a user an HTML string
from build_html_from_forecast import *


def email_the_users(in_forecast):
    """
    This should take in a forecast instance and tailor a custom HTML message for each user.
    Then pass the HTML message to the email function.
    """
    print('')
    for user in user_data.users:
        html_string = build_html_from_forecast(in_forecast, user)
        send_html_email_to_user(html_string, user['addr'])
