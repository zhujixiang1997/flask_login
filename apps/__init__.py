from flask import Flask

from apps.account.views import account
from apps.ext import init_ext


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = '123456'
    init_ext(app)
    reigster(app)
    return app


def reigster(app:Flask):
    app.register_blueprint(account,url_prefix='/account')