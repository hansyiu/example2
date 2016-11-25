# _*_ coding: utf-8 _*_
from flask_sqlalchemy import SQLAlchemy
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username



# admin = User('admin', 'admin@example.com')
# db.create_all()  # 如果User表不存在则使用，否则注释这句
# db.session.add(admin)
# db.session.commit()  # 把修改写入到数据库
#
#
# User.query.all()
# User.query.filter_by(username='admin').first()
