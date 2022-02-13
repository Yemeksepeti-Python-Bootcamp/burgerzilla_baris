from flask import current_app
from app.api.product.utils import loadProductData
from app.api.order_detail.utils import order_status_check
from app.models.menu.menu_schema import Menu
from app.models.orders.orders import Orders
from app.models.product.product import Product
from app.utils.helpers.database_helper import DatabaseHelper
from app.utils.helpers.string_helper import StringHelper
from app.utils.messages.error_message_response import ErrorMessages
from app.utils.messages.responses import Responses
from app.utils.messages.success_message_response import SuccessMessages
from app.models.restaurant.restaurant import Restaurant
from .utils import getOrderDetails, loadRestaurantData
from app.api.menu.utils import loadMenuData
from app import db

error_messages = ErrorMessages()
success_messages = SuccessMessages()
string_helper = StringHelper()
responses = Responses()
database_helper = DatabaseHelper()

class RestaurantService:
    """
    This class is used to handle all 
    the restaurant related services
    """

    @staticmethod
    def getRestaurantData(restaurant_id):
        """
        This method is used to get 
        the restaurant data by restaurant id
        """
        restaurant = Restaurant.query.filter_by(id = restaurant_id).first() # get the restaurant data

        if restaurant: # if restaurant data is found
            restaurant_data = loadRestaurantData(restaurant) # load the restaurant data
            response = responses.success_response(200, string_helper.SUCCES_RESTAURANT_FOUND) # success response
            response["restaurant"] = restaurant_data # add the restaurant data to the response

            return response,200 # return the response

        else: # if restaurant data is not found
            current_app.logger.error(string_helper.FAIL_RESTAURANT_FOUND) # log the error
            response = responses.error_response(404, string_helper.FAIL_RESTAURANT_FOUND) # error response
             
            return response, 404
    
# ------------------------------------------------------------
# ------------------ MENU OPERATIONS -------------------------
# ------------------------------------------------------------

    @staticmethod
    def getMenuDetail(restaurant_id):
        """
        This method is used to get the menu detail 
        of a restaurant by restaurant id.
        
        """
        menu = Menu.query.filter_by(restaurant_id = restaurant_id).first() # get menu data
                
        if menu: # if menu exist
            products = Product.query.filter_by(menu_id = menu.id).all() # get all products
            restaurant_name = str(Restaurant.query.filter_by(id = restaurant_id).first().restaurant_name) # get restaurant name
            menu_name = str(menu.menu_name) # get menu name

            restaurant_product_data = [loadProductData(product) for product in products] # get product data from product model
            response = responses.success_response(200, string_helper.SUCCES_MENU_FOUND) # success response with status code 200
            response["restaurant_name"] = restaurant_name # add restaurant name to response
            response["menu"] = menu_name # add menu name to response
            response["products"] = restaurant_product_data # add product data to response

            return response,200 # return response with status code 200
        else: # if menu not exist
            response = responses.error_response(404, string_helper.FAIL_MENU_FOUND) # error response with status code 404
            return response

    @staticmethod
    def createMenu(menu_data, restaurant_id):
        """
        This method is used to create a menu 
        for a restaurant by restaurant id.
        """
        menu_name = menu_data.get("menu_name") # get menu name from request data
        menu = Menu.query.filter_by(menu_name = menu_name, restaurant_id = restaurant_id).first() # get menu data by menu name and restaurant id
 
        if menu: # if menu exist in the database
            response = responses.error_response(404, string_helper.MENU_ALREADY_EXISTS) # error response with status code 404 
            return response, 404

        else: # if menu does not exist in the database create a new menu
            menu = Menu(menu_name = menu_name,restaurant_id = restaurant_id) # create a new menu object

            database_helper.saveDatabase(menu) # save the menu to the database with the database helper
            response = responses.success_response(200, string_helper.SUCCESS_MENU_CREATED) # success response with status code 200
            response["menu"] = loadMenuData(menu) # add menu data to response 
            return response, 200

    @staticmethod
    def updateMenu(menu_id, menu_data):
        """
        This method is used to update a menu
        by menu id. 
        """
        menu_name = menu_data.get("menu_name") # get menu name from request data 
        menu = Menu.query.filter_by(id = menu_id).first() # get menu data by menu id 

        if menu: # if menu exist in the database 
            menu.menu_name = menu_name # update the menu name 
            database_helper.updateDatabase() # update the menu in the database with the database helper

            response = responses.success_response(200, string_helper.SUCCESS_MENU_UPDATED) # success response with status code 200
            response["menu"] = loadMenuData(menu) # add menu data to response
            return response, 200

        else: # if menu does not exist in the database 
            response = responses.error_response(404, string_helper.FAIL_MENU_FOUND)
            return response, 404
    
    @staticmethod
    def deleteMenu(menu_id):
        """
        This method is used to delete a menu 
        by menu id.
        """

        menu = Menu.query.filter_by(id = menu_id).first() # get menu data by menu id 
        products = Product.query.filter_by(menu_id = menu_id).all() # get all products by menu id

        if menu: # if menu exist in the database 
            database_helper.deleteDatabase(menu) # delete menu
            for product in products: # delete products
                database_helper.deleteDatabase(product) # delete products that belong to menu
            database_helper.updateDatabase() # update database

            response = responses.success_response(200, string_helper.SUCCESS_MENU_DELETED) # success response with status code 200
            response["menu_name"] = menu.menu_name # add menu name to response
            return response, 200

        else: # if menu does not exist in the database
            response = responses.error_response(404, string_helper.FAIL_MENU_FOUND) # error response with status code 404
            return response, 404


# ------------------------------------------------------------
# ------------------ PRODUCT OPERATIONS ----------------------
# ------------------------------------------------------------

    @staticmethod
    def updateProduct(product_id, product_data):
        """
        This method is used to update a product 
        by product id.
        """
        product_name = product_data.get("product_name") # get product name from request data
        product_price = product_data.get("product_price") # get product price from request data 
        product_description = product_data.get("product_description") # get product description from request data
        product_image = product_data.get("product_image") # get product image from request data
        product = Product.query.filter_by(id = product_id).first() # get product data by product id

        if product: # if product exist in the database
            product.product_name = product_name # update the product name
            product.product_price = product_price # update the product price
            product.product_description = product_description # update the product description
            product.product_img = product_image # update the product image
            
            database_helper.updateDatabase() # update the product in the database with the database helper

            response = responses.success_response(200, string_helper.SUCCESS_PRODUCT_UPDATED) # success response with status code 200
            response["product"] = loadProductData(product)
            return response, 200

        else: # if product does not exist in the database
            response = responses.error_response(404, string_helper.FAIL_PRODUCTS_FOUND) # error response with status code 404
            return response, 404

    @staticmethod
    def deleteProduct(product_id):
        """
        This method is used to delete a product
        by product id.

        """

        product = Product.query.filter_by(id = product_id).first() # get product data by product id

        if product: # if product exist in the database
            database_helper.deleteDatabase(product) # delete product
            response = responses.success_response(200, string_helper.SUCCESS_PRODUCT_DELETED) # success response with status code 200
            response["product"] = product.product_name # add product name to response
            return response, 200

        else: # if product does not exist in the database
            return error_messages.err_resp("Product not found", "Product not found", 404) # error response with status code 404
    
    @staticmethod
    def addProductToMenu(product_data):
        """
        This method is used to add a product to a menu.

        """
        # gets the product data from the request
        product_name = product_data.get("product_name")
        product_price = product_data.get("product_price") 
        product_description = product_data.get("product_description") 
        product_image = product_data.get("product_image") 
        menu_id = product_data.get("menu_id") 

        menu = Menu.query.filter_by(id = menu_id).first() # get menu data by menu id

        if menu: # checks if menu exists
            product = Product(product_name = product_name, product_description = product_description, 
                product_price = product_price, product_img = product_image,  menu_id = menu_id) # create a new product object

            database_helper.saveDatabase(product) # save the product to the database with the database helper

            response = responses.success_response(200, string_helper.SUCCESS_PRODUCT_CREATED) # success response with status code 200
            response["menu"] = menu.menu_name
            response["product"] = loadProductData(product)
            return response, 200
        else: # if menu does not exist in the database
            response = responses.error_response(404, string_helper.FAIL_MENU_FOUND)
            return response, 404

    @staticmethod
    def getAllProducts(restaurant_id):
        """
        This method is used to get all products
        by restaurant id.
        
        """
        restaurant = Restaurant.query.filter_by(id = restaurant_id).first() # get restaurant data by restaurant id
        menu = Menu.query.filter_by(restaurant_id = restaurant_id).first() # get menu data by restaurant id
        all_products = Product.query.filter_by(menu_id = menu.id).all() # get all products by menu id 

        if menu: # if menu exist in the database
            response = responses.success_response(200, string_helper.SUCCESS_PRODUCTS_FOUND) # success response with status code 200
            response["restaurant_name"] = restaurant.restaurant_name # add restaurant name to response
            response["products"] = [loadProductData(product) for product in all_products] # add all products to response 
            return response, 200
        
        else: # if menu does not exist in the database
            response = responses.error_response(404, string_helper.FAIL_PRODUCTS_FOUND)
            response["restaurant_name"] = restaurant.restaurant_name
            return response, 200

# ------------------------------------------------------------
# ------------------ ORDER OPERATIONS ------------------------
# ------------------------------------------------------------

    @staticmethod
    def getAllOrders(restaurant_id):
        """
        This method is used to get all orders
        by restaurant id.
        
        """
        orders = Orders.query.filter_by(restaurant_id = restaurant_id).all() # get all orders by restaurant id

        response = responses.success_response(200, string_helper.SUCCESS_ORDERS_FOUND) # success response with status code 200
        response["orders"] = getOrderDetails(orders) # add all orders to response
        return response, 200
    
    @staticmethod
    def updateOrderStatus(order_id, restaurant_id):
        """
        This method is used to update order status
        by order id.
        
        """

        order = Orders.query.filter_by(id = order_id, restaurant_id = restaurant_id ).first() # get order by id and restaurant id
       
        if order: # check if order exists
            if order.order_status < 4: # if order not delivered or cancelled
                order.order_status = order.order_status + 1

                database_helper.updateDatabase() # update database

                response = responses.success_response(200, string_helper.ORDER_STATUS_UPDATED) # success response with status code 200

                response["order_id"] = str(order.id)
                response["old_order_status"] = order_status_check(order.order_status - 1)
                response["new_order_status"] = order_status_check(order.order_status)
                return response, 200
            else:
                response = responses.error_response(400, string_helper.ORDER_ALREADY_DELIVERED_OR_CANCELED)
                return response, 400
        else: # if order does not exist
            response = responses.error_response(404, string_helper.FAIL_ORDER_FOUND)
            return response, 404


    @staticmethod
    def cancelOrder(order_id, restaurant_id):
        """
        This method is used to cancel order
        by order id.
        
        """
        order = Orders.query.filter_by(id = order_id, restaurant_id = restaurant_id ).first() # get order by id and restaurant id

        response = {}
        if order: # check if order exists
            if order.order_status < 4: # if order not delivered or cancelled
                order.order_status = 5 # cancel order
                database_helper.updateDatabase() # update database

                response = responses.success_response(200, string_helper.SUCCESS_ORDER_CANCEL)
                response["order_status"] = order_status_check(order.order_status)
                return response, 200
            else:
                response = responses.error_response(400, string_helper.ORDER_ALREADY_DELIVERED_OR_CANCELED)
                return response, 400
        else: # if order does not exist
            response = responses.error_response(404, string_helper.FAIL_ORDER_FOUND)
            return response, 404
