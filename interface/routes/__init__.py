from .wallet import wallet_bp

def init_app(app):
    app.register_blueprint(wallet_bp)
