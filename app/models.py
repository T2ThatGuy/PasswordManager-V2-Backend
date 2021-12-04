# --- App Imports
from app import db, login

# --- Flask Imports
from flask_login import UserMixin


class User(UserMixin, db.Model):

    uid = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, unique=True)
    master_password = db.Column(db.String)
    email = db.Column(db.String)
    admin = db.Column(db.Boolean, default=False)

    # --- Relationships
    passwords = db.relationship("Password", backref='user')


class Password(UserMixin, db.Model):

    uid = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    password = db.Column(db.String)

    # --- Relationships
    user_uid = db.Column(db.String, db.ForeignKey('user.uid'))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))