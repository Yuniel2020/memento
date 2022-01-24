# CS50's Final Project - Memento 

#### Video Demo:  https://youtu.be/7P-sjr1b4i0

## Purpose
#### My applications aims to allow writing without any distraction.

#### The implementation of the application is quite simple, although I have conceived the project to be easy to scale. In general terms, the project is a CRUD app that tries to follow some of the most important aspects of RESTful API design when creating a SPA that connects to a rich-text editor through an API.

## Live Site
https://ilmemento.herokuapp.com

#### Technology Stack:
1. Backend:
  - Python
  - Flask
  - API

2. Frontend
  - HTML
  - CSS344113
  - JavaScript

3. Database
  - SQLite

## How the app works
### Generalities
The implementation of the application is quite simple, although I have conceived the project to be easy to scale. In order to do that I followed some recommendations from books like 'Flask Web Development' by Miguel Grinberg and of course from the official documentation. 

In general terms my project is a CRUD app that tries to follow some of the most important aspects of Restful api design, by creating a SPA that connects to a rich-text editor (TinyMCE 5) through an API     

I've deployed the app on heroku because I wanted to see how is to run a Flask app in production. Before you can use the app, you have to create an account, then login and start writing. When you save a post, kind of view mode is activated. That way you can see your post, but you can not edit them. If you want to edit one post, you have that option as well as the delete option. 

### Details
The app is created following the package-module pattern proposed in the official documentation as one possible solution for medium-size flask app.

### Packages and modules 
This app contains three top-level folders: 
 - app: This is the application package, where the flask application and others packages and modules live
 - migrations: this folder contains the database migrations scripts
 - venv: this folder contains the Python virtual environment
 
#### app package. Details (this package can be given any desired name)
The app package contains:
 - The main package: This is where all of the main implementations and functionalities of the app remain. It's implemented using the Blueprint principle of modular-scalable-design for flask application. The main package contains:
	- The Blueprint constructor: Here is where the Blueprint 
	object is instantiated.
	- The errors module
	- The forms module
	- The views module with all routes: There is the index view route that redirect to the login route. Although the app is implemented to follow almost all needed functionalities in order to create an account, no account will be really store in database. This means that the user can create an account, login, use the app and, but, when he/she logs out, all data will be deleted. 

In order to authenticate users, the Flask-Login and the Werkzeug packages have been used. The first one works very closely with the User model (see Database). The second one provides tools for password generation and password authentication.


 - The templates and static directories
 - The app package constructor
 - The models module (database): The database has been implemented using the Flask-SQLAlchemy extension. This extension simplifies the use of SQLAlchemy inside Flask, and provide several database backends, like the one for SQLite engine, the one that I've used. I've created one database with two models, User and Post, that connected through a one-to-many relationship. 


### Modules outside app
  - config.py: This file stores the configuration settings. It is conceived thinking in the possibility of escalating the app, meaning adding functionalities to it like mail confirmation, unit testing database configuration, etc.

    First, basedir is defined, which is a variable that points to the directory where the config.py module is. This basedir variable is then used to reference the database to be used for each particular environment. 
    Then a class and two subclasses are declared. The class will contain settings that are common to all environments. The subclasses
    will contain the specific ones.
    
    At the bottom, the different configurations are registered in a config dictionary, and one of them is registered as the default (development)
 
  !!! - memento.py: defines the application instance and a command-line function to create the database when deploying the app
  

### Possible improvements
This is a very simple app that can be easily scale due to the design-pattern followed (see Flask documentation: Pattern for Flask). Some possible improvements are:
  -  Responsive design
  -  Other functionalities implementations according to the use: email support, account confirmation using itsdangerous
