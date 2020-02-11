from flask import Flask, Blueprint


def create_app(config_filename):
    '''create an instance of the Flask application'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.BaseConfig')
    app.config.from_pyfile('config.py')

    # Register db with the app
    from app import db
    db.init_app(app)

    #Register the jwt extension instance with the app
    from app.extensions import jwt
    jwt.init_app(app)

    #Register the api blueprint with app
    from .api.v1 import version1
    app.register_blueprint(version1)
    
    return app