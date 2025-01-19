import tweepy
from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv


bp = Blueprint('twitter', __name__, url_prefix='/twitter')

# Load environment variables
load_dotenv()

# Load Twitter credentials from environment variables
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY,
    TWITTER_API_SECRET_KEY,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET
)
twitter_api = tweepy.API(auth)

@bp.route('/share', methods=['POST'])
def share_on_twitter():
    data = request.get_json()
    message = data.get('message')

    if not message:
        return jsonify({"message": "Message content is required"}), 400

    try:
        twitter_api.update_status(status=message)
        return jsonify({"message": "Shared successfully on Twitter"}), 200
    except tweepy.errors.Forbidden as e:
        # Handle forbidden tweets (e.g., duplicate content or policy violations)
        return jsonify({"message": f"Twitter API error (Forbidden): {e}"}), 403
    except tweepy.errors.TweepyException as e:
        # Handle all other Tweepy exceptions
        return jsonify({"message": f"Failed to share on Twitter: {e}"}), 500

# Debug: Check if environment variables are loaded
print("TWITTER_API_KEY:", TWITTER_API_KEY)
print("TWITTER_API_SECRET_KEY:", TWITTER_API_SECRET_KEY)
print("TWITTER_ACCESS_TOKEN:", TWITTER_ACCESS_TOKEN)
print("TWITTER_ACCESS_TOKEN_SECRET:", TWITTER_ACCESS_TOKEN_SECRET)
