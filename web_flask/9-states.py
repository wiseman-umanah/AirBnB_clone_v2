#!/usr/bin/python3
"""Flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states/<id>", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def display_states(id=""):
    states = storage.all(State)
    if id != "":
        id = f"State.{id}"
    return render_template("9-states.html", states=states, id=id)


@app.teardown_appcontext
def display_states_close(error):
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
