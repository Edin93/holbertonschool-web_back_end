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
    ''' flask app Config class. '''
    LANGUAGES = ["en", "fr"]
    babel._default_locale = 'en'
    babel._default_timezone = 'UTC'
