from flask import Blueprint

web_bp = Blueprint('web', __name__)

# --- Register web blueprints
from app.web.account import bp as web_account_bp

web_bp.register_blueprint(web_account_bp)