""" Creating the package constructor for a blueprint """

from flask import Blueprint

""" Instantiate an object of a Blueprint class """
""" Arguments for the constructor: blueprint name and module or
     package where the blueprint is located  """
main = Blueprint('main', __name__)

""" The modules are imported at the bottom to avoid errors due 
    to circular dependencies. See pag. 90 """ 
""" This is a relative import """
from . import views, errors, forms
