from attr import fields
from app import ma
from app.models.product.product import Product

class ProductSchema(ma.Schema):
    """
    Schema for product data
    """
    
    class Meta:
        model = Product
        fields = ('id', 'product_name', 'product_description', 'product_price', 'product_img', 'menu_id')