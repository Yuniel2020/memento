from flask import render_template, redirect, flash, url_for, current_app, request, jsonify
from flask.json import dumps
from flask_login.utils import logout_user
from . import auth
from .forms import RegisterForm, LoginForm
from .. import db
from .. models import User, Post, PostSchema
from .. email import send_email
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user


@auth.route('/login', methods=['GET','POST'])
def login():
    """ Login View Function """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and check_password_hash(user.password_hash, form.password.data):
            login_user(user, form.remember_me.data)
            #flash('You are logged in!')
            return redirect(url_for('auth.dashboard'))
        flash('Invalid username or password')      
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """ Register View Function """
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,
                    password_hash = generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        #flash('You are now registered')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form) 


@auth.route('/logout')
@login_required
def logout():
    """ Logout View Function """
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('.login'))


@auth.route('/dashboard', methods=['POST', 'GET'])
@login_required
def dashboard():
    """ Dashboard View Function """
    journal_title_list = Post.query.filter(Post.user_id==current_user.id).all()
    return render_template('auth/dashboard.html', journal_title_list=journal_title_list)


@auth.route('/save_journal', methods=['POST'])
@login_required
def save_journal():
    """ Dashboard-Save View Function """
    elTitle = request.form.get('elTitle')
    elBody = request.form.get('elBody')
    journal = Post(title=elTitle, body=elBody, user_id=int(current_user.id))
    db.session.add(journal)
    db.session.commit()
    return loading_entry()

@auth.route('/loading_entry', methods=['GET'])
@login_required
def loading_entry():
    """ Load-Journal-List View Function """
    last_one = Post.query.filter(Post.user_id==current_user.id).count()
    load_this = Post.query.filter(Post.user_id==current_user.id, Post.id==last_one)
    print(last_one)
    post_schema = PostSchema(many=True)
    output = post_schema.dump(load_this)    
    # print(output)
    return jsonify({'post': output }).data

@auth.route('/edit_entry', methods=['GET'])
@login_required
def edit_entry():
    """ Edit-Journal View Function """
    elItemDB = request.args.get('elItemDB')
    # print(elItemDB)
    #print(current_user)
    responseObject = Post.query.filter(Post.user_id==current_user.id, Post.id==elItemDB).first()   
    # print(responseObject)
    post_schema = PostSchema()
    output = post_schema.dump(responseObject) 
    # print(output)
    return jsonify({'post': output }).data

@auth.route('/submit_change', methods=['POST'])
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


@auth.route('/loading_change', methods=['GET'])
@login_required
def loading_change():
    """ Load-Journal-List View Function """
    elItemDB = request.args.get('elItemDB')
    # print(elItemDB)
    #print(current_user)
    responseObject = Post.query.filter(Post.user_id==current_user.id, Post.id==elItemDB).first()   
    # print(responseObject)
    post_schema = PostSchema()
    output = post_schema.dump(responseObject) 
    # print(output)
    return jsonify({'post': output }).data    

@auth.route('/delete_entry', methods=['POST'])
@login_required
def delete_entry():
    """ Delete-Journal-Entry View Function """
    elItemDB = int(request.form.get('elItemDB'))    
    #print(elItemDB)
    #print(current_user)
    deleteEntry = Post.query.filter(Post.user_id==current_user.id, Post.id==elItemDB).first()
    # print(deleteEntry)
    db.session.delete(deleteEntry)
    db.session.commit()
    return dashboard()