def loadProductData(product_db_object):
    from app.models.product.product_schema import ProductSchema

    product_schema = ProductSchema()
    product_data = product_schema.dump(product_db_object)
    
    return product_data