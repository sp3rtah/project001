from flask_sqlalchemy import SQLAlchemy
from flask_loguru import Logger
from .config import Config
from flask import Flask

db = SQLAlchemy()
logger = Logger()


def create_app(_config=Config):
    app = Flask(__name__)
    app.config.from_object(_config)

    # configure logger
    logger.init_app(app, {'LOG_PATH': app.config['LOG_PATH'], 'LOG_NAME': 'session.log'})

    # configure db
    from main.homepage.models import Transaction
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # configure blueprints
    from main.homepage import homepage_blueprint
    from main.errors import error_blueprint

    app.register_blueprint(error_blueprint)
    app.register_blueprint(homepage_blueprint, url_prefix='/')

    return app
