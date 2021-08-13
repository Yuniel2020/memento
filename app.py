import os
from flask import Flask, request, render_template, redirect, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from werkzeug.exceptions import HTTPException
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_mail import Mail, Message
from threading import Thread


""" CONFIGURATIONS """
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__) # Creating the Flask application instance 
app.config['SECRET_KEY'] = '!justIf2are1*'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# If set to True SQLAlchemy will log all the statements issued to stderr which can be useful for debugging.
app.config['SQLALCHEMY_ECHO'] = True
app.config['MAIL_SERVER']= 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MEMENTO_MAIL_SUBJECT_PREFIX'] = '[Memento]'
app.config['MEMENTO_MAIL_SENDER'] = 'memento.gmbh@gmail.com'
app.config['MEMENTO_ADMIN'] = os.environ.get('MAIL_USERNAME')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

""" Defining form class"""
class LoginForm(FlaskForm):
     name = StringField('name', validators=[DataRequired()])
     email = StringField('Email', validators=[DataRequired(), Length(1, 64), 
                                              Email()])
     submit = SubmitField('submit')

""" Defining model for database """
# Defining the models for Users table
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
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

db.create_all()

""" Add automatic imports """
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Post=Post)
    
#########################################################   
""" View functions """

""" Index """
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


""" Login """
@app.route('/login', methods=['GET', 'POST'])
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
            if app.config['MEMENTO_ADMIN']:
                send_email(app.config['MEMENTO_ADMIN'], 'New User',
                 'mail/new_user', user=user)       
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''            
        return render_template('dashboard.html', name=session['name'])
    return render_template('login.html', form=form, name=user, email=mail) 


""" Implementing Asynchronous Email Support"""
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

""" Defining Email Support Function """
def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['MEMENTO_MAIL_SUBJECT_PREFIX'] + subject, 
                            sender=app.config['MEMENTO_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr    

@app.errorhandler(404)
def page_not_found(e):
    return 'This page does not exist', 404

@app.errorhandler(500)
def internal_server_error(e):
    return 'Internal server error', 500