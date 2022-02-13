from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_description = db.Column(db.String(350), nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    product_img = db.Column(db.String(350), nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    order_details = db.relationship('OrderDetails', backref='product', lazy='dynamic')


