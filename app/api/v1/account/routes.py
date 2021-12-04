from app.api.v1.account import api_account_bp

@api_account_bp.route('/login', methods=['GET', 'POST'])
def login():
    return '<h1>Test Example</h1>'