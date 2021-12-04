# --- Flask Imports
from flask import redirect, url_for

# --- Dashboard Imports
from app.web.dashboard import bp

# --- App Imports

# --- Misc Imports


# --- Main Dashboard route
@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():

    return redirect(url_for('debug.routes'))
