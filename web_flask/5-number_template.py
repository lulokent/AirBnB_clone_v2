#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
from flask import render_template
w_app = Flask(__name__)


@w_app.route('/', strict_slashes=False)
def landing_page():
    """ Displays greeting on the home page"""
    return "Hello HBNB!"


@w_app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays greeting"""
    return "HBNB"


@w_app.route("/c/<text>", strict_slashes=False)
def c_with_text(text):
    """ formated text returned as a string"""
    return 'C ' + text.replace('_', ' ')


@w_app.route('/python/', defaults={'text': 'is_cool'})
@w_app.route('/python/<text>')
def python_text_params(text):
    """ Displays python followed by value of text """
    return "Python " + text.replace("_", " ")


@w_app.route('/number/<int:n>')
def number(n):
    """ returns 'n is a number' is n is integer """
    return "{} is a number".format(n)


@w_app.route('/number_template/<int:n>')
def number_template(n):
    """ returns an html page if n is an integer """
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    w_app.run(host='0.0.0.0', port=5000)
