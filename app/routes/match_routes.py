from flask import Blueprint, jsonify
from app.models import Match


bp = Blueprint('match', __name__, url_prefix='/match')

@bp.route('/<int:match_id>', methods=['GET'])
def get_match(match_id):
    match = Match.query.get(match_id)
    if match:
        return jsonify({"home_team": match.home_team, "away_team": match.away_team, "score": match.score}), 200
    return jsonify({"message": "Match not found"}), 404
