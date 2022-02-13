import json
from utils.common import register_user, login_user
from utils.base import BaseTestCase

class TestCustomerLoginRegisterAuth(BaseTestCase):
    def test_LoginRegister_When_User_Is_Customer(self):
        # Test for user registration
        data = dict(
        email='test@customer.com',
        username='test_customer',
        name='Test',
        surname = 'customer',
        address = 'Customer address',
        password='123456789',
        )

        register_response = register_user(self, data)
        register_data = json.loads(register_response.data.decode())

        self.assertEquals(register_response.status_code, 200)
        self.assertTrue(register_response.status)
        self.assertEquals(register_data["user"]["email"], data['email'])

        # Test for restaurant login
        login_response = login_user(self, data['email'], data['password'])
        login_data = json.loads(login_response.data.decode())

        self.assertEquals(login_response.status_code, 200)
        self.assertTrue(login_response.status)
        self.assertEquals(login_data["user"]["email"], data['email'])


