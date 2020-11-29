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
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('2-app.Config')


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages. """
    requested_lang = request.accept_languages.best_match(app.config.LANGUAGES)
    return requested_lang


@app.route('/')
def default():
    """ Returns a 2-index.html template """
    return render_template('2-index.html')
