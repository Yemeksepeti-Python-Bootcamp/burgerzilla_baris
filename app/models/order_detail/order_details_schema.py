from attr import fields
from app import ma
from app.models.order_detail.order_details import OrderDetails

class OrderDetailsSchema(ma.Schema):
    """
    Schema for order_details data
    """

    class Meta:
        model = OrderDetails
        fields = ('id', 'order_id', 'product_id', 'delivery_address')