# _*_ coding: utf-8 _*_
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)


app.config.from_object('app.settings')
# app.config.from_envvar('FLASKR_SETTINGS')

# 初始化数据库对象
db = SQLAlchemy(app)

# 初始化login_manager对象
login_manager = LoginManager




