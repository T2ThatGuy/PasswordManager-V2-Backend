# --- Flask Imports
from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__, url_prefix='/v1')

# --- Api V1 Account Imports
from app.api.v1.account import api_account_bp

# --- Register API Blueprints
api_v1.register_blueprint(api_account_bp)
