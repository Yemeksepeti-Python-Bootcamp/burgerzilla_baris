from ast import Name
from flask_restx import Namespace, fields

class OrderDetailsDTO:
    api = Namespace("order_detail", description="Order detail related operations")

    order_detail = api.model("order_detail", {
        "id": fields.Integer,
        "order_id": fields.Integer,
        "product_id": fields.Integer,
        "delivery_address": fields.String,
    })

    order_data_response = api.model("order_data_response", {
        "status": fields.Boolean,
        "message": fields.String,
        "order": fields.Nested(order_detail)
    })





