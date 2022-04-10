# --- BASE CONFIG
import os
PROJ_DIR = os.path.dirname(os.path.abspath(f'{__file__}/..'))

# --- LOAD .flaskenv
from dotenv import load_dotenv
load_dotenv(f'{PROJ_DIR}/.flaskenv')


class BaseConfig:
    
    # Security Config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database Config
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    
    # Database Config
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(PROJ_DIR, 'database.db')


class ProdConfig(BaseConfig):
    pass
