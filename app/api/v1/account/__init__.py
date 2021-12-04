# --- Flask Imports
from flask import Blueprint

api_account_bp = Blueprint('api_account', __name__)

# --- Account Imports
from app.api.v1.account import routes
