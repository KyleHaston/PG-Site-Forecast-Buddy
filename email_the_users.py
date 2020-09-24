import user_data  # Our own user data.
import email_addresses   # email address lookup by hash
from send_html_email_to_user import *  # our function for emailing a user an HTML string
from build_html_from_forecast import *


def email_the_users(in_forecast, in_debug):
    """
    This should take in a forecast instance and tailor a custom HTML message for each user.
    Then pass the HTML message to the email function.
    """
    print('')
    print('    E-mailing the users...')
    if in_debug:  # in debug mode, a forecast file is saved to the server
        html_string = build_html_from_forecast(in_forecast, user_data.users[0])  # assumes server is first entry
    else:  # not debug mode: send emails out
        for user in user_data.users:
            if user['addr_hash'] != 'server':
                html_string = build_html_from_forecast(in_forecast, user)
                send_html_email_to_user(html_string, email_addresses.email_addresses_by_hash[user['addr_hash']])
