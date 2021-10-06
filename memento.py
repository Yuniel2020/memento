""" Here it's where the application instance is defined """
import os
from app import create_app, db 
from app.models import User, Post
from flask_migrate import Migrate, upgrade

""" Creating an application using the app constructor """
app = create_app(os.getenv('MEMENTO_CONFIG') or 'default')
migrate = Migrate(app, db)

""" Adding the deploy command """
@app.cli.command()
def deploy():
    """ Run deployment tasks"""
    db.create_all()

