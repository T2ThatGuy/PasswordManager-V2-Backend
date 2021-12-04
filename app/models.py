# --- App Imports
from app import db

# --- Flask Imports
from flask_login import UserMixin


class User(UserMixin, db.Model):

    uid = db.Column(db.String, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)


class Password(UserMixin, db.Model):

    uid = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    password = db.Column(db.String)