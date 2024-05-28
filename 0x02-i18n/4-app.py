#!/usr/bin/env python3
"""ALX SE Backend - i18N"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Babel configurations"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Return the best match of locale to use"""
    locale = request.query_string.decode()
    if locale:
        return locale.split('=')[-1]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render 4-index.html"""
    return render_template("4-index.html")


if __name__ == '__main__':
    app.run()
