#!/usr/bin/env python3
"""
Get locale from request
"""


from flask import Flask, render_template, request, flash
from flask_babel import Babel, _, lazy_gettext as _l, gettext


class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """
     determine the best match with our supported languages.
    """
    return 'fr'
    # return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Hello world
    """
    return render_template("4-index.html", get_locale=get_locale)


if __name__ == '__main__':
    app.run(debug=True)
