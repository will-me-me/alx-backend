#!/usr/bin/env python3
"""ALX SE Backend - i18N"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config(object):
    """Babel Configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Return the best locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render 1-index.html"""
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run(debug=True)
