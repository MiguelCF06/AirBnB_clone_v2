#!/usr/bin/python3
"""
Starts a Flask Web Application
"""

from flask import Flask
from flask import render_template
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
    """Return n is a number only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_route(n):
    """Return an html template only if n is a number"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """Return an html template only if n is a number and display if it is odd
or even"""
    if n % 2 == 0:
        what_is = "even"
    else:
        what_is = "odd"
    return render_template("6-number_odd_or_even.html", n=n,
                           what_is=what_is)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
