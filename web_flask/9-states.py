#!/usr/bin/python3
"""
starts a Flask web application.
"""

from flask import Flask, render_template
from models import *
from models import storage
w_app = Flask(__name__)


@w_app.route('/states',strict_slashes=False)
@w_app.route('/states/,state_id>',strict_slashes=False)
def states(state_id=None):
    """ Displays the states and cities listed in Alphabetical order."""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html',states=states, state_id=state_id)

@w_app.teardown_appcontext
def teardown_db(exception):
    """ Closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    w_app.run(host='0.0.0.0', port=5000)
