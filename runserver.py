# _*_ coding: utf-8 _*_
# 加载配置文件
from app import app
from app.controller import main as main_blueprint

app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run()

