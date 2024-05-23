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
    """ Displays greeting."""
    return "HBNB"


if __name__ == "__main__":
    web_app.run(host='0.0.0.0', port=5000)
