#!/usr/bin/python3
"""
Start a Flask Web App
"""

from flask import Flask
from flask import render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_app(exception):
    """Closes the storage when a teardown ocurred"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
