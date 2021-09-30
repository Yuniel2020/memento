from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from . import db, login_manager, ma
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
    posts = db.relationship('Post', back_populates='user', lazy='dynamic')

    # This method give the table a readable string representation that
    #  can be use for debugging and testing purposes.
    def __repr__(self):
        return "<id='%s',  username='%s', email='%s', password_hash='%s')>" % (self.id, self.username,
                      self.email, self.password_hash)
    
# Defining the models for Posts table
class Post(db.Model):
    __tablename__ =  'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = relationship('User', back_populates='posts', lazy=True)

    def __repr__(self):
        return "<id='%s', title='%s', body='%s', timestamp='%s', user_id='%s')>" % (self.id, self.title,
                                self.body, self.timestamp, self.user_id)          

    # This function will be called when the extension requires to load 
    # a user from the database given its identifier
    @login_manager.user_loader # The decorator is used to register the function with Flask-Login
    def load_user(user_id):
        return User.query.get(int(user_id))

""" Generating marshmallow Schemas from the models using SQLAlchemySchema"""
# Marshmallow Schema for User
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
    password_hash = ma.auto_field()
    posts = ma.auto_field()
    
class PostSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Post        # ?
        include_fk = True

    id = ma.auto_field()
    title = ma.auto_field()
    body = ma.auto_field()
    timestamp = ma.auto_field()
    user_id = ma.auto_field()