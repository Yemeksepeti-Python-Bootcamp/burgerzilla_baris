from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request

from .service import UserService
from .dto import UserDTO

api = UserDTO.api
data_response = UserDTO.data_response

@api.route('/order/<int:restaurant_id>')
class CreateOrder(Resource):
    @api.doc('Create order',responses={200: ("Success", data_response), 404: 'Order Not Found' })
    @jwt_required()
    def post(self, restaurant_id):
        """
        This method is used to create an order.
        """
        order_data = request.get_json()

        current_user_info = get_jwt_identity()
        user_id = current_user_info['id']

        return UserService.createOrder(user_id, restaurant_id, order_data)

@api.route('/orders/<int:order_id>')
class GetOrderById(Resource):
    @api.doc('Get order by id',responses={200: ("Success", data_response), 404: 'Order Not Found' })
    @jwt_required()
    def get(self, order_id):
        """
        This method is used to get an order by id.
        """
        current_user_info = get_jwt_identity()
        user_id = current_user_info['id']

        return UserService.getOrderById(order_id, user_id)


@api.route('/orders')
class GetOrders(Resource):
    @api.doc('Get all orders belonging user',responses={200: ("Success", data_response), 404: 'Order Not Found' })
    @jwt_required()
    def get(self):
        """Get all orders belonging user"""
        current_user_info = get_jwt_identity()
        user_id = current_user_info["id"]

        return UserService.get_orders(user_id)

@api.route('/order/<int:order_id>')
class CancelOrder(Resource):
    @api.doc('Cancel order',responses={200: ("Success", data_response), 404: 'Order Not Found' })
    @jwt_required()
    def put(self, order_id):
        """Cancel order"""
        current_user_info = get_jwt_identity()
        user_id = current_user_info["id"]

        return UserService.cancel_order(user_id, order_id)

@api.route('/orders/active_orders')
class GetActiveOrders(Resource):
    @api.doc('Get all active orders belonging user',responses={200: ("Success", data_response), 404: 'Order Not Found' })
    @jwt_required()
    def get(self):
        """Get all active orders belonging user"""
        current_user_info = get_jwt_identity()
        user_id = current_user_info["id"]

        return UserService.get_active_orders(user_id)

@api.route('/restaurants')
class GetRestaurants(Resource):
    @api.doc('Get all restaurants',responses={200: ("Success", data_response), 404: 'Restaurant Not Found' })
    @jwt_required()
    def get(self):
        """Get all restaurants that exist in the system"""
        return UserService.get_all_restaurants()

@api.route('/restaurant/<int:restaurant_id>')
class GetSpecificRestaurant(Resource):
    @api.doc('Get specific restaurant',responses={200: ("Success", data_response), 404: 'Restaurant Not Found' })
    @jwt_required()
    def get(self, restaurant_id):
        """Get specific restaurant by their restaurant id in the system"""
        return UserService.get_restaurant_by_id(restaurant_id)