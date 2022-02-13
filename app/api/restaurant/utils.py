from app.api.order_detail.utils import order_status_check
from app.api.product.utils import loadProductData
from app.models.order_detail.order_details import OrderDetails
from app.models.product.product import Product
from app.models.restaurant.restaurant_schema import RestaurantSchema
from app.models.user.user import User

def loadRestaurantData(restaurant_db_object):
    restaurant_schema = RestaurantSchema() 
    restaurant_data = restaurant_schema.dump(restaurant_db_object)

    return restaurant_data


def isRestaurantUser(current_user):
    """
     Check if the user is a restaurant user
    Return: Boolean
    """
    
    return current_user["is_restaurant"] == True

def isRestaurantOwner(current_user, restoran_info):
    """
     Check if the user is a owner of restaurant
    Return: Boolean
    """
    restaurant_email = restoran_info.email
    
    return current_user["email"] == restaurant_email

def getOrderDetails(orders):
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
        order_details["restaurant_name"] = order.restaurant.restaurant_name
        order_details["order_owner"] = User.query.filter_by(id = order.customer_id).first().username
        order_details["order_date"] = str(order.order_date)
        order_details["order_address"] = order.delivery_address
        order_details["order_total_price"] = str(total_price)+" TL"
        order_details["products"] = product_datas
        
   
        all_order_details.append(order_details)

    return all_order_details



