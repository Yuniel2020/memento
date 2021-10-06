import unittest
from flask import current_app
from app import create_app, db

class BasicTestCase(unittest.TestCase):
    def setUp(self):                                          #   setUp and tearDown run after each test  
        self.app = create_app("testing")                      #   setUp tries to create an environment similar to that of running the application
        self.app_context = self.app.app_context()             #   It first create an app configured for testing and activates it context
        self.app_context.push()                               #   That ensures that tests have access to current_app
        db.create_all()                                       #   Then it creates a brand-new data base for the tests using FLask-SQLAlchemy create_all()

    def tearDown(self):                                       #   The database and the app context are remove in the tearDown method
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):                                 # Each method which name begins with test_ is execute as a test
        self.assertFalse(current_app is None)                  # This first method ensures that the app instance exists.

    def test_app_is_testing(self):                             # This method ensures that the app is running under the testing config
        self.assertTrue(current_app.config["TESTING"])


# To run the unit tests, a custom command can be added to the memento.py
# script

