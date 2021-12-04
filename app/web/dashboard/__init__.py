# --- Flask Imports
from flask import Blueprint

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# --- Dashboard route imports
from app.web.dashboard import routes
