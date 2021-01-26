from web.api import api

def init_app(app):
    app.register_blueprint(api.api_bp, url_prefix="/api")