# --- Flask Imports
from flask import Blueprint

bp = Blueprint('main', __name__)

# --- Web Main Imports
from app.web.main import routes
