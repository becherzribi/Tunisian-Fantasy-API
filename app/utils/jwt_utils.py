from datetime import datetime, timedelta
import jwt
from flask import current_app

def create_access_token(user_id):
    expiration = timedelta(minutes=15)
    payload = {
        "sub": str(user_id),  # Ensure the user_id is a string
        "exp": datetime.utcnow() + expiration,
        "type": "access",
    }
    return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")

def create_refresh_token(user_id):
    expiration = timedelta(days=7)
    payload = {
        "sub": str(user_id),  # Ensure the user_id is a string
        "exp": datetime.utcnow() + expiration,
        "type": "refresh",
    }
    return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")



def decode_token(token):
    try:
        payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        if not isinstance(payload.get("sub"), str):  # Validate that sub is a string
            return {"error": "Subject must be a string"}
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.DecodeError:
        return {"error": "Token is invalid"}
    except jwt.InvalidTokenError as e:
        return {"error": f"Token error: {str(e)}"}