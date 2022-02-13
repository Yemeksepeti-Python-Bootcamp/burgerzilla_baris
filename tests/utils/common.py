import json

def register_user(self, data):
    register_info = {
        'email': data['email'],
        'username': data['username'],
        'name': data['name'],
        'surname': data['surname'],
        'address': data['address'],
        'password': data['password'],
    }
    return self.client.post(
        '/auth/user_register', 
        data=json.dumps(register_info), 
        content_type='application/json',)

def register_restaurant(self, data):
    register_info = {
        'email': data['email'],
        'restaurant_name': data['restaurant_name'],
        'owner_name': data['owner_name'],
        'owner_surname': data['owner_surname'],
        'address': data['address'],
        'password': data['password'],
    }
    return self.client.post(
        '/auth/restaurant_register', 
        data=json.dumps(register_info), 
        content_type='application/json',)

def login_user(self, email, password):
    return self.client.post(
        '/auth/user_login', 
        data=json.dumps({'email': email, 'password': password}), 
        content_type='application/json',)

def login_restaurant(self, email, password):
    return self.client.post(
        '/auth/restaurant_login', 
        data=json.dumps({'email': email, 'password': password}), 
        content_type='application/json',)