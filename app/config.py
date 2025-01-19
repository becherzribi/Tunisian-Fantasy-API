import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'  # Use a secure secret key
    API_TITLE = "Fantasy League API"  # Title of your API
    API_VERSION = "1.0"              # API version
    OPENAPI_VERSION = "3.0.3"        # OpenAPI specification version
    OPENAPI_URL_PREFIX = "/"         # Base URL prefix for Swagger UI
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"  # Path for Swagger UI
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  # Swagger UI CDN URL



