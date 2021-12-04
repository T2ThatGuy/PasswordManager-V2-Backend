# --- Flask Imports
from flask import render_template

# --- Dashboard Imports
from app.web.dashboard import bp

# --- App Imports

# --- Misc Imports


# --- Main Dashboard route
@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():

    return render_template('web/base.html')
