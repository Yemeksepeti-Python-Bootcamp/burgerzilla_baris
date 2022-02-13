from flask import request
from flask_restx import Resource
from ..utils.messages.error_message_response import ErrorMessages

from .service import AuthService
from .dto import AuthDTO
from .schemas import LoginSchema, RegisterSchemaForUser, RegisterSchemaForRestaurant

api = AuthDTO.api
auth_success = AuthDTO.auth_success_data

login_schema = LoginSchema()
register_user_schema = RegisterSchemaForUser()
register_restaurant_schema = RegisterSchemaForRestaurant()

error_messages = ErrorMessages()
auth_service = AuthService()

@api.route('/user_login')
class UserLogin(Resource):
    """
    User Login

    """

    auth_login = AuthDTO.auth_login_data # get login data from dto
    @api.doc('Auth Login', responses = {200: 'Success', 400: 'Validation Error', 404: 'User Not Found', 500: 'Internal Server Error'}) # set doc
    @api.expect(auth_login, validate=True) # set expect
    def post(self): 
        """
        User Login
        """
        login_data = request.get_json() # get login data from request
        
        if(errors := login_schema.validate(login_data)): # if errors
            return error_messages.validation_error(False, errors), 400 # return error response
        
        return auth_service.user_login(login_data) # return response

@api.route('/restaurant_login')
class RestaurantLogin(Resource):
    """
    Restaurant Login

    """

    auth_login = AuthDTO.auth_login_data # get login data from dto
    @api.doc('Auth Login', responses = {200: 'Success', 400: 'Validation Error', 404: 'User Not Found', 500: 'Internal Server Error'}) # set doc
    @api.expect(auth_login, validate=True) # set expect
    def post(self): 
        """
        User Login
        """
        login_data = request.get_json() # get login data from request
        
        if(errors := login_schema.validate(login_data)): # if errors
            return error_messages.validation_error(False, errors), 400 # return error response
        
        return auth_service.restaurant_login(login_data)

@api.route('/user_register')
class UserRegister(Resource):
    """
    User Register

    """
    auth_register = AuthDTO.auth_user_register_data
    @api.doc('Auth Register', responses = {200: 'Success', 400: 'Validation Error', 500: 'Internal Server Error'})
    @api.expect(auth_register, validate=True)
    def post(self):
        register_data = request.get_json()

        if(errors := register_user_schema.validate(register_data)):
            return error_messages.validation_error(False, errors), 400
        return auth_service.user_register(register_data)

@api.route('/restaurant_register')
class RestaurantRegister(Resource):
    """
    User Register

    """
    auth_register = AuthDTO.auth_restaurant_register_data
    @api.doc('Auth Register', responses = {200: 'Success', 400: 'Validation Error', 500: 'Internal Server Error'})
    @api.expect(auth_register, validate=True)
    def post(self):
        register_data = request.get_json()

        if(errors := register_restaurant_schema.validate(register_data)):
            return error_messages.validation_error(False, errors), 400
        return auth_service.restaurant_register(register_data)


# @api.route('/user_logout')
# class UserLogout(Resource):
#     """
#     User Logout

#     """
#     @api.doc('Auth Logout', responses = {200: 'Success', 500: 'Internal Server Error'})
#     def post(self):
#         return auth_service.user_logout()


    