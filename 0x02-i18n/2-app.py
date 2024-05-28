#!/usr/bin/env python3
"""ALX Backend - il8n Module"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Babel configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Return the best match"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render 2-index.html"""
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run()
