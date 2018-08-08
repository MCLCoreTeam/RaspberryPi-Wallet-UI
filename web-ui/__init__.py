import os
from flask import Flask
from flask_bootstrap import Bootstrap

def create_app(test_config=None):
    root_dir = os.path.expanduser('~/pos-ui')
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return 'Hello, World!'

    return app
