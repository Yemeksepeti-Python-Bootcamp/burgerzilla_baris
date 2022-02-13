import json
from utils.common import login_restaurant, register_restaurant
from utils.base import BaseTestCase

class TestRestaurantLoginRegisterAuth(BaseTestCase):
    def test_LoginRegister_When_User_Is_Restaurant(self):
        # Test for user registration
        data = dict(
        email='test@restaurant.com',
        restaurant_name='test_restaurant',
        owner_name='Test',
        owner_surname = 'Restaurant',
        address = 'Test address',
        password='123456789',
        )

        register_response = register_restaurant(self, data)
        register_data = json.loads(register_response.data.decode())

        self.assertEquals(register_response.status_code, 200)
        self.assertTrue(register_response.status)
        self.assertEquals(register_data["restaurant"]["email"], data['email'])

        # Test for restaurant login
        login_response = login_restaurant(self, data['email'], data['password'])
        login_data = json.loads(login_response.data.decode())

        self.assertEquals(login_response.status_code, 200)
        self.assertTrue(login_response.status)
        self.assertEquals(login_data["restaurant"]["email"], data['email'])


