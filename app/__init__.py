"""
App Initialization

"""
from flask import Flask

from .extensions import db, bcrypt, cors, jwt, ma
from config import config_by_name

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    register_extensions(app)

    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from .api.user import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/api/user')

    from .api.restaurant import restaurant_blueprint
    app.register_blueprint(restaurant_blueprint, url_prefix='/api/restaurant')

    return app


def register_extensions(app):
    # Registers flask extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)
