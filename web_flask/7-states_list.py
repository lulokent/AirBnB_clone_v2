#!/usr/bin/python3
""" Starts a web flask app """
from flask import Flask, render_template
from models.state import State
from models import storage
w_app = Flask(__name__)


@w_app.route("/states_list", strict_slashes=False)
def states_list():
    """ loads template states"""
    state_list = storage.all(State)
    return render_template("7-states_list.html", states=state_list)


@w_app.teardown_appcontext
def teardown(arg=None):
    """ Close current session"""
    storage.close()


if __name__ == "__main__":
    w_app.run(host="0.0.0.0", port=5000)
