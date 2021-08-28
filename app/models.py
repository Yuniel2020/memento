from flask_sqlalchemy import SQLAlchemy
from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime

""" Defining model for database """
# Defining the models for Users table
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='user', lazy='dynamic')

    # This method give the table a readable string representation that
    #  can be use for debugging and testing purposes.
    def __repr__(self):
        return '<User %r>' % self.username
    
# Defining the models for Posts table
class Post(db.Model):
    __tablename__ =  'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % self.post

# This function will be called when the extension requires to load 
    # a user from the database given its identifier
    @login_manager.user_loader # The decorator is used to register the function with Flask-Login
    def load_user(user_id):
        return User.query.get(int(user_id))

