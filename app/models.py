from datetime import datetime 
from app.db import db 
 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    fantasy_teams = db.relationship('FantasyTeam', back_populates='user', lazy=True)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.username}>'
 
 
class FantasyTeam(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    name = db.Column(db.String(100), nullable=False) 
    points = db.Column(db.Integer, default=0)  # Add points attribute 
    players = db.relationship('Player', backref='team', lazy=True, cascade="all, delete-orphan") 
    user = db.relationship('User', backref=db.backref('fantasy_teams', lazy=True)) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
    user = db.relationship('User', back_populates='fantasy_teams') 
    def __repr__(self): 
        return f'<FantasyTeam {self.name}>' 
 
class Player(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(100), nullable=False) 
    position = db.Column(db.String(50), nullable=False) 
    goals = db.Column(db.Integer, default=0)  # Add goals attribute 
    assists = db.Column(db.Integer, default=0)  # Add assists attribute 
    is_captain = db.Column(db.Boolean, default=False)  # Add captain boolean 
    fantasy_points = db.Column(db.Integer, default=0)  # Add fantasy points attribute 
    fantasy_team_id = db.Column(db.Integer, db.ForeignKey('fantasy_team.id'), nullable=True) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
 
    def __repr__(self): 
        return f'<Player {self.name}, Position {self.position}>' 
 
# Association tables for home and away team players 
match_home_team = db.Table( 
    'match_home_team', 
    db.Column('match_id', db.Integer, db.ForeignKey('match.id'), 
primary_key=True), 
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'), 
primary_key=True) 
) 
 
match_away_team = db.Table( 
    'match_away_team', 
    db.Column('match_id', db.Integer, db.ForeignKey('match.id'), 
primary_key=True), 
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'), 
primary_key=True) 
) 
 
class Match(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    home_team = db.Column(db.String(100), nullable=False) 
    away_team = db.Column(db.String(100), nullable=False) 
    score = db.Column(db.String(10), nullable=True) 
    date = db.Column(db.DateTime, default=datetime.utcnow) 
 
    home_team_players = db.relationship( 
        'Player', 
        secondary=match_home_team, 
        backref=db.backref('home_matches', lazy='dynamic'), 
        lazy='dynamic' 
    ) 
 
    away_team_players = db.relationship( 
        'Player', 
        secondary=match_away_team, 
        backref=db.backref('away_matches', lazy='dynamic'), 
        lazy='dynamic' 
    ) 
 
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
 
    def __repr__(self): 
        return f'<Match {self.home_team} vs {self.away_team} on {self.date}>' 