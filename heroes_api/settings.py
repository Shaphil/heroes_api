import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = 'heroes.db'
    DB_PATH = os.path.join(basedir, DB_NAME)
    SECRET_KEY = 'alpha neutron star'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False
