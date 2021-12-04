# --- Flask Import and Setup
from flask import Flask, url_for
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_jwt_extended import JWTManager

from config import DevConfig

bootstrap = Bootstrap()
mail = Mail()
jwt = JWTManager()

login = LoginManager()
login.login_view = 'account.login'

# --- Database Imports and Setup
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

db = SQLAlchemy()
migrate = Migrate()

# --- Blueprints
from app.api import api_bp
from app.web import web_bp
from app.debug import bp as debug_bp

def create_app( config_class=DevConfig ):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    login.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)

    app.extensions['mail'].debug = 0

    # --- Register api and web blueprints
    app.register_blueprint(api_bp)
    app.register_blueprint(web_bp)
    app.register_blueprint(debug_bp)

    return app

# --- Model Imports
from app import models
