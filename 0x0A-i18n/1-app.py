#!/usr/bin/env python3
"""
Flask application
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    ''' flask app Config class. '''
    LANGUAGES = ["en", "fr"]
    default_locale = 'en'
    default_timezone = 'UTC'


# babel._default_locale = Config.default_locale
# babel._default_timezone = Config.default_timezone
app.config.from_object('1-app.Config')


@app.route('/')
def default():
    """ Returns a 1-index.html template """
    return render_template('1-index.html')
