import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')


USER_LENGHT = 16
REGEX_PATTERN = '^[A-Za-z0-9]*$'
DEFAULT_SHORT = 6
