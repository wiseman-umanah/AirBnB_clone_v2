#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Function to return Hello Hbnb with Flask"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function to return HBNB with Flask"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    """Function to return HBNB with Flask"""
    text = text.replace("_", " ")
    return f"C {escape(text)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
