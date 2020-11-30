#!/usr/bin/env python3
"""
Flask application
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    ''' flask app Config class. '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages. """
    locale = request.args.get('locale')
    if locale is not None and locale in app.config['LANGUAGES']:
        return locale
    locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    return locale


app.config.from_object('6-app.Config')


def get_user():
    ''' Returns a user dictionary or None, if the user doesn't exist. '''
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    ''' Handles request before making the request to the API. '''
    user = get_user()
    g.user = user


@app.route('/')
def default():
    """ Returns a 6-index.html template """
    return render_template('6-index.html')
