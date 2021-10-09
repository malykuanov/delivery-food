from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import DevelopmentConfig


db = SQLAlchemy()
migrate = Migrate()

login_manager = LoginManager()
login_manager.login_view = '.login'
login_manager.login_message = 'Необходима авторизация'
login_manager.login_message_category = 'success'


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    return app