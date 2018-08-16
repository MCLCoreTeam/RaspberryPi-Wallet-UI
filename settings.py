import os
DEBUG = True
CSRF_ENABLED = True
CSRF_SESSION_KEY = os.urandom(24)
SECRET_KEY = os.urandom(24)
WALLET_RPC_URL = "http://%s:%s@127.0.0.1:8332"%("Rpcuser", "Rpcpassword")
UI_VERSION = '0.1.1'
