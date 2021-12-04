# --- Create api blueprint
from flask import Blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api')

# --- API Version imports
from app.api.v1 import api_v1

# --- Register api versions
api_bp.register_blueprint(api_v1)
