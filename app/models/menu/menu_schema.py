from app import ma
from app.models.menu.menu import Menu

class MenuSchema(ma.Schema):
    """
    Schema for menu data
    """
    class Meta:
        model = Menu
        fields = ('id', 'restaurant_id', 'menu_name' )