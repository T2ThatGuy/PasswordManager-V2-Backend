# --- Flask Imports
from flask import request, jsonify
from flask_jwt_extended import jwt_required

# --- API V1 Imports
from app.api.v1.account import api_account_bp

# --- App Imports


@api_account_bp.route('/login', methods=['GET'])
def login():
    return '<h1>Test Example</h1>'