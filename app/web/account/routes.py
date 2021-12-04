# --- Flask Imports
from flask import redirect, url_for, render_template

# --- Web Imports
from app.web.account import bp
from app.web.account.forms import LoginForm

# --- App Imports


# --- Misc Imports


@bp.route('/login', methods=['GET'])
def login():
    form = LoginForm()

    return render_template('web/login.html', title='Login', form=form)

@bp.route('/forgot-psw', methods=['GET'])
def forgot_psw():
    return redirect(url_for('deubg.routes'))

@bp.route('/psw-reset/<token>', methods=['GET', 'POST'])
def psw_reset(token):
    return redirect(url_for('debug.routes'))
