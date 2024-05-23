#!/usr/bin/python3
""" Start web application with flask """

from flask import Flask, render_template
from models import storage
from models.state import State

w_app = Flask(__name__)


@w_app.route('/cities_by_states', strict_slashes=False)
def list_of_states():
    """ Returns list of states """
    state_list = storage.all(State)
    return render_template("8-cities_by_states.html", states=state_list)


@w_app.teardown_appcontext
def teardown(arg=None):
    """ closes session"""
    storage.close()


if __name__ == "__main__":
    w_app.run(host="0.0.0.0", port=5000)
