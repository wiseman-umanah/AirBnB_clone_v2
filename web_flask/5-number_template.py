#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape
from flask import render_template


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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_fun(text="is cool"):
    """Function to return HBNB with Flask"""
    text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Function to return HBNB with Flask"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_tem(n):
    """Function to print number template"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
