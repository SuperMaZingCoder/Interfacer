from web.db import db

class UserPreferences(db.Model):
    __table_name__ = "user_preferences"
    user_id = db.Column(db.BigInteger, nullable=False)
    guild_id = db.Column(db.BigInteger, nullable=False)
    __mapper_args__ = {
        "primary_key": [user_id, guild_id]
    }
