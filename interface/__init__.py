import os
from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config=None):
    from . import routes, services

    app = Flask(__name__)

    app.config.from_object('settings')

    if 'FLASK_CONF' in os.environ:
        app.config.from_envvar('FLASK_CONF')

    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    routes.init_app(app)
    services.init_app(app)
    bootstrap.init_app(app)

    return app
