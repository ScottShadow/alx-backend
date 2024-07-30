#!/usr/bin/env python3
"""
Get locale from request
"""


from flask import Flask, render_template, request, flash, g
from flask_babel import Babel, _, lazy_gettext as _l, gettext


class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """
     determine the best match with our supported languages.
    """
    locale = request.args.get('locale')
    print('locale', locale)
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    # return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


def get_user(login_as):
    """
    Get user
    """
    try:
        login_as = int(login_as)
        return users.get(login_as)
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """
    Before request
    """
    g.user = get_user(request.args.get("login_as"))
    g.locale = get_locale()
    print(g.user)


@app.route('/', methods=['GET'], strict_slashes=False)
def login():
    """
    Hello world
    """
    return render_template("5-index.html", get_locale=get_locale)


if __name__ == '__main__':
    app.run(debug=True)
