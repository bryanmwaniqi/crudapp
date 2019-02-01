# import json

# from ..models.user_model import User

# def authenticate(username, password):
#     user = User.all_users.get(username, None)
#     if user and password == user["password"]:
#         return user

# def identity(payload):
#     user_id = payload['identity']
#     for user in User.all_users.keys():
#         if user['id'] == user_id:
#             return user