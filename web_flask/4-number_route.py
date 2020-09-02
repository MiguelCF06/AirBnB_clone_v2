#!/usr/bin/python3
"""
Starts a Flask Web Application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Returns hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Return C  followed by the value of the text variable"""
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """Return Python followed by the value of the text variable"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def num_route(n):
    """Return n is a number if n is an integer"""
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
