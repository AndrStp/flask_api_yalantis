from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name: str='default'):
    """Factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db, directory='app/migrations')    

    # api blueprint
    from app.api import api
    app.register_blueprint(api, url_prefix='/api')

    return app
