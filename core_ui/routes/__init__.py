from . import wallet

def init_app(app):
    app.register_blueprint(wallet.wallet_bp)
    app.add_url_rule('/', endpoint='index')
