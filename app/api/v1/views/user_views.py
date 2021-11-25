import json
import datetime

from flask_restful import reqparse, Resource
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from ..models.user_model import User
from app.db import get_db
from app.extensions import jwt

blacklist = set()

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('email', required=True, help='email argument is required')
parser.add_argument('username', required=True, help='username argument is required')
parser.add_argument('password', required=True, help='password argument is required')

parser_2 = parser.copy()
parser_2.remove_argument('email')

class UserRegistration(Resource):
    '''User Regisrtration class'''
    def post(self):
        args = parser.parse_args()
        email = args['email']
        username = args['username']
        password = args['password']

        new_user = User(email, username, password)
        new_user.signup()

        # db = get_db()
        # cur = db.cursor()
        # cur.execute(
        #     "INSERT INTO users (id, email, username, password) VALUES (%s, %s, %s, %s)"
        #     , (new_user.id, new_user.email, new_user.username, new_user.password))
        # db.commit()
        return {"New user created": new_user.__dict__}, 201

    @jwt_required
    def get(self):
        many = User.get_all()
        return many

class UserLogin(Resource):
    '''Login class for authentictating a user and assigning access tokens'''
    def post(self):
        args = parser_2.parse_args()
        username = args['username']
        password = args['password']

        user = User.get_one(username)

        if not user:
            return {'message': 'No such user'}, 401

        if user and user["password"] != password:
            return {"message": "password Incorrect"}

        expiration = datetime.timedelta(minutes=20)
        access_token = create_access_token(identity=username, expires_delta=expiration)
        return {'message': 'Logged in successfully!', 'token': access_token}, 200

class Logout(Resource):
    '''Logout class for login out users by revoking their access tokens'''
    @jwt_required
    def get(self):
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
        return {'message': 'logged out successfully'}