from flask import Flask

def create_app():
    from web import db, api, general
    app = Flask(__name__)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    db.init_app(app)
    api.init_app(app)
    general.init_app(app)
    return app