import os

DEBUG = True

THREADS_PER_PAGE = 2

CSRF_ENABLED = True

CSRF_SESSION_KEY = os.urandom(24)

SECRET_KEY = os.urandom(24)
