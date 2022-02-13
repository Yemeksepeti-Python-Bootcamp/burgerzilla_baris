from app import db
from datetime import datetime

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order_details = db.relationship('OrderDetails', backref='order', lazy='dynamic')
    order_status = db.Column(db.Integer, nullable=False, default = 1)
    order_note = db.Column(db.String(256), nullable=True)
    delivery_address = db.Column(db.String(300), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


