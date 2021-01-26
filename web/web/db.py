from os import environ

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    user = environ.get("POSTGRES_USER")
    password = environ.get("POSTGRES_PASSWORD")
    database = environ.get("POSTGRES_DB")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{user}:{password}@db:5432/{database}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)