#!/usr/bin/env python3
""" module 5-app.py """
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ config class for Babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ gets best match for locales """
    if 'locale' in request.args and request.args.get(
            'locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ returns a user dict of user data"""
    userId = request.args.get('login_as')
    try:
        return users[int(userId)]
    except (KeyError, ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """ find a user if any"""
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index() -> str:
    """ Basic Flask App """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
