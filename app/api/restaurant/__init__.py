from flask_restx import Api
from flask import Blueprint
from app.api.restaurant.controller import api as restaurant_namespace

restaurant_blueprint = Blueprint('restaurant', __name__)
restaurant = Api(restaurant_blueprint, title='Application Restaurant', version='1.0')

restaurant.add_namespace(restaurant_namespace)

