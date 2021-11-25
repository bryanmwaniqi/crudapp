from flask import Blueprint
from flask_restful import Api

from .views.products import AllProducts
from .views.user_views import UserRegistration, UserLogin, Logout

version1 = Blueprint('api_version_1', __name__, url_prefix='/crudapp/api/v1')

api = Api(version1)

api.add_resource(AllProducts, '/products')
api.add_resource(UserRegistration, '/signup')
api.add_resource(UserLogin, '/login')
api.add_resource(Logout, '/logout')