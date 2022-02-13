from flask_restx import Namespace, fields

class UserDTO:

    api = Namespace('user', description='user related operations')

    user = api.model('user', {
        "username": fields.String,
        'email': fields.String,
        'name': fields.String,
        'surname': fields.String,
        'address': fields.String,
        'joined_date': fields.DateTime

        })
    
    data_response = api.model('data_response', {
        "status": fields.Boolean,
        "message": fields.String,
        "user": fields.Nested(user)
        })

