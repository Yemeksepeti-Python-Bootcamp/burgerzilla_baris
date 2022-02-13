from flask_restx import Api
from flask import Blueprint
from .controller import api as auth_namespace

auth_blueprint = Blueprint('auth', __name__)
auth = Api(auth_blueprint, title='Application Auth', version='1.0')

auth.add_namespace(auth_namespace)

