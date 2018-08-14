from .rpcrequest import Rpcrequest, wallet
rpc = Rpcrequest()
def init_app(app):
    rpc.init_app(app)
