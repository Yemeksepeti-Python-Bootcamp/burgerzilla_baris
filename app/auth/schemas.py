from marshmallow import Schema, fields
from marshmallow.validate import Length, Regexp

class LoginSchema(Schema):
    """
    Schema for login data
    /auth/login [POST]

    Parameters:
    - email: string
    - password: string
    
    """
    
    email = fields.Email(
        required=True,
        description="User email address", 
        validate = [Length(min=5, max=100)])

    password = fields.String(
        required=True, 
        description="User password", 
        validate=[Length(min=8, max=128)])

class RegisterSchemaForUser(Schema):
    """
    Schema for register data
    /auth/register [POST]

    Parameters:
    - email: string
    - username: string
    - name: string
    - password: string
    
    """
    
    email = fields.Email(
        required=True,
        description="User email address", 
        validate = [
            Length(min=5, max=100), 
            Regexp(regex=r'^[^@]+@[^@]+\.[^@]+$')
            ]
        )

    username = fields.String(
        required=True, 
        description="User username", 
        validate=[Length(min=5, max=100)])

    name = fields.String(
        required=True, 
        description="User name", 
        validate=[Length(min=2, max=100)])
    
    surname = fields.String(
        required=True,
        description="User surname",
        validate=[Length(min=2, max=100)])

    password = fields.String(
        required=True, 
        description="User password", 
        validate=[Length(min=8, max=128)])

    address = fields.String(
        required=True, 
        description="User address", 
        validate=[Length(min=2, max=250)])
    
class RegisterSchemaForRestaurant(Schema):

    email = fields.Email(
        required=True,
        description="Restaurant email address", 
        validate = [
            Length(min=5, max=100), 
            Regexp(regex=r'^[^@]+@[^@]+\.[^@]+$')
            ]
        )

    restaurant_name = fields.String(
        required=True, 
        description="restaurant_name", 
        validate=[Length(min=5, max=100)])

    owner_name = fields.String(
        required=True, 
        description="owner_name ", 
        validate=[Length(min=2, max=100)])
    
    owner_surname = fields.String(
        required=True,
        description="owner_name",
        validate=[Length(min=2, max=100)])

    address = fields.String(
        required=True,
        description="restaurant address",
        validate=[Length(min=10, max=500)])

    password = fields.String(
        required=True, 
        description="User password", 
        validate=[Length(min=8, max=128)])
    
