#!/usr/bin/env python3
"""
Flask application
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


class Config:
    ''' flask app Config class. '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('3-app.Config')


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages. """
    requested_lang = request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def default():
    """ Returns a 3-index.html template """
    home_title = gettext('home_title')
    home_header = gettext('home_header')
    return render_template(
        '3-index.html',
        home_title=home_title,
        home_header=home_header
    )
