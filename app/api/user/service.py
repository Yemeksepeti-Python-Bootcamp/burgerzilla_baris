from flask import current_app, jsonify
from app.api.order_detail.utils import order_status_check
from app.api.user.utils import computeTotalPrice, getRestaurantDetails, getUserAllOrderDetails, getUserSpecificOrderDetails, isProductExistInRestaurant, parseOrderData
from app.models.menu.menu import Menu
from app.models.order_detail.order_details import OrderDetails
from app.models.orders.orders import Orders
from app.models.product.product import Product
from app.models.restaurant.restaurant import Restaurant
from app.utils.messages.error_message_response import ErrorMessages
from app.utils.messages.success_message_response import SuccessMessages
from app.utils.helpers.database_helper import DatabaseHelper
from app.utils.helpers.string_helper import StringHelper
from app.utils.messages.responses import Responses
from app.models.user.user import User
from app import db


error_messages = ErrorMessages()
success_messages = SuccessMessages()
responses = Responses()
string_helper = StringHelper()
database_helper = DatabaseHelper()

class UserService:

    # --------------------------------------------------------------------------------------------------------------------------
    # -------------- ORDER OPERATIONS -------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------

    @staticmethod
    def createOrder(customer_id, restaurant_id, order_data):
        """
        This method is used to create an order.
        """
        restaurant = Restaurant.query.filter_by(id = restaurant_id).first() # Get restaurant details

        if restaurant: # if restaurant exists
            products_data = parseOrderData(order_data) # Parse order data and returns ordered products
            
            quantity_product = len(products_data) # Get quantity of ordered products
            

            if quantity_product: # if quantity of ordered products is not equal to zero 
                product_status = isProductExistInRestaurant(products_data, restaurant_id) # Check if product is exist in restaurant

                if product_status["is_exist"]: # Check if ordered products are exist in the restaurant

                    if quantity_product == 1: # if quantity of ordered products is just one
                        product = Product.query.filter_by(id = products_data[0]["product_id"]).first() # Get product details
                        menu = Menu.query.filter_by(id = product.menu_id).first() # get menu
                        user = User.query.filter_by(id = customer_id).first() # get user

                        if restaurant_id == menu.restaurant_id: # if restaurant has the product, then create order
                            order = Orders(
                                customer_id = customer_id, restaurant_id = restaurant_id, 
                                order_status = 1, delivery_address = user.address, total_price = computeTotalPrice(products_data))
                            database_helper.saveDatabase(order)
                            
                            order_detail = OrderDetails(order_id = order.id, product_id = product.id, product_quantity = products_data[0]["quantity"])
                            database_helper.saveDatabase(order_detail)

                            response = responses.success_response(200, string_helper.SUCCESS_ORDER_CREATED)
                            response["restaurant_name"] = restaurant.restaurant_name
                            response["order_status"] = order_status_check(order.order_status)
                            response["product_name"] = product.product_name
                            response["quantity"] = products_data[0]["quantity"]
                            response["total_price"] = computeTotalPrice(products_data)
                            response["created_date"] = str(order.order_date)
                            return response
                    else:
                        user = User.query.filter_by(id = customer_id).first() # get user
                        order = Orders(customer_id = customer_id, restaurant_id = restaurant_id,order_status = 1, 
                                    delivery_address = user.address, total_price = computeTotalPrice(products_data)) 
                        database_helper.saveDatabase(order)

                        for product in products_data:
                            product_s = Product.query.filter_by(id = product["product_id"]).first() # Get product details
                            menu = Menu.query.filter_by(id = product_s.menu_id).first() # get menu
                            

                            if restaurant_id == menu.restaurant_id: # if restaurant has the product, then create order
                                order_detail = OrderDetails(order_id = order.id, product_id = product_s.id, product_quantity = product["quantity"])
                                database_helper.saveDatabase(order_detail)

                        response = responses.success_response(200, string_helper.SUCCESS_ORDER_CREATED)
                        response["restaurant_name"] = restaurant.restaurant_name
                        response["order_status"] = order_status_check(order.order_status)
                        response["created_date"] = str(order.order_date)
                        response["total_price"] = computeTotalPrice(products_data)
                        response["products"] = products_data
                        
                        return response
                else:
                    current_app.logger.error(string_helper.FAIL_PRODUCTS_FOUND)
                    response = responses.error_response(400, string_helper.FAIL_PRODUCTS_FOUND)
                    product = Product.query.filter_by(id = product_status["product_id"]).first() # Get product details
                    response["does_not_exist"] = product.product_name

                    return response   

            else:
                current_app.logger.error(string_helper.THERE_IS_NO_ORDER)
                response = responses.error_response(400, string_helper.THERE_IS_NO_ORDER)
                return response
        else:
            current_app.logger.error(string_helper.FAIL_RESTAURANT_FOUND)
            response = responses.error_response(400, string_helper.FAIL_RESTAURANT_FOUND)
            return response
        

    @staticmethod
    def getOrderById(order_id, user_id):
        """
        This method is used to get an order by id.
        """
        order = Orders.query.filter_by(id = order_id).first()

        if order.customer_id == user_id:
            order_detail = getUserSpecificOrderDetails(order)

            response = responses.success_response(200, string_helper.SUCCESS_ORDERS_FOUND)
            response["order_id"] = order_detail["order"].id
            response["order_status"] = order_status_check(order_detail["order"].order_status)
            response["restaurant_name"] = order_detail["restaurant"].restaurant_name
            response["total_price"] = order_detail["total_price"]
            response["order_address"] = order_detail["order"].delivery_address
            response["created_date"] = str(order_detail["order"].order_date)
            response["products"] = order_detail["order_details"]
 
            return response          
        else:
            current_app.logger.error(string_helper.FAIL_ORDER_FOUND)
            response = responses.error_response(400, string_helper.FAIL_ORDER_FOUND)
            response["order_id"] = order.id
            return response
        

    @staticmethod
    def get_orders(user_id):
        orders = Orders.query.filter_by(customer_id=user_id).all()
        active_orders_count = len([order for order in orders if order.order_status < 4])

        if orders:
            all_orders = getUserAllOrderDetails(orders)
            response = responses.success_response(200, string_helper.SUCCESS_ORDERS_FOUND)
            response["orders_count"] = len(all_orders)
            response["active_orders_count"] = active_orders_count
            response["orders"] = all_orders
            return response, 200

        else:
            current_app.logger.error(string_helper.FAIL_ORDER_FOUND)
            response = responses.error_response(404, string_helper.FAIL_ORDER_FOUND)
            return response, 404

    @staticmethod
    def cancel_order(user_id, order_id):
        order = Orders.query.filter_by(id=order_id, customer_id = user_id).first()

        if order:
            order.order_status = 6 # 6 = cancelled
            db.session.commit()

            response = responses.success_response(200, string_helper.SUCCESS_ORDER_CANCEL)
            return response, 200
        else:
            current_app.logger.error(string_helper.FAIL_ORDER_FOUND)
            response = responses.error_response(404, string_helper.FAIL_ORDER_FOUND)
            return response, 404

    @staticmethod
    def get_active_orders(user_id):
        orders = Orders.query.filter_by(customer_id = user_id).all()
        orders = [order for order in orders if order.order_status < 4]

        if orders:
            all_orders = getUserAllOrderDetails(orders)
            response = responses.success_response(200, string_helper.SUCCESS_ORDERS_FOUND)
            response["active_orders_count"] = len(all_orders)
            response["orders"] = all_orders

            return response, 200
        else:
            current_app.logger.error(string_helper.FAIL_ACTIVE_ORDERS)
            response = responses.error_response(404, string_helper.FAIL_ACTIVE_ORDERS)
            return response, 404
    
    # --------------------------------------------------------------------------------------------------------------------------
    # -------------- RESTAURANT OPERATIONS -----------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------

    @staticmethod
    def get_all_restaurants():
        restaurants = Restaurant.query.all()

        if restaurants:
            response = responses.success_response(200, string_helper.SUCCES_RESTAURANT_FOUND)
            response["restaurants"] = getRestaurantDetails(restaurants)
            return response, 200
        else:
            current_app.logger.error(string_helper.FAIL_RESTAURANT_FOUND)
            response = responses.error_response(404, string_helper.FAIL_RESTAURANT_FOUND)
            return response, 404
    
    @staticmethod
    def get_restaurant_by_id(restaurant_id):
        restaurant = Restaurant.query.filter_by(id = restaurant_id).first()

        if restaurant:
            response = responses.success_response(200, string_helper.SUCCES_RESTAURANT_FOUND)
            response["restaurants"] = getRestaurantDetails([restaurant])
            return response, 200

        else:
            current_app.logger.error(string_helper.FAIL_RESTAURANT_FOUND)
            response = responses.error_response(404, string_helper.FAIL_RESTAURANT_FOUND)
            return response, 404



    