from flask import Flask, Blueprint

def create_app(config_filename):
    app = Flask(__name__,)
    app.config.from_object('config.TestingConfig')

    from .api.v1 import version1 
    app.register_blueprint(version1)

    return app