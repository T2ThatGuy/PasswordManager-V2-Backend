# --- Flask Imports
from flask import Flask

# --- Flask Extension Imports
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

# --- Flask Blueprint Imports


# --- Misc Imports


# --- Logging Config
import logging
logger = logging.getLogger(__name__)


def make_app(config: str = 'api.config.DevConfig') -> Flask:

    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return "Hello Worl"
    
    return app

# --- Models Import
from api import models
