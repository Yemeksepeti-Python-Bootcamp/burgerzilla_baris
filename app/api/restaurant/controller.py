from flask import  jsonify, request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.menu.menu import Menu
from app.models.product.product import Product

from app.models.restaurant.restaurant import Restaurant
from app.utils.helpers.string_helper import StringHelper
from app.utils.messages.responses import Responses
from .utils import isRestaurantUser, isRestaurantOwner

from .service import RestaurantService
from .dto import RestaurantDTO

api = RestaurantDTO.api
data_response = RestaurantDTO.data_response
restaurant_menu_response = RestaurantDTO.restaurant_menu_response
responses = Responses()
string_helper = StringHelper()


@api.route('/<int:id>')
class RestaurantGetById(Resource):

    @jwt_required()
    def get(self, id):
        """Get restaurant by id"""
        return RestaurantService.getRestaurantData(id)

# ------------------------------------------------------------
# ------------------ MENU OPERATIONS -------------------------
# ------------------------------------------------------------

@api.route('/menu')
class GetMenuByRestaurantId(Resource):
    @api.doc('Get Restaurant menu by id',responses={200: ("Success", restaurant_menu_response),404: 'Restaurant Not Found' },params={'restaurant_id': 'restaurant_id'})
    @jwt_required()
    def get(self):
        """Get Restaurant menu by id"""
        current_user_info = get_jwt_identity() # get current user info from jwt token
        restaurant = Restaurant.query.filter_by(id = current_user_info["id"]).first() # get restaurant info from db
        return RestaurantService.getMenuDetail(restaurant.id) 



@api.route('/menu')
class CreateMenu(Resource):
    @api.doc('Create new menu',responses={200: ("Success", data_response),404: 'Restaurant Not Found' })
    @jwt_required()
    def post(self):
        """Create new menu"""

        menu_data = request.get_json() # get data from request

        current_user_info = get_jwt_identity() # gets jwt the user info
        restaurant = Restaurant.query.filter_by(id = current_user_info["id"]).first() # gets restaurant by id

        if isRestaurantUser(current_user_info): # checks if the user is a restaurant user
            if isRestaurantOwner(current_user_info, restaurant): # checks if user is a restaurant owner
                return RestaurantService.createMenu(menu_data, restaurant.id)
            else:
                response = responses.error_response(401, string_helper.YOUR_ARE_NOT_OWNER_RESTAURANT)
                return response,401
        else:
            response = responses.error_response(401, string_helper.YOU_ARE_NOT_RESTAURANT_USER)
            return response,401


@api.route('/menu/<int:menu_id>')
class DeleteMenu(Resource):
    @api.doc('Delete menu',responses={200: ("Success", data_response),404: 'Restaurant Not Found' })
    @jwt_required()
    def delete(self, menu_id):
        """Delete menu"""
        current_user_info = get_jwt_identity() # get jwt user info 
        restaurant = Restaurant.query.filter_by(id = current_user_info["id"]).first() # get restaurant by id
        

        if isRestaurantUser(current_user_info): # checks if the user is a restaurant user
            if isRestaurantOwner(current_user_info, restaurant): # checks if user is a restaurant owner
                menu = Menu.query.filter_by(id = menu_id).first()  # gets menu by id
                if restaurant.id == menu.restaurant_id: # check if the menu belongs to the restaurant, if yes delete
                    return RestaurantService.deleteMenu(menu_id)
                else:
                    response = responses.error_response(401, string_helper.FAIL_PRODUCTS_FOUND)
                    return response,401
            else:
                response = responses.error_response(401, string_helper.YOUR_ARE_NOT_OWNER_RESTAURANT)
                return response,401
        else:
            response = responses.error_response(401, string_helper.YOU_ARE_NOT_RESTAURANT_USER)
            return response,401


@api.route('/menu/<int:menu_id>')
class UpdateMenu(Resource):
    @api.doc('Update menu',responses={200: ("Success", data_response),404: 'Restaurant Not Found' })
    @jwt_required()
    def put(self,  menu_id):
        """Update menu"""

        menu_data = request.get_json() # get data from request

        current_user_info = get_jwt_identity() # gets jwt the user info
        restaurant = Restaurant.query.filter_by(id = current_user_info["id"]).first() # gets restaurant by id


        if isRestaurantUser(current_user_info): # checks if the user is a restaurant user
            if isRestaurantOwner(current_user_info, restaurant): # checks if user is a restaurant owner
                return RestaurantService.updateMenu(menu_id, menu_data)
            else:
                response = responses.error_response(401, string_helper.YOUR_ARE_NOT_OWNER_RESTAURANT)
                return response,401
        else:
            response = responses.error_response(401, string_helper.YOU_ARE_NOT_RESTAURANT_USER)
            return response,401


# ------------------------------------------------------------
# ------------------ PRODUCT OPERATIONS ----------------------
# ------------------------------------------------------------

@api.route('/menu/add')
class AddProductToMenu(Resource):
    @api.doc('Add product to restaurant menu',responses={200: ("Success", data_response),404: 'Restaurant Not Found' })
    @jwt_required()
    def post(self):
        """Add product to restaurant menu"""

        current_user_info = get_jwt_identity() # gets jwt the user info
        restaurant = Restaurant.query.filter_by(id = current_user_info["id"]).first()
 

        if isRestaurantUser(current_user_info): # checks if the user is a restaurant user
            if isRestaurantOwner(current_user_info, restaurant): # checks if user is a restaurant owner
                product_data = request.get_json()
                return RestaurantService.addProductToMenu(product_data)
            else:
                response = responses.error_response(401, string_helper.YOUR_ARE_NOT_OWNER_RESTAURANT)
                return response,401
        else:
            response = responses.error_response(401, string_helper.YOU_ARE_NOT_RESTAURANT_USER)
            return response,401

@api.route('/product/<int:product_id>')
class UpdateProduct(Resource):
    @api.doc('Update product',responses={200: ("Success", data_response),404: 'Restaurant Not Found' })
    @jwt_required()
    def put(self,  product_id):
        product_data = request.get_json()

        current_user_info = get_jwt_identity() # gets jwt the user info
        restaurant = Restaurant.query.filter_by(id = current_user_info["id"]).first() # gets restaurant by id


        if isRestaurantUser(current_user_info): # checks if the user is a restaurant user
            if isRestaurantOwner(current_user_info, restaurant): # checks if user is a restaurant owner
                return RestaurantService.updateProduct(product_id, product_data)
            else:
                response = responses.error_response(401, string_helper.YOUR_ARE_NOT_OWNER_RESTAURANT)
                return response,401
        else:
            response = responses.error_response(401, string_helper.YOU_ARE_NOT_RESTAURANT_USER)
            return response,401


@api.route('/products/<int:product_id>')
class DeleteProduct(Resource):
    @api.doc('Delete product from restaurant menu',responses={200: ("Success", data_response),404: 'Restaurant Not Found' })
    @jwt_required()
    def delete(self, product_id):
        current_user_info = get_jwt_identity()
        restaurant = Restaurant.query.filter_by(id = current_user_info["id"]).first()
       

        if isRestaurantUser(current_user_info): # checks if the user is a restaurant user
            if isRestaurantOwner(current_user_info, restaurant): # checks if user is a restaurant owner
                product = Product.query.filter_by(id = product_id).first() # gets product by id
                menu = Menu.query.filter_by(id = product.menu_id).first()  # gets menu by id

                if restaurant.id == menu.restaurant_id: # check if the product belongs to the restaurant, if yes delete
                    return RestaurantService.deleteProduct(product_id)
                else:
                    response = responses.error_response(401, string_helper.FAIL_PRODUCTS_FOUND)
                    return response,401
            else:
                response = responses.error_response(401, string_helper.YOUR_ARE_NOT_OWNER_RESTAURANT)
                return response,401
        else:
            response = responses.error_response(401, string_helper.YOU_ARE_NOT_RESTAURANT_USER)
            return response,401

@api.route('/products')
class GetAllProducts(Resource):
    @api.doc('Get all products from restaurant menu',responses={200: ("Success", restaurant_menu_response),404: 'Restaurant Not Found' })
    @jwt_required()
    def get(self):
        current_user_info = get_jwt_identity()
        restaurant = Restaurant.query.filter_by(id = current_user_info["id"]).first()
        

        if isRestaurantUser(current_user_info): # checks if the user is a restaurant user
            return RestaurantService.getAllProducts(restaurant.id)
        else:
            response = responses.error_response(401, string_helper.YOU_ARE_NOT_RESTAURANT_USER)
            return response,401



# ------------------------------------------------------------
# ------------------ ORDER OPERATIONS ------------------------
# ------------------------------------------------------------

@api.route('/orders')
class GetAllOrders(Resource):
    @api.doc('Get all orders from restaurant',responses={200: ("Success", data_response),404: 'Restaurant Not Found' })
    @jwt_required()
    def get(self):
        current_user_info = get_jwt_identity()
        restaurant_id = current_user_info["id"]
        
        if isRestaurantUser(current_user_info):
            return RestaurantService.getAllOrders(restaurant_id)
        else:
            response = responses.error_response(401, string_helper.YOU_ARE_NOT_RESTAURANT_USER)
            return response,401

@api.route('/order/update/<int:order_id>')
class UpdateOrderStatus(Resource):
    @api.doc('Update order status',responses={200: ("Success", data_response),404: 'Restaurant Not Found' })
    @jwt_required()
    def put(self, order_id):
        current_user_info = get_jwt_identity()
        restaurant_id = current_user_info["id"]  

        if isRestaurantUser(current_user_info):
            return RestaurantService.updateOrderStatus(order_id, restaurant_id)
        else:
            response = responses.error_response(401, string_helper.YOU_ARE_NOT_RESTAURANT_USER)
            return response,401

@api.route('/order/cancel/<int:order_id>')
@api.doc(params={'order_id': 'order_id'})
class CancelOrder(Resource):
    @api.doc('Cancel order',responses={200: ("Success", data_response),404: 'Restaurant Not Found' })
    @jwt_required()
    def put(self, order_id):
        current_user_info = get_jwt_identity()
        restaurant_id = current_user_info["id"]  

        if isRestaurantUser(current_user_info):
            return RestaurantService.cancelOrder(order_id, restaurant_id)
        else:
            response = responses.error_response(401, string_helper.YOU_ARE_NOT_RESTAURANT_USER)
            return response,401