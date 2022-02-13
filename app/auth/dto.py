from flask_restx import Namespace, fields

class AuthDTO:
    api = Namespace('auth', description='authentication related operations')

    user_data = api.model('Auth User Object', {
        "username": fields.String,
        "name": fields.String,
        "surname": fields.String,
        "email": fields.String,
        "joined_date": fields.DateTime})
    
    restaurant_data = api.model('Auth Restaurant Object', {
        "id": fields.Integer,
        "restaurant_name": fields.String,
        'email': fields.String,
        'owner_name': fields.String,
        'owner_surname': fields.String,
        'address': fields.String,
        'joined_date': fields.DateTime
        })

    auth_login_data = api.model('Login Data', {
        "email": fields.String(required=True, description="User email address"),
        "password": fields.String(required=True, description="User password")
    })

    auth_user_register_data = api.model('Register Data', 
    { "email": fields.String(required=True, description="User email address"),
        "username": fields.String(required=True, description="User username"),
        "name": fields.String(required=True, description="User name"),
        "password": fields.String(required=True, description="User password"),
        "address": fields.String(required=True, description="User address"),
    })

    auth_restaurant_register_data = api.model('Register Data', 
    { "email": fields.String(required=True, description="User email address"),
        "restaurant_name": fields.String(required=True, description="Restaurant name"),
        "owner_name": fields.String(required=True, description="Restaurant owner name"),
        "owner_surname": fields.String(required=True, description="Restaurant owner surname"),
        "address": fields.String(required=True, description="Restaurant address"),
        "password": fields.String(required=True, description="Restaurant password")
    })

    auth_success_data = api.model('Auth Success Response', 
    {"status": fields.Boolean,
     "message": fields.String,
     "access_token": fields.String,
     "user": fields.Nested(user_data)
    })
       