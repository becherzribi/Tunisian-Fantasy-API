from app.app import create_app
from app.db import db
from app.models import FantasyTeam, Player, Match, User
from datetime import datetime
from werkzeug.security import generate_password_hash

def add_default_users():
    """
    Add default users to the database, including the first admin user (you).
    """
    print("Adding default users...")
    
    # Create the first admin user (you)
    admin_user = User(
        username="becher",  # Your username
        email="becher@gmail.com",  # Your email
        password_hash=generate_password_hash("becher123"),  # Your password
        is_admin=True  # You are an admin
    )

    # Create regular users
    regular_user1 = User(
        username="test_user1",
        email="user1@example.com",
        password_hash=generate_password_hash("securepassword"),
        is_admin=False  # Regular user
    )
    regular_user2 = User(
        username="test_user2",
        email="user2@example.com",
        password_hash=generate_password_hash("securepassword"),
        is_admin=False  # Regular user
    )

    try:
        db.session.add_all([admin_user, regular_user1, regular_user2])
        db.session.commit()
        print("Default users added!")
    except Exception as e:
        print(f"Error adding default users: {e}")
        db.session.rollback()

def seed_data():
    """
    Seed the database with fantasy teams, players, and matches.
    """
    # Fetch all users from the database
    print("Fetching users from the database...")
    users = db.session.query(User).all()

    if not users:
        print("No users found in the database. Please ensure users are added first.")
        return

    print("Users found in the database:")
    for user in users:
        print(f"User ID: {user.id}, Username: {user.username}, Is Admin: {user.is_admin}")

    # Create fantasy teams for existing users
    print("Creating fantasy teams...")
    teams = []
    if len(users) > 0:
        team1 = FantasyTeam(user_id=users[0].id, name="Becher's Team", points=100)  # Your team
        teams.append(team1)
    if len(users) > 1:
        team2 = FantasyTeam(user_id=users[1].id, name="User1's Team", points=85)
        teams.append(team2)
    if len(users) > 2:
        team3 = FantasyTeam(user_id=users[2].id, name="User2's Team", points=75)
        teams.append(team3)

    try:
        db.session.add_all(teams)
        db.session.commit()
        print("Fantasy teams created.")
    except Exception as e:
        print(f"Error creating fantasy teams: {e}")
        db.session.rollback()

    # Add players to teams
    print("Adding players to teams...")
    players = []
    if len(teams) > 0:
        player1 = Player(name="Player 1", position="Forward", goals=10, assists=5, is_captain=True, fantasy_points=50, fantasy_team_id=teams[0].id)
        player2 = Player(name="Player 2", position="Midfielder", goals=5, assists=7, fantasy_points=40, fantasy_team_id=teams[0].id)
        players.extend([player1, player2])
    if len(teams) > 1:
        player3 = Player(name="Player 3", position="Defender", goals=2, assists=3, fantasy_points=30, fantasy_team_id=teams[1].id)
        players.append(player3)
    if len(teams) > 2:
        player4 = Player(name="Player 4", position="Goalkeeper", goals=0, assists=1, fantasy_points=20, fantasy_team_id=teams[2].id)
        players.append(player4)

    try:
        db.session.add_all(players)
        db.session.commit()
        print("Players added.")
    except Exception as e:
        print(f"Error adding players: {e}")
        db.session.rollback()

    # Create matches and assign players to matches
    print("Creating matches and assigning players...")
    match1 = Match(home_team="Team A", away_team="Team B", score="2-1", date=datetime(2023, 12, 1))
    match2 = Match(home_team="Team C", away_team="Team D", score="1-3", date=datetime(2023, 12, 15))

    try:
        db.session.add_all([match1, match2])
        db.session.commit()

        # Assign players to matches
        if len(players) >= 2:
            match1.home_team_players.append(players[0])  # Player 1 plays for Team A
            match1.away_team_players.append(players[1])  # Player 2 plays for Team B
        if len(players) >= 4:
            match2.home_team_players.append(players[2])  # Player 3 plays for Team C
            match2.away_team_players.append(players[3])  # Player 4 plays for Team D

        db.session.commit()
        print("Matches created and players assigned.")
    except Exception as e:
        print(f"Error creating matches or assigning players: {e}")
        db.session.rollback()

    print("Database seeded with fantasy teams, players, and matches!")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
        add_default_users()  # Ensure users are present
        seed_data()  # Seed the database with fantasy teams, players, and matches