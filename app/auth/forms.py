from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from ..models import User
from wtforms import ValidationError

""" Defining form class"""
""" RegisterForm class """
class RegisterForm(FlaskForm):
     username = StringField('username', validators=[DataRequired(), Length(1, 64),
               Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
               'Usernames muss have only letters, numbers, dots or ' 
                'underscores')])
     email = StringField('Email', validators=[DataRequired(), Length(1, 64), 
                                              Email()])
     password = PasswordField('password', validators=[DataRequired(), 
          EqualTo('password2', message='Password must match')])
     password2 = PasswordField('password2', validators=[DataRequired()]) 
     submit = SubmitField('Register')

     def validate_email(self, email):
          if User.query.filter_by(email=email.data).first():
               raise ValidationError('Email already registered.')
     
     def validate_username(self, username):
          if User.query.filter_by(username=username.data).first():
               raise ValidationError('Username alreay in use')


""" LoginForm class """
class LoginForm(FlaskForm):
     email = StringField('email', validators=[DataRequired(), Length(1, 64), 
                                              Email()])
     password = PasswordField('password', validators=[DataRequired()])
     remember_me = BooleanField('Keep me logged in')
     submit = SubmitField('Log in')

