from flask_restx import Namespace, fields

class ProductDTO:

    api = Namespace('product', description='product related operations')

    product = api.model('product', {
        "id": fields.Integer,
        "product_name": fields.String,
        'product_description': fields.String,
        'product_price': fields.Float,
        'product_image': fields.String,
    })

