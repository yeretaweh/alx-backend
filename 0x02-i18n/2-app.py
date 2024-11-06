#!/usr/bin/env python3
"""
Flask app with Babel locale selector.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Config class for Babel setup.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

# Instantiate Babel as module-level variable
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Selects the best match for supported languages
    using request.accept_languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Returns the rendered index.html template.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
