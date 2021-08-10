from flask import Flask, render_template, redirect
from werkzeug.exceptions import HTTPException

app = Flask(__name__) # Creating the Flask application instance 


@app.route('/', methods=['GET', 'POST'])
def index():
    """if method == 'POST':
        render_template('login.html')"""
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return 'This page does not exist', 404

@app.errorhandler(500)
def internal_server_error(e):
    return 'Internal server error', 500