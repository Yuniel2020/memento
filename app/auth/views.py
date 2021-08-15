from flask import render_template, redirect, flash, url_for, current_app
from . import auth
from .forms import RegisterForm, LoginForm
from .. import db
from .. models import User
from .. email import send_email


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """ Login View Function """
    form = LoginForm()
    if form.validate_on_submit():
         user = User.query.filter_by(username=form.name.data).first()
         if user:
             flash('You are now logged in!')
             return render_template('dashboard.html', name=user)
         else:
             flash('You are not registered')
             return redirect(url_for('.register'))
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """ Register View Function """
    user = None
    mail = None
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
            if current_app.config['MEMENTO_ADMIN']:
                send_email(current_app.config['MEMENTO_ADMIN'], 'New User',
                 'mail/new_user', user=user)
            flash('You are now registered')           
        else:
            flash('You have already an account')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form, name=user, email=mail) 

 
