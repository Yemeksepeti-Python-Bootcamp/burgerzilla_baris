from app.api.order_detail.utils import order_status_check
from app.api.product.utils import loadProductData
from app.models.menu.menu import Menu
from app.models.order_detail.order_details import OrderDetails
from app.models.product.product import Product
from app.models.restaurant.restaurant import Restaurant
from app.models.user.user import User
from app.models.user.user_schema import UserSchema


def isProductExistInRestaurant(product_data:list, restaurant_id:int) -> bool: 
    """
    This method is used to check if a product is exist in a restaurant.

    Returns True if the product is exist in the restaurant.
    """
    menu = Menu.query.filter_by(restaurant_id = restaurant_id).first()
    products = Product.query.filter_by(menu_id = menu.id).all()
    restoran_product_ids = [product.id for product in products]
    product_status = {}

    for product in product_data:
        if product["product_id"] not in restoran_product_ids:
            product_status = {"is_exist": False, "product_id": product["product_id"]}
            return product_status

    product_status["is_exist"] = True
    return product_status

def parseOrderData(order_data):
    orders = []

    products = order_data["order"]
    
    if len(products):
        for product in products:
            product_info= {}
            product_info["product_id"] = product["product_id"]
            product_info["product_name"] = Product.query.filter_by(id = product["product_id"]).first().product_name
            product_info["quantity"] = product["quantity"]
            product_info["product_price"] = Product.query.filter_by(id = product["product_id"]).first().product_price

            orders.append(product_info)
    return orders

def computeTotalPrice(products):
    """
    This method is used to compute the total price of a product.

    Returns the total price.
    """
    total_price = 0

    for product in products:
        total_price += product["product_price"] * product["quantity"]

    return total_price


def getUserSpecificOrderDetails(order):
    
    order_details_map = {}
    product_datas = []
    total_price = 0

    order_details = OrderDetails.query.filter_by(order_id = order.id).all()

    for order_detail in order_details:
        product = Product.query.filter_by(id = order_detail.product_id).first()
        quantity = OrderDetails.query.filter_by(product_id = product.id).first().product_quantity
        product_data = loadProductData(product)
        product_datas.append(product_data)
        total_price += product.product_price * quantity


    order_details = OrderDetails.query.filter_by(order_id = order.id).first()
    product = Product.query.filter_by(id = order_details.product_id).first()
    menu = Menu.query.filter_by(id = product.menu_id).first()
    restaurant = Restaurant.query.filter_by(id = menu.restaurant_id).first()

    order_details_map["order"] = order
    order_details_map["order_details"] = product_datas
    order_details_map["product"] = product
    order_details_map["menu"] = menu
    order_details_map["restaurant"] = restaurant
    order_details_map["total_price"] = total_price

    return order_details_map


def getUserAllOrderDetails(orders):
    """
    This function is used to get the 
    all order details of a user from database.

    Returns a list of order details.
    """
    all_order_details = []


    for order in orders:
        total_price = 0
        order_details = {}
        product_datas = []


        order_details["order_id"] = order.id
        order_details_s = OrderDetails.query.filter_by(order_id = order.id).all()

        for order_detail in order_details_s:
            product_data = {}
            product = Product.query.filter_by(id = order_detail.product_id).first()
            quantity = order_detail.product_quantity
            product_data["product_id"] = product.id
            product_data["product_name"] = product.product_name
            product_data["product_description"] = product.product_description
            product_data["quantity"] = quantity
            product_data["product_price"] = product.product_price

            product_datas.append(product_data)
            total_price += product.product_price * quantity

        order_details["order_status"] = order_status_check(order.order_status)
        order_details["restaurant_name"] = Restaurant.query.filter_by(id = order.restaurant_id).first().restaurant_name
        order_details["order_owner"] = User.query.filter_by(id = order.customer_id).first().username
        order_details["order_date"] = str(order.order_date)
        order_details["order_address"] = order.delivery_address
        order_details["order_total_price"] = str(total_price)+" TL"      
        order_details["products"] = product_datas
        
        all_order_details.append(order_details)

    return all_order_details

def getRestaurantDetails(restaurants):
    """
    This method is used to parse the 
    restaurant data from the database.

    Returns a list of restaurant data.
    """
    all_restaurant_details = []

    for restaurant in restaurants:
        restaurant_data = {}
        menu_data = {}

        menu = Menu.query.filter_by(restaurant_id = restaurant.id).first()
        products = [loadProductData(product) for product in Product.query.filter_by(menu_id = menu.id).all()]
        menu_data["menu_name"] = menu.menu_name
        menu_data["products"] = products
     
        restaurant_data["restaurant_id"] = restaurant.id
        restaurant_data["restaurant_name"] = restaurant.restaurant_name
        restaurant_data["restaurant_email"] = restaurant.email
        restaurant_data["restaurant_address"] = restaurant.address
        restaurant_data["restaurant_menu"] = menu_data

        all_restaurant_details.append(restaurant_data)
    
    return all_restaurant_details

        

