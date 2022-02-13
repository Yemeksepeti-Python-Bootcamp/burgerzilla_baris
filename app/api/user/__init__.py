from flask_restx import Api
from flask import Blueprint
from app.api.user.controller import api as user_namespace

user_blueprint = Blueprint('user', __name__)
user = Api(user_blueprint, title='Application User', version='1.0')

user.add_namespace(user_namespace)

