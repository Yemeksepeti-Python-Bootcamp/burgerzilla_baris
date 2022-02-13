from app import db

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu_name = db.Column(db.String(100), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    products = db.relationship('Product', backref='menu', lazy='dynamic')