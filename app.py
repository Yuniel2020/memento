from flask import Flask, render_template 

app = Flask(__name__) # Creating the Flask application instance 

@app.route('/')
def index():
    return render_template('index.html')