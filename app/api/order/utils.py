def load_order_data(order_db_object):
    from app.models.orders.orders_schema import OrdersSchema

    order_schema = OrdersSchema()
    order_data = order_schema.dump(order_db_object)
    
    return order_data