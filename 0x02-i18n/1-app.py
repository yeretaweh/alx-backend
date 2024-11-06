#!/usr/bin/env python3
"""
Flask app with Babel integration for i18n.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class for Babel setup.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

# Instantiate Babel
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Returns the rendered index.html template.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
