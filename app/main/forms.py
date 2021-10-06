from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length

""" Defining form class"""
""" RegisterForm class """
class RegisterForm(FlaskForm):
     email = StringField('Email', validators=[DataRequired(), Length(1, 64), 
                                              Email()])
     password = PasswordField('password', validators=[DataRequired()])


""" LoginForm class """
class LoginForm(FlaskForm):
     email = StringField('email', validators=[DataRequired(), Length(1, 64), 
                                              Email()])
     password = PasswordField('password', validators=[DataRequired()])
     remember_me = BooleanField('Remember me')
