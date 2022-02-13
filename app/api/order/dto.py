
from flask_restx import Namespace, fields

from app.api.order_detail.dto import OrderDetailsDTO

class OrderDTO:
    api = Namespace("order", description="Order related operations")

    order = api.model("order", {
        "id": fields.Integer(readOnly=True, description="The unique identifier of a order"),
        "restaurant_id": fields.Integer(required=True, description="The restaurant id of a order"),
        "customer_id": fields.Integer(required=True, description="The customer id of a order"),
        "order_details": fields.List(fields.Nested(OrderDetailsDTO.order_detail), description="The order details of a order"),
        "order_date": fields.DateTime(required=True, description="The order date of a order"),
        "order_status": fields.Integer(required=True, description="The order status of a order"),
    })

    order_data_response = api.model("order_data_response", {
        "status":fields.Boolean,
        "message":fields.String,
        "order":fields.Nested(order)
    })



