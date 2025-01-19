from functools import wraps
from flask import Blueprint, request, jsonify, make_response
from app.db import db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.utils.jwt_utils import create_access_token, create_refresh_token, decode_token
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

bp = Blueprint('auth', __name__, url_prefix='/auth')

limiter = Limiter(key_func=get_remote_address)

# Register a new user (regular user only)
@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"message": "All fields are required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already registered"}), 409

    hashed_password = generate_password_hash(password)

    new_user = User(
        username=username,
        email=email,
        password_hash=hashed_password,
        is_admin=False  # Regular users are not admins by default
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# Login user (returns is_admin in the response)
@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)
        response = make_response(jsonify({
            "access_token": access_token,
            "is_admin": user.is_admin  # Include the user's role in the response
        }))
        response.set_cookie(
            "refresh_token",
            refresh_token,
            httponly=True,
            secure=True,  # Ensure HTTPS in production
            samesite='Strict'
        )
        return response, 200
    return jsonify({"message": "Invalid credentials"}), 401

# Refresh access token
@bp.route('/refresh', methods=['POST'])
def refresh_token():
    refresh_token = request.cookies.get("refresh_token")
    if not refresh_token:
        return jsonify({"message": "Refresh token is required"}), 400

    decoded = decode_token(refresh_token)
    if "error" in decoded:
        return jsonify({"message": decoded["error"]}), 401

    if decoded.get("type") != "refresh":
        return jsonify({"message": "Invalid token type"}), 401

    user_id = decoded.get("sub")
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    new_access_token = create_access_token(user.id)
    return jsonify({"access_token": new_access_token}), 200

# Logout user
@bp.route('/logout', methods=['POST'])
def logout():
    response = make_response(jsonify({"message": "Successfully logged out"}))
    response.delete_cookie("refresh_token")
    return response, 200