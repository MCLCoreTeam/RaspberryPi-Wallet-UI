import os
DEBUG = True
CSRF_ENABLED = True
CSRF_SESSION_KEY = os.urandom(24)
SECRET_KEY = os.urandom(24)
WALLET_RPC_URL = "http://%s:%s@pricebox:8332"%("StakerUI", "1triclypassword!")
UI_VERSION = 'v0.1.1'
