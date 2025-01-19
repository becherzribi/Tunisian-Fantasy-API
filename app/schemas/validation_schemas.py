from marshmallow import Schema, fields 
 
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)  # Password is only for input
    is_admin = fields.Bool(dump_only=True)  # is_admin is only for output
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
 
class FantasyTeamSchema(Schema): 
    id = fields.Int(dump_only=True) 
    user_id = fields.Int(required=True) 
    name = fields.Str(required=True) 
    created_at = fields.DateTime(dump_only=True) 
    updated_at = fields.DateTime(dump_only=True) 
 
class PlayerSchema(Schema): 
    id = fields.Int(dump_only=True) 
    name = fields.Str(required=True) 
    position = fields.Str(required=True) 
    fantasy_team_id = fields.Int(required=False) 
    created_at = fields.DateTime(dump_only=True) 
    updated_at = fields.DateTime(dump_only=True) 
 
class MatchSchema(Schema): 
    id = fields.Int(dump_only=True) 
    home_team = fields.Str(required=True) 
    away_team = fields.Str(required=True) 
    score = fields.Str(required=False) 
    date = fields.DateTime(required=True) 
    created_at = fields.DateTime(dump_only=True) 
    updated_at = fields.DateTime(dump_only=True) 