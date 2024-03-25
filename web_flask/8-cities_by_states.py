#!/usr/bin/python3
"""Module to starts flask with name of states and cities"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/cities_by_state", strict_slashes=False)
def display_states_cities():
    """Returns cities by states for web"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def display_states_close(error):
    """Closes session of program"""
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
