def load_order_details_data(order_detail_db_object):
    from app.models.order_detail.order_details_schema import OrderDetailsSchema

    order_detail_schema = OrderDetailsSchema()
    order_detail_data = order_detail_schema.dump(order_detail_db_object)

    return order_detail_data

def order_status_check(order_stat):
    if order_stat == 1:
        return "New"
    elif order_stat == 2:
        return "In progress"
    elif order_stat == 3:
        return "On the way"
    elif order_stat == 4:
        return "Delivered"
    elif order_stat == 5:
        return "Cancelled by Restaurant"
    elif order_stat == 6:
        return "Cancelled by Customer"

