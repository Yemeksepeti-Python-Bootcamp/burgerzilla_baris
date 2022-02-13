from app import ma
from app.models.user.user import User

class UserSchema(ma.Schema):
    """
    Schema for user data
    """
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'surname', 'address', 'joined_date', 'is_restaurant')