import json

from flask_restful import reqparse, Resource
from flask_jwt import jwt_required
# from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, get_raw_jwt

from ..models.user_model import User

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('email', required=True, help='email argument is required')
parser.add_argument('username', required=True, help='username argument is required')
parser.add_argument('password', required=True, help='password argument is required')

class UserRegistration(Resource):
    '''User Regisrtration class'''
    def post(self):
        args = parser.parse_args()
        email = args['email']
        username = args['username']
        password = args['password']

        new_user = User(email, username, password)
        User.all_users[new_user.username] = new_user.__dict__
        return {"New user created": new_user.__dict__}

    @jwt_required
    def get(self):
        many = User.get_all()
        return User.all_users

class UserLogin(Resource):
    '''Login class for authentictating a user and assigning access tokens'''
    def post(self):
        args = parser.parse_args()
        email = args['email']
        password = args['password']

        if user and user["password"] != password:
            return {"message": "password Incorrect"}
        token = create_access_token(identity=email)
        return {'message': 'Logged in successfully!', 'token': token}, 201