from flask import Blueprint, render_template

from web.api.models import UserPreferences


general_bp = Blueprint("general_bp", __name__, template_folder="templates")

@general_bp.route("/")
def index():
    return render_template("general/index.html")