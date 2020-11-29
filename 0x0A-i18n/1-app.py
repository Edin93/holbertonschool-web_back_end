#!/usr/bin/env python3
"""
Flask application
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


class Config:
    ''' Language Config class. '''
    LANGUAGES = ["en", "fr"]

    @babel.localeselector
    def get_locale():
        """ Returns requested language. """
        requested_lang = request.args.get('lang')
        if not requested_lang:
            return 'en'

    @babel.timezoneselector
    def get_timezone():
        """ Returns requested timezone. """
        requested_tz = request.args.get('timezone')
        if not requested_tz:
            return 'UTC'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
