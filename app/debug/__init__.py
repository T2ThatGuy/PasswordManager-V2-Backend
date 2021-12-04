# --- Flask imports
from flask import Blueprint

bp = Blueprint('debug', __name__, url_prefix='/debug')

# --- Main route imports
from app.debug import routes