#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
w_app = Flask(__name__)


@w_app.route('/', strict_slashes=False)
def landing_page():
    """ Displays greeting on home page."""
    return "Hello HBNB!"


@w_app.route('/hbnb', strict_slashes=False)
def flask_greeting2():
    """ Displays a greeting"""
    return "HBNB"


@w_app.route("/c/<text>", strict_slashes=False)
def c_with_text(text):
    """ Displays C followed by a string."""
    return 'C ' + text.replace('_', ' ')


@w_app.route('/python/', defaults={'text':'is_cool'})
@w_app.route('/python/<text>')
def python_text_params(text):
    """ Displays python followed by value of text """
    return "Python " + text.replace("_", " ")


@w_app.route('/number/<int:n>')
def num_display(n):
    """ returns 'n is a number' is n is integer """
    return "{} is a number".format(n)


if __name__ == "__main__":
    w_app.run(host='0.0.0.0', port=5000)
