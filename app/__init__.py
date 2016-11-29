# _*_ coding: utf-8 _*_
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.settings')
    # app.config.from_envvar('FLASKR_SETTINGS')

    # 初始化数据库对象
    db.init_app(app)

    # 初始化login_manager对象
    login_manager.init_app(app)

    # 初始化蓝本
    from .controller import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app




