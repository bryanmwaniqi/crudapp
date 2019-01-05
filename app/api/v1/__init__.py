from flask import Blueprint
from flask_restful import Api

version1 = Blueprint('api_version-1', __name__)

api = Api(version1)


