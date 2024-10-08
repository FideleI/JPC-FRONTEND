import os 
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,'.env'))


class Config:
    """Base config"""
    SECRET_KEY = os.getenv("SECRET_KEY")
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
