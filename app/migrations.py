from flask_migrate import Migrate
from app.db import db

migrate = Migrate()

def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)
