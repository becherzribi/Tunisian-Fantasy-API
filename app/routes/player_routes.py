from flask import Blueprint, request, jsonify   
from app.models import Player, FantasyTeam, Match
from app.db import db  # Correct import of db



bp = Blueprint('player', __name__, url_prefix='/player')


@bp.route('/add', methods=['POST']) 
def add_player():
    data = request.get_json()
    team_id = data.get('team_id')
    name = data.get('name')
    position = data.get('position')
    goals= data.get('goals')
    assists = data.get('assists')
    is_captain = data.get('is_captain')
    fantasy_points = data.get('fantasy_points')
    fantasy_team_id= data.get('fantasy_team_id')

    team = FantasyTeam.query.get(team_id)
    
    if not team:
        return jsonify({"message": "Fantasy team not found"}), 404
    
    new_player = Player(name=name, position=position, team=team, goals=goals, assists=assists, is_captain=is_captain, fantasy_points=fantasy_points, fantasy_team_id=team_id)

    db.session.add(new_player)  # Ensure db is properly imported
    db.session.commit()
    return jsonify({"message": "Player added successfully"}), 201

@bp.route('/<int:team_id>/players', methods=['GET'])
def get_players(team_id):
    team = FantasyTeam.query.get(team_id)
    if not team:
        return jsonify({"message": "Fantasy team not found"}), 404

    players = Player.query.filter_by(fantasy_team_id=team_id).all()
    result = [{"id": player.id, "name": player.name, "position": player.position, "goals": player.goals, "assists": player.assists, "is_captain": player.is_captain, "fantasy_points": player.fantasy_points} for player in players]
    
    return jsonify(result), 200

@bp.route('/update/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    data = request.get_json()
    player = Player.query.get(player_id)

    if not player:
        return jsonify({"message": "Player not found"}), 404

    player.name = data.get('name', player.name)
    player.position = data.get('position', player.position)
    player.goals = data.get('goals', player.goals)
    player.assists = data.get('assists', player.assists)
    player.is_captain = data.get('is_captain', player.is_captain)
    player.fantasy_points = data.get('fantasy_points', player.fantasy_points)
    db.session.commit()
    
    return jsonify({"message": "Player updated successfully"}), 200

@bp.route('/delete/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    player = Player.query.get(player_id)

    if not player:
        return jsonify({"message": "Player not found"}), 404

    db.session.delete(player)
    db.session.commit()
    
    return jsonify({"message": "Player deleted successfully"}), 200
