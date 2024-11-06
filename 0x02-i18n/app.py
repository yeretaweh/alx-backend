#!/usr/bin/env python3
""" Flask app to demonstrate i18n with user login simulation. """

from flask import Flask, request, g, render_template
from flask_babel import Babel, _, format_datetime
from pytz import timezone, exceptions
from datetime import datetime
import pytz
from typing import Optional

app = Flask(__name__)
babel = Babel(app)

# Mock database of users
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[dict]:
    """
    Returns a user dictionary if the user ID is found in the mock database.
    The user ID is passed via the 'login_as' URL parameter.

    Returns:
        Optional[dict]: A dictionary containing user info
        or None if the ID is not found.
    """
    login_as = request.args.get('login_as')
    if login_as:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request() -> None:
    """
    Function to be executed before each request. It sets the user
    as a global variable `g.user` if the 'login_as' parameter is passed.
    """
    g.user = get_user()


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determines the time zone based on the URL parameters, user settings,
    or defaults to 'UTC' if no valid time zone is found.

    Returns:
        str: The user's time zone or 'UTC' as a default.
    """
    # Check if timezone is passed as a URL parameter
    tz_param = request.args.get('timezone')
    if tz_param:
        try:
            return timezone(tz_param).zone
        except exceptions.UnknownTimeZoneError:
            pass

    # Check if timezone is set in user settings
    if g.user and g.user.get('timezone'):
        try:
            return timezone(g.user['timezone']).zone
        except exceptions.UnknownTimeZoneError:
            pass

    # Default to UTC
    return 'UTC'


@app.route('/')
def index() -> str:
    """
    Renders the home page, displaying a welcome message and the current time
    based on the user's time zone.

    Returns:
        str: Rendered HTML template for the index page.
    """
    # Get the current time in the user's inferred time zone
    current_tz = pytz.timezone(get_timezone())
    current_time = datetime.now(current_tz)

    # Format the current time based on the locale
    formatted_time = format_datetime(current_time)

    # Render the template with the formatted time
    return render_template('index.html', current_time=formatted_time)


if __name__ == "__main__":
    app.run(debug=True)
