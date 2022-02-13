from app import ma
from app.models.restaurant.restaurant import Restaurant

class RestaurantSchema(ma.Schema):
    """
    Schema for restaurant data
    """
    
    class Meta:
        model = Restaurant
        fields = ('id', 'is_restaurant','restaurant_name', 'email', 'owner_name', 'owner_surname', 'address', 'joined_date', 'hash_password')