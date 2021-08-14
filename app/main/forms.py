from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

""" Defining form class"""
class LoginForm(FlaskForm):
     name = StringField('name', validators=[DataRequired()])
     email = StringField('Email', validators=[DataRequired(), Length(1, 64), 
                                              Email()])
     submit = SubmitField('submit')
