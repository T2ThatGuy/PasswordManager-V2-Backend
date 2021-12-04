# --- Flask Imports
from flask import redirect, url_for

# --- Web Main Imports
from app.web.main import bp

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def main_index():

    return redirect(url_for('dashboard.index'))
