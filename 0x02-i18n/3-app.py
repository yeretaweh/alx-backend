#!/usr/bin/env python3
"""
Flask app for i18n demo with user login simulation.

Configures Flask-Babel for language localization.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['LANGUAGES'] = ['en', 'fr']

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Selects the best match for supported languages
    using request.accept_languages.

    Returns:
        The best match for supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Returns the rendered 3-index.html template as a str.

    Returns:
        str: The rendered 3-index.html template.
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
