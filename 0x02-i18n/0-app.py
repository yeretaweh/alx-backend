#!/usr/bin/env python3
"""A simple Flask app to demonstrate i18n."""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Returns the rendered index.html template"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
