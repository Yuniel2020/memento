# from werkzeug.exceptions import HTTPException
from . import main


""" If errorhandler decorator (@app.errorhandler) is used inside a blueprint,
     the handler will be invoked only for error that originate in the routes
    defined by the blueprint """
""" To install app-wide error handlers, the app_errorhandler decorator 
    must be used instead"""
@main.app_errorhandler(404)
def page_not_found(e):
    return 'This page does not exist', 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return 'Internal server error', 500