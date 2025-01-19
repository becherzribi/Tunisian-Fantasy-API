from flask import Blueprint, request, jsonify
from app.db import db
from app.models import FantasyTeam, User  # Ensure User is imported


bp = Blueprint('fantasy', __name__, url_prefix='/fantasy')

@bp.route('/create', methods=['POST'])
def create_fantasy_team():
    data = request.get_json()
    user_id = data.get('user_id')
    team_name = data.get('team_name')

    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    if not team_name:
        return jsonify({"message": "Team name is required"}), 400

    new_team = FantasyTeam(user_id=user_id, name=team_name)
    db.session.add(new_team)
    db.session.commit()

    return jsonify({"message": "Fantasy team created successfully"}), 201


@bp.route('/update/<int:team_id>', methods=['PUT'])
def update_fantasy_team(team_id):
    data = request.get_json()
    new_team_name = data.get('team_name')
    new_points = data.get('points')

    # Retrieve the fantasy team by ID
    team = FantasyTeam.query.get(team_id)
    
    if not team:
        return jsonify({"message": "Fantasy team not found"}), 404

    # Update the team's name if provided
    if new_team_name:
        team.name = new_team_name

    # Update the team's points if provided
    if new_points is not None:
        team.points = new_points

    # Commit changes to the database
    db.session.commit()

    return jsonify({
        "message": f"Fantasy team updated successfully. New Name: '{team.name}', New Points: {team.points}"
    }), 200

@bp.route('/delete/<int:team_id>', methods=['DELETE'])
def delete_fantasy_team(team_id):
    """Endpoint to delete a fantasy team by ID."""
    team = FantasyTeam.query.get(team_id)
    
    if not team:
        return jsonify({"message": "Fantasy team not found"}), 404
    
    db.session.delete(team)
    db.session.commit()
    return jsonify({"message": f"Fantasy team '{team.name}' deleted successfully"}), 200