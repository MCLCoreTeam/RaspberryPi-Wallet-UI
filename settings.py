import os

CSRF_ENABLED = True
CSRF_SESSION_KEY = os.urandom(24)
SECRET_KEY = os.urandom(24)
WALLET_RPC_URL = "http://%s:%s@127.0.0.1:8332"%("Rpcuser", "Rpcpassword")
