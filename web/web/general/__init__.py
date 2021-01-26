from web.general.general import general_bp

def init_app(app):
    app.register_blueprint(general_bp)