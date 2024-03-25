#!/usr/bin/python3
"""Flask web app to web browser"""
from flask import Flask, render_template
from models import storage
from models.state import State
# from models.amenity import Amenity
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def display():
    """Prints all states in dbms"""
    states = storage.all(State)
    #amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states) #amenities=amenities)


@app.teardown_appcontext
def display_states_close(error):
    """Closes each query session"""
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
