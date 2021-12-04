# --- App Imports
from app import create_app
app = create_app()
app.app_context().push()

from app import db

from app.models import User

# --- Misc Imports
import uuid

if User.query.all():
    create_new = input(f"Database file at ({app.config['SQLALCHEMY_DATABASE_URI']}) already has users created are you sure you would like to add the default users? (Enter Y/y for Yes anything else for No) ")

    if not create_new.strip().lower() in ["y", "yes"]:
        quit()

default_user_data = [

    {
        "username": "T2ThatGuy",
        "admin": True
    },
    {
        "username": "CharlieS",
        "admin": False
    }

]

print("\n\n[INFO] Adding default users\n")

for user in default_user_data:

    user_res = User.query.filter_by(username=user['username']).first()

    if user_res:
        print(f"[ERROR] Could not create user {user['username']} as they already exist in the database")
        continue

    new_user = User(uid=f'U+{uuid.uuid4()}', username=user['username'], master_password="12345", email=f"{user['username']}@test.com", admin=user['admin'])
    db.session.add(new_user)

    print(f"[SUCCESS] Added {new_user.username} to database with ID {new_user.uid}")

db.session.commit()
