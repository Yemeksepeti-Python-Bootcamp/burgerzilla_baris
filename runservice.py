import os
import click
from dotenv import load_dotenv
from app import create_app, db
from app.models.orders.orders import Orders
from app.models.order_detail.order_details import OrderDetails

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from flask_migrate import Migrate
from app.models.user.user import User
from app.models.product.product import Product
from app.models.orders.orders import Orders
from app.models.order_detail.order_details import OrderDetails
from app.models.menu.menu import Menu
from app.models.restaurant.restaurant import Restaurant


app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(
    db=db, 
    User=User, 
    Product=Product, 
    Orders=Orders, 
    OrderDetails=OrderDetails,
    Menu=Menu, 
    Restaurant=Restaurant
    )

@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run unit test """
    import unittest

    if test_names:
        """
        flask test tests.test_dataset_model
        """
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests',pattern='test*.py')

    result =  unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

