# --- Flask Imports

# --- Api Imports
from api import db

# --- Misc Imports
from uuid import uuid4

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(32), primary_key=True, default=lambda: uuid4().hex)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<USER: {self.username}>'

    def to_json(self, show_email: bool = False) -> dict[str, str]:
        payload = {
            "id": self.id,
            "username": self.username
        }

        if show_email:
            payload['email'] = self.email

        return payload