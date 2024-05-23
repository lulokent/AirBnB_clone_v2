#!/usr/bin/python3
""" Starts a Flask web application
    Listens on 0.0.0.0, port 5000
"""
from flask import Flask
w_app = Flask(__name__)


@w_app.route('/', strict_slashes=False)
def Landing_pg():
    """ Displays greeting 'Hello HBNB'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    w_app.run(host="0.0.0.0", port=5000)
