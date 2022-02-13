"""
All packages and modules that are used by the application.

"""
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



db = SQLAlchemy() # for used database operations

bcrypt = Bcrypt() # for hashing passwords
migrate = Migrate() # for database migrations
cors = CORS() # for cross-origin resource sharing

jwt = JWTManager() # for JWT authentication
ma = Marshmallow() # for serializing data