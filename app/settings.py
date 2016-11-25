# _*_ coding: utf-8 _*_
# 默认开启debug，正式上线关闭debug
DEBUG = True

# 关闭Flask-SQLAlchemy事件系统告警
SQLALCHEMY_TRACK_MODIFICATIONS = False

# CSRF密匙
SECRET_KEY = 'A!DGGSddgeqedjkdfjsokjiewlkr'

# 数据库连接信息
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask'

