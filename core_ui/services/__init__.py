from flask_wallet_rpc import Walletrpc, wallet
rpc = Walletrpc()

def init_app(app):
    rpc.init_app(app)
