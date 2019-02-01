import json
import datetime

from flask_restful import reqparse, Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

from ..models.user_model import User
from app.db import get_db

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('email', help='email argument is required')
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
        new_user.signup()

        db = get_db()
        cur = db.cursor()
        cur.execute(
            "INSERT INTO users (id, email, username, password) VALUES (%s, %s, %s, %s)"
            , (new_user.id, new_user.email, new_user.username, new_user.password))
        db.commit()
        return {"New user created": new_user.__dict__}

    @jwt_required
    def get(self):
        many = User.get_all()
        return many

class UserLogin(Resource):
    '''Login class for authentictating a user and assigning access tokens'''
    def post(self):
        args = parser.parse_args()
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