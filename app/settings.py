# _*_ coding: utf-8 _*_
# 默认开启debug，正式上线关闭debug
DEBUG = True

# 关闭Flask-SQLAlchemy事件系统告警
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 密匙,用于session加密
SECRET_KEY = '$6HiA5|W0?t>y!Hbb+nf$eBR]/;gox(>8iAeHQ~-wHoi4CrsMa5'

# 数据库连接信息
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask'

