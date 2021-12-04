from flask import Blueprint

web_bp = Blueprint('web', __name__)

# --- Register web blueprints
from app.web.main import bp as web_main_bp
from app.web.account import bp as web_account_bp
from app.web.dashboard import bp as web_dashboard_bp

web_bp.register_blueprint(web_main_bp)
web_bp.register_blueprint(web_account_bp)
web_bp.register_blueprint(web_dashboard_bp)
