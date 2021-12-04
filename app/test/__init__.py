from flask import Blueprint

test_bp = Blueprint('test_bp', __name__)
account_bp = Blueprint('account_bp', __name__)

account_bp.route('/login', methods=['GET'])
def login():
    return 'Test login page'

test_bp.register_blueprint(account_bp, url_prefix='/account')
