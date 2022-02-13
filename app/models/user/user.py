from datetime import datetime
from ...utils.helpers.string_helper import StringHelper
from app import db, bcrypt

string_helper = StringHelper()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(100), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    name = db.Column(db.String(100), nullable = True)
    surname = db.Column(db.String(100), nullable = True)
    address = db.Column(db.String(300), nullable = True)
    orders = db.relationship('Orders', backref = 'user', lazy = 'dynamic')
    joined_date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    is_restaurant = db.Column(db.Boolean, nullable = False, default = False)
    hash_password = db.Column(db.String(128))



    
    @property
    def password(self) -> str:
        raise AttributeError(string_helper.PASSWORD_NOT_ACCESSIBLE)
    
    @password.setter
    def password(self, password: str) -> None:
        """
        Setter for password
        """
        self.hash_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def verify_password(self, password: str) -> bool:
        """
        Verify password
        """
        return bcrypt.check_password_hash(self.hash_password, password)
