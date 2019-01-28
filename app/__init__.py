from flask import Flask, Blueprint
from flask_jwt import JWT

jwt = JWT()

def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.TestingConfig')
    app.config.from_pyfile('config.py')

    from app.api.v1.utils.auth_handler import authenticate, identity 
    jwt = JWT(app, authenticate, identity)

    from .api.v1 import version1 
    app.register_blueprint(version1)

    return app