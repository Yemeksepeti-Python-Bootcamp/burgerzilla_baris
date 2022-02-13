from attr import fields
from app import ma
from app.models.orders.orders import Orders

class OrdersSchema(ma.Schema):
    """
    Schema for orders data
    """

    class Meta:
        model = Orders
        fields = ('id', 'restaurant_id', 'customer_id', 'order_date')