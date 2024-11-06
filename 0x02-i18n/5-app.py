#!/usr/bin/env python3
"""
Flask app to demonstrate i18n with user login simulation.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

# Mock users "database"
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Babel configuration


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

# Define the get_user function


def get_user():
    login_as = request.args.get('login_as')
    if login_as:
        try:
            user_id = int(login_as)
            return users.get(user_id)
        except (ValueError, TypeError):
            return None
    return None

# Before request function


@app.before_request
def before_request():
    g.user = get_user()

# Locale selector for Babel


@babel.localeselector
def get_locale():
    # If user is logged in, use their locale
    if g.user and g.user.get("locale") in app.config['LANGUAGES']:
        return g.user["locale"]
    # Else, use the request or default behavior
    return request.args.get('locale', request.accept_languages.best_match(
        app.config['LANGUAGES']))


@app.route('/')
def index():
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
