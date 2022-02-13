from flask import current_app
from flask_jwt_extended import create_access_token

from app import db
from app.utils.messages.error_message_response import ErrorMessages
from app.utils.helpers.string_helper import StringHelper
from app.utils.messages.responses import Responses
from app.utils.messages.success_message_response import SuccessMessages

from app.models.user.user import User
from app.models.restaurant.restaurant import Restaurant
from app.models.user.user_schema import UserSchema
from app.models.restaurant.restaurant_schema import RestaurantSchema

user_schemas = UserSchema()
restaurant_schemas = RestaurantSchema()

error_messages = ErrorMessages()
success_messages = SuccessMessages()
string_helper = StringHelper()
responses = Responses()

class AuthService:
    @staticmethod
    def user_login(data):
        email = data.get('email') # get email from data
        password = data.get('password') # get password from data

        try:
            user = User.query.filter_by(email=email).first() # get user from db
            if user is None: # if user is None
                return error_messages.err_resp(string_helper.USER_NOT_FOUND, "email_404", 404) # return error response

            elif user and user.verify_password(password): # if user is not None and user password is correct
                user_data = user_schemas.dump(user) # get user data
                access_token = create_access_token(identity = user_data) # create access token

                response = responses.success_response(200, string_helper.SUCCESS_LOGIN) # create success response
                response["access_token"] = access_token # add access token to response
                response["user"] = user_data # add user data to response

                return response, 200 # return response

            return error_messages.err_resp(string_helper.INVALID_PASSWORD_OR_EMAIL, "password_or_email_invalid_401", 401) # return error response

        except Exception as e:
            current_app.logger.error(e)
            return error_messages.internal_err_resp() # return error response
            
    
    
    @staticmethod
    def restaurant_login(data):
        email = data.get('email') # get email from data
        password = data.get('password') # get password from data

        try:
            restaurant = Restaurant.query.filter_by(email=email).first() # get user from db
            if restaurant is None: # if user is None
                return error_messages.err_resp(string_helper.FAIL_RESTAURANT_FOUND, "email_404", 404) # return error response

            elif restaurant and restaurant.verify_password(password): # if user is not None and user password is correct
                restaurant_data = restaurant_schemas.dump(restaurant) # get user data
                access_token = create_access_token(identity = restaurant_data) # create access token
                response = success_messages.message(True, string_helper.SUCCESS_LOGIN) # create success response
                response["access_token"] = access_token # add access token to response
                response["restaurant"] = restaurant_data # add user data to response

                return response, 200 # return response

            return error_messages.err_resp(string_helper.INVALID_PASSWORD_OR_EMAIL, "password_or_email_invalid_401", 401) # return error response

        except Exception as e:
            current_app.logger.error(e)
            return error_messages.internal_err_resp() # return error response

    @staticmethod
    def user_register(data):
        email = data.get('email')
        username = data.get('username')
        name = data.get('name')
        surname = data.get('surname')
        password = data.get('password')
        address = data.get('address')


        if User.query.filter_by(email=email).first(): # get user from db
            return error_messages.err_resp(string_helper.EMAIL_ALREADY_EXISTS, "email_409", 409) # return error response

        elif User.query.filter_by(username=username).first(): # get user from db
            return error_messages.err_resp(string_helper.USERNAME_ALREADY_EXISTS, "username_409", 409) # return error response

        try:
            user = User(email=email, username=username, name=name, surname=surname, password=password, address = address) # create user
            db.session.add(user) # add user to db
            db.session.commit() # commit user to db

            user_data = user_schemas.dump(user) # get user data
            access_token = create_access_token(identity = user_data) # create access token

            response = success_messages.message(True, string_helper.SUCCESS_REGISTER) # create success response
            response["access_token"] = access_token # add access token to response
            response["user"] = user_data # add user data to response

            return response, 200 # return response
        
        except Exception as e:
            current_app.logger.error(e)
            return error_messages.internal_err_resp()
    
    @staticmethod
    def restaurant_register(data):
        email = data.get('email')
        restaurant_name = data.get('restaurant_name')
        owner_name = data.get('owner_name')
        owner_surname = data.get('owner_surname')
        address = data.get('address')
        password = data.get('password')


        if Restaurant.query.filter_by(email=email).first(): # get user from db
            return error_messages.err_resp(string_helper.EMAIL_ALREADY_EXISTS, "email_409", 409) # return error response

        elif Restaurant.query.filter_by(restaurant_name=restaurant_name).first(): # get user from db
            return error_messages.err_resp(string_helper.RESTAURANT_NAME_ALREADY_EXISTS, "username_409", 409) # return error response

        try:
            restaurant = Restaurant(
                email=email, 
                restaurant_name=restaurant_name, 
                owner_name=owner_name, 
                owner_surname=owner_surname, 
                address = address, 
                password=password) # create user

            db.session.add(restaurant) # add user to db
            db.session.commit() # commit user to db

            restaurant_data = restaurant_schemas.dump(restaurant) # get user data
            access_token = create_access_token(identity = restaurant_data) # create access token

            response = success_messages.message(True, string_helper.SUCCESS_REGISTER) # create success response
            response["access_token"] = access_token # add access token to response
            response["restaurant"] = restaurant_data # add user data to response

            return response, 200 # return response
        
        except Exception as e:
            current_app.logger.error(e)
            return error_messages.internal_err_resp()


            



