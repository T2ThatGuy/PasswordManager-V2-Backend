import os


class BaseConfig:

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    WORKDIR = os.path.abspath(os.path.dirname(__file__))


class DevConfig(BaseConfig):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT') or 25


class ProductionConfig(BaseConfig):

    pass