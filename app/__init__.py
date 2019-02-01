from flask import Flask, Blueprint


def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.TestingConfig')
    app.config.from_pyfile('config.py')

    from .api.v1 import jwt
    jwt.init_app(app)

    # Register db with the app
    from app import db
    db.init_app(app)

    from .api.v1 import version1 
    app.register_blueprint(version1)

    return app