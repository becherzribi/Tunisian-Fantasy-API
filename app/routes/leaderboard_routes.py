from flask import Blueprint, jsonify
from app.models import FantasyTeam, User
from sqlalchemy.orm import joinedload


bp = Blueprint('leaderboard', __name__, url_prefix='/leaderboard')

@bp.route('/get', methods=['GET'])
def get_leaderboard():
    # Fetch fantasy teams with their associated users, ordered by points in descending order
    teams = FantasyTeam.query.options(joinedload(FantasyTeam.user)).order_by(FantasyTeam.points.desc()).all()

    # Build the leaderboard response
    leaderboard = [
        {
            "score": team.points,
            "team_name": team.name,
            "user_id": team.user.id,
            "username": team.user.username
            
        }
        for team in teams
    ]

    return jsonify(leaderboard), 200
