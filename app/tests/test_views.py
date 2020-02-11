import unittest

from app import create_app
from app.api.v1.models.user_model import User

class TestEndpoints(unittest.TestCase):

    def setup(self):
        self.app = create_app("config.TestingConfig").test_client()
        test_user_data = {"email": "test@gmail.com", "username": "test-user", "password": "testpassword" }
        test_user = User(test_user_data['email'],test_user_data['username'],test_user_data['password'])
        test_user.signup()
        access_token = create_access_token(identity=test_user_data['username'], expires_delta=False)
        self.headers = {'Authorization': 'Bearer ' + access_token}

    def test_signup_post(self):
        test_data = {"email": "vim@vimac.com", "username": "test-user", "password": "testpassword" }
        resp_object = self.app.post('/crudapp/api/v1/signup', json=test_data, headers=self.headers)
        self.assertEqual(resp_object.status_code, 201)
        self.assertDictEqual(resp_object.get_json(), {"New user created": test_data.update(id=2)}, msg='the user dict posted should be the same user dict returned updated with an id')