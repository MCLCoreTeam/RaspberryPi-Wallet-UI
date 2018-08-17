from flask_wallet_rpc import Walletrpc, wallet
rpc_call = Walletrpc()

def init_app(app):
    rpc_call.init_app(app)
