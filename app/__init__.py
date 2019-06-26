from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config
from flask import Flask
import pymysql

pymysql.install_as_MySQLdb()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
