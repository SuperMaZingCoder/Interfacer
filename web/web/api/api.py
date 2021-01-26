from os import environ

from flask import Blueprint
import requests

from web.api.models import UserPreferences


api_bp = Blueprint("api_bp", __name__)

token = environ.get("TOKEN")
headers = {
    "Authorization": f"Bot {token}"
}

@api_bp.route("/guilds/<int:guild_id>")
def guild(guild_id: int) -> dict:
    response = requests.get(f"https://discord.com/api/guilds/{guild_id}", headers=headers)
    return response.json()

@api_bp.route("/guilds/<int:guild_id>/members/<member_id>")
def member(guild_id: int, member_id: int) -> dict:
    if UserPreferences.query.filter_by(user_id=member_id, guild_id=guild_id).first():
        response = requests.get(f"https://discord.com/api/guilds/{guild_id}/members/{member_id}", headers=headers)
        return response.json()
    return {"detail": "user is not in database"}