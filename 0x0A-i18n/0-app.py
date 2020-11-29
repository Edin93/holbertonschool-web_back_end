#!/usr/bin/env python3
"""
Flask application.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def default():
    """ Returns a 0-index.html template. """
    return render_template("0-index.html")
