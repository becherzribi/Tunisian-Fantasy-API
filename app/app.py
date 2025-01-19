from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api
from flask_swagger_ui import get_swaggerui_blueprint
from app.db import db
from app.models import User, Player, Match
import os
from dotenv import load_dotenv

# Import blueprints
from app.routes.auth_routes import bp as auth_bp
from app.routes.fantasy_routes import bp as fantasy_bp
from app.routes.leaderboard_routes import bp as leaderboard_bp
from app.routes.match_routes import bp as match_bp
from app.routes.player_routes import bp as player_bp
from app.routes.twitter_routes import bp as twitter_bp
from app.routes.admin_routes import bp as admin_bp

load_dotenv()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Flask-Smorest and OpenAPI Configuration
    app.config["API_TITLE"] = "Tunisian Fantasy API"
    app.config["API_VERSION"] = "1.0"
    app.config["OPENAPI_VERSION"] = "3.0.3"  # Ensure OpenAPI version is correct
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # Database Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_secret_key")

    # Initialize Flask-Smorest API
    api = Api(app)

    # Swagger UI Setup
    SWAGGER_URL = "/api/docs"  # Swagger UI endpoint
    API_URL = "/static/swagger.json"  # Path to your OpenAPI spec file
    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={"app_name": "Tunisian Fantasy API"}
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    # Register Blueprints for your API endpoints
    app.register_blueprint(auth_bp)
    app.register_blueprint(fantasy_bp)
    app.register_blueprint(leaderboard_bp)
    app.register_blueprint(match_bp)
    app.register_blueprint(player_bp)
    app.register_blueprint(twitter_bp)
    app.register_blueprint(admin_bp)

    # Initialize database and migrations
    db.init_app(app)
    migrate.init_app(app, db)

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app
