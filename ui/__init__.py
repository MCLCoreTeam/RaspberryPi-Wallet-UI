import os
from flask import Flask
from flask_bootstrap import Bootstrap

def create_app(test_config=None):
    root_dir = os.path.expanduser('~/code/ui')
    app = Flask(__name__, instance_path=root_dir)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        return 'Hello, World!'

    return app
