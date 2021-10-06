import os
basedir = os.path.abspath(os.path.dirname(__file__))

""" This base class defines settings that are commom to all configurations
    subclasses as they are class variables"""
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """ Additional way to allow the app to customize its configuration"""
    """ This is a static method"""
    @staticmethod
    def init_app(app):
        pass


""" This subclasses define settings that are specific to a configuration """
""" Additional configurations can be added as needed """ 
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

""" Each configuration tries to import the database URL from an environment
    variable, and when it is not available it sets a default one based on SQLite"""
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'

""" As you've seen, the SQLALCHEMY_DATABASE_URI variable os assigned different 
    values under each of the three configurations. This enables the app to use 
    a different database in each configuration  """
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


""" The different configurations are then registered in a config dictionary. 
    One of the configurations is registered as the default"""
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    
    'default': DevelopmentConfig
}