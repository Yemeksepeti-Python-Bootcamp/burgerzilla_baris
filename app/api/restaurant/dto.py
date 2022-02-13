from flask_restx import Namespace, fields
from app.api.menu.dto import MenuDTO

class RestaurantDTO:
    api = Namespace('restaurant', description='restaurant related operations')

    restaurant = api.model('restaurant', {
        "id": fields.Integer,
        "restaurant_name": fields.String,
        'email': fields.String,
        'owner_name': fields.String,
        'owner_surname': fields.String,
        'address': fields.String,
        'joined_date': fields.DateTime
        })
    
    data_response = api.model('data_response', {
        "status": fields.Boolean,
        "message": fields.String,
        "restaurant": fields.Nested(restaurant)
        })
    
    restaurant_menu_response = api.model('restaurant_menu_response', {
        "status": fields.Boolean,
        "message": fields.String,
        "restaurant_menus":fields.Nested(MenuDTO.menu)
        })

    menu_get_by_restaurant_id_data = api.model('menu_get_by_restaurant_id_data', {
        "restaurant_id": fields.Integer,
    })

