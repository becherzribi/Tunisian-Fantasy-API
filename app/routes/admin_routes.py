from flask import Blueprint, request, jsonify
from app.db import db
from app.models import User
from app.utils.jwt_utils import decode_token
from functools import wraps
from werkzeug.security import generate_password_hash

bp = Blueprint('admin', __name__, url_prefix='/admin')

# Admin required decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the token from the request headers
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Authorization token is required"}), 401

        # Remove the "Bearer " prefix if present
        if token.startswith("Bearer "):
            token = token[7:]

        # Decode the token to get the user ID
        decoded = decode_token(token)
        if "error" in decoded:
            return jsonify({"message": decoded["error"]}), 401

        # Get the user from the database
        user_id = decoded.get("sub")
        user = User.query.get(user_id)

        # Check if the user is an admin
        if not user or not user.is_admin:
            return jsonify({"message": "Admin access required"}), 403

        # If the user is an admin, proceed with the original function
        return f(*args, **kwargs)

    return decorated_function

# Register a new admin (only accessible by existing admins)
@bp.route('/register', methods=['POST'])
@admin_required
def register_admin():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"message": "All fields are required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already registered"}), 409

    hashed_password = generate_password_hash(password)

    new_admin = User(
        username=username,
        email=email,
        password_hash=hashed_password,
        is_admin=True  # Set the user as an admin
    )
    db.session.add(new_admin)
    db.session.commit()
    return jsonify({"message": "Admin registered successfully"}), 201

# Get all users (Admin only)
@bp.route('/users', methods=['GET'])
@admin_required
def get_all_users():
    users = User.query.all()
    result = [{"id": user.id, "username": user.username, "email": user.email, "is_admin": user.is_admin} for user in users]
    return jsonify(result), 200

# Delete a user (Admin only)
@bp.route('/users/<int:user_id>', methods=['DELETE'])  # Fixed route
@admin_required
def delete_user(user_id):  # `user_id` is now passed dynamically
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200

# Make a user an admin (Admin only)
@bp.route('/users/<int:user_id>/make_admin', methods=['PUT'])  # Fixed route
@admin_required
def make_admin(user_id):  # `user_id` is now passed dynamically
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    user.is_admin = True
    db.session.commit()
    return jsonify({"message": "User is now an admin"}), 200
