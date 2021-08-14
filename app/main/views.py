from flask import render_template, session, redirect, url_for
from . import main
from .forms import LoginForm
from .. import db
from ..models import User
from .. email import send_async_email, send_email

""" Index """
@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    """Log user in"""
    user = None
    mail = None
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
            session['know'] = False
            if main.app.config['MEMENTO_ADMIN']:
                send_email(app.config['MEMENTO_ADMIN'], 'New User',
                 'mail/new_user', user=user)       
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''            
        return render_template('dashboard.html', name=session['name'])
    return render_template('login.html', form=form, name=user, email=mail) 

 
