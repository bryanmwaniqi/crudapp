import unittest
import os

from app import create_app
# from app.api.v1.models.user_model import User

class BaseTestEndpoints(unittest.TestCase):

    def setup(self):
        '''Initialize app and the Test client'''
        self.app = create_app(os.getenv('APP_SETTINGS'))
        self.client = self.app.test_client
        self.test_user_data = {"email": "test@gmail.com", "username": "test-user", "password": "testpassword" }
        self.headers = {'Content-Type': 'application/json'}

    def test_signup_post(self):
        test_data = {"email": "vim@vimac.com", "username": "test-user", "password": "testpassword" }
        rv = self.client().post('/crudapp/api/v1/signup', json=test_data, headers=self.headers)
        self.assertEqual(resp_object.status_code, 201)
        self.assertDictEqual(resp_object.get_json(), {"New user created": test_data.update(id=2)}, 
                            msg='the user dict posted should be the same user dict returned updated with an id')