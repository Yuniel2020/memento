from flask_sqlalchemy import SQLAlchemy
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

""" Defining model for database """
# Defining the models for Users table
class User(db.Model):
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
    post = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % self.post

