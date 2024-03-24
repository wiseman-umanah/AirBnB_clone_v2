#!/usr/bin/python3
"""Flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def display_states_close(error):
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
