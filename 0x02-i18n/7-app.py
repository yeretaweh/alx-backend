#!/usr/bin/env python3
"""Flask Babel setup for language localization."""

from flask import Flask, request, g, render_template
from flask_babel import Babel, _
from pytz import timezone, exceptions

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """
    Before each request, set g.user to the user corresponding to the
    login_as parameter in the request, or None if no such parameter exists.
    """
    login_as = request.args.get('login_as')
    if login_as:
        user = users.get(int(login_as))
        g.user = user
    else:
        g.user = None


@babel.timezoneselector
def get_timezone():
    """
    Selects the best match for supported timezones
    using request URL parameter and user settings.

    Returns:
        The best match for supported timezones.
    """
    # Check URL parameters
    tz_param = request.args.get('timezone')
    if tz_param:
        try:
            return timezone(tz_param).zone
        except exceptions.UnknownTimeZoneError:
            pass

    # Check user settings
    if g.user and g.user.get('timezone'):
        try:
            return timezone(g.user['timezone']).zone
        except exceptions.UnknownTimeZoneError:
            pass

    # Default to UTC
    return 'UTC'


@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        The rendered 7-index.html template.
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(debug=True)
