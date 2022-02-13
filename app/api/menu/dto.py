from flask_restx import Namespace, fields
from app.api.product.dto import ProductDTO

class MenuDTO:
    api = Namespace('menu', description='menu related operations')

    menu = api.model('menu', {
        "id": fields.Integer,
        "menu_name": fields.String,
        'products': fields.List(fields.Nested(ProductDTO.product))
    })


