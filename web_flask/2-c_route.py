#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
w_app = Flask(__name__)


@w_app.route('/', strict_slashes=False)
def landing_page():
    """ Display greeting on the home page."""
    return "Hello HBNB!"


@w_app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display greeting"""
    return "HBNB"


@w_app.route("/c/<text>", strict_slashes=False)
def c_with_text(text):
    """ Displays C followed by a string."""
    return 'C ' + text.replace('_', ' ')


if __name__ == "__main__":
    w_app.run(host='0.0.0.0', port=5000)
