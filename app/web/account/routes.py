# --- Flask Imports
from flask import redirect, url_for

# --- Web Imports
from app.web.account import bp

# --- App Imports


# --- Misc Imports


@bp.route('/login', methods=['GET'])
def login():
    return redirect(url_for('debug.routes'))

@bp.route('/forgot-psw', methods=['GET'])
def forgot_psw():
    return redirect(url_for('deubg.routes'))

@bp.route('/psw-reset/<token>', methods=['GET', 'POST'])
def psw_reset(token):
    return redirect(url_for('debug.routes'))
