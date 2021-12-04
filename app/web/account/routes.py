from app.web.account import bp

@bp.route('/test', methods=['GET'])
def test():

    return "{'Test': 'Example'}"