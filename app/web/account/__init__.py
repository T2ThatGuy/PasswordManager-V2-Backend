from flask import Blueprint

bp = Blueprint('account', __name__)

# --- Account Imports
from app.web.account import routes