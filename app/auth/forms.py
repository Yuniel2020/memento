from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

""" Defining form class"""
class RegisterForm(FlaskForm):
     name = StringField('name', validators=[DataRequired()])
     email = StringField('Email', validators=[DataRequired(), Length(1, 64), 
                                              Email()])
     password = PasswordField('password', validators=[DataRequired(), 
          EqualTo('password2', message='Password must match')])
     password2 = PasswordField('password2', validators=[DataRequired()]) 
     submit = SubmitField('Register')

class LoginForm(FlaskForm):
     name = StringField('name', validators=[DataRequired()])
     password = PasswordField('password', validators=[DataRequired()])
     submit = SubmitField('Login')

