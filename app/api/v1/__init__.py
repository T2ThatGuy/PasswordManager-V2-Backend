from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__, url_prefix='/v1')

from app.api.v1.account import api_account_bp

api_v1.register_blueprint(api_account_bp)