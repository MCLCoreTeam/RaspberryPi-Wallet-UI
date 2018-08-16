import os
DEBUG = True
CSRF_ENABLED = True
CSRF_SESSION_KEY = os.urandom(24)
SECRET_KEY = os.urandom(24)
WALLET_RPC_URL = "http://%s:%s@10.0.0.90:8332"%("StakerUI", "1triclypassword!")
UI_VERSION = '0.1.1'
