""" This is the app package constructor. Inside of it is created 
    the factory function. See pag. 88 """

from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import config
from flask_login import LoginManager

# As there is not application instance to initialize the extensions with,
# and creates instance for each extensions, they are created uninitialized
# by passing no arguments into the constructors
mail = Mail()
db = SQLAlchemy()
ma = Marshmallow()
login_manager = LoginManager() # Initializing Flask-Login in the app factory
login_manager.login_view = 'auth.login'
# The login_view attribute of the LoginManager object sets the endpoint for the
# login page. Flask-Login will redirect to the login page
# when an anonymous user tries to access a protected page   

""" Defining the application factory """
""" It takes as argument the name of a configuration to use for the app"""
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name]) 
    config[config_name].init_app(app)

    mail.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    login_manager.init_app(app)

    """ Registering the blueprint inside the app factory """
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
