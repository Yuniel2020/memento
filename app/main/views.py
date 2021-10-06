from flask import render_template, redirect, flash, url_for, request, jsonify
from . import main
from .forms import RegisterForm, LoginForm
from .. import db
from .. models import User, Post, PostSchema
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from flask.json import dumps
from flask_login.utils import logout_user
from werkzeug.security import generate_password_hash, check_password_hash

""" Index """
@main.route('/', methods=['GET'])
def index():
    return login()

""" Demo Login """
@main.route('/demo', methods=['GET'])
def demo():
    return render_template('dashboard.html')
    
""" Login """
@main.route('/login', methods=['GET','POST'])
def login():
    # Login View Function
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and check_password_hash(user.password_hash, form.password.data):
            login_user(user, form.remember_me.data)
            #flash('You are logged in!')
            return redirect(url_for('main.dashboard'))
        flash('Invalid email or password')      
    return render_template('login.html', form=form)

""" Register """
@main.route('/register', methods=['GET', 'POST'])
def register():
    """ Register View Function """
    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # Check if email exists already
            check_this_email = User.query.filter_by(email=form.email.data).first()
            if check_this_email is None:
                user = User(email=form.email.data,
                            password_hash = generate_password_hash(form.password.data))
                db.session.add(user)
                db.session.commit()
                flash('You are now registered')
                return redirect(url_for('main.login'))
            flash("Email exists already")            
    return render_template('register.html', form=form)

""" Logout"""
@main.route('/logout')
@login_required
def logout():
    """ Logout View Function """
    delete_user = User.query.filter(User.id==current_user.id).first()
    db.session.delete(delete_user)
    db.session.commit()
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.login'))

""" Dashboard """
@main.route('/dashboard', methods=['POST', 'GET'])
@login_required
def dashboard():
    """ Dashboard View Function """
    journal_title_list = Post.query.filter(Post.user_id==current_user.id).order_by(Post.timestamp.desc()).all()
    return render_template('dashboard.html', journal_title_list=journal_title_list)

""" Save Entry """
@main.route('/save_journal', methods=['POST'])
@login_required
def save_journal():
    """ Dashboard-Save View Function """
    elTitle = request.form.get('elTitle')
    elBody = request.form.get('elBody')
    journal = Post(title=elTitle, body=elBody, user_id=int(current_user.id))
    db.session.add(journal)
    db.session.commit()
    return loading_entry()

""" Load last entry """
@main.route('/loading_entry', methods=['GET'])
@login_required
def loading_entry():
    """ Load-Journal-List View Function """
    last_one = Post.query.filter(Post.user_id==current_user.id).count()
    load_this = Post.query.filter(Post.user_id==current_user.id, Post.id==last_one)
    post_schema = PostSchema(many=True)
    output = post_schema.dump(load_this)    
    return jsonify({'post': output }).data

""" Edit Entry """
@main.route('/edit_entry', methods=['GET'])
@login_required
def edit_entry():
    """ Edit-Journal View Function """
    elItemDB = request.args.get('elItemDB')
    responseObject = Post.query.filter(Post.user_id==current_user.id, Post.id==elItemDB).first()   
    post_schema = PostSchema()
    output = post_schema.dump(responseObject) 
    return jsonify({'post': output }).data

""" Submit Change """
@main.route('/submit_change', methods=['POST'])
@login_required
def submit_change():
    """ Submit change Function """
    elTitle = request.form.get('elTitle')
    elBody = request.form.get('elBody')
    elItemDB = request.form.get('elItemDB')
    responseObject = Post.query.filter(Post.user_id==current_user.id, Post.id==elItemDB).first()
    responseObject.title = elTitle
    responseObject.body = elBody
    db.session.commit()
    return loading_change()

""" Load Change """
@main.route('/loading_change', methods=['GET'])
@login_required
def loading_change():
    """ Load-Journal-List View Function """
    elItemDB = request.args.get('elItemDB')
    responseObject = Post.query.filter(Post.user_id==current_user.id, Post.id==elItemDB).first()   
    post_schema = PostSchema()
    output = post_schema.dump(responseObject) 
    return jsonify({'post': output }).data    

""" Delete Entry"""
@main.route('/delete_entry', methods=['POST'])
@login_required
def delete_entry():
    """ Delete-Journal-Entry View Function """
    elItemDB = int(request.form.get('elItemDB'))    
    deleteEntry = Post.query.filter(Post.user_id==current_user.id, Post.id==elItemDB).first()
    db.session.delete(deleteEntry)
    db.session.commit()
    return dashboard()