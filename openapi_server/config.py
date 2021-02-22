import os

class Config(object):
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = 'not_totally_secret'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']