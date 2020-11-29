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


cfg = Config()
app.config.from_object(cfg)
babel.default_locale = cfg.default_locale
babel.default_timezone = cfg.default_timezone
