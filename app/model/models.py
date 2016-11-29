# _*_ coding: utf-8 _*_
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='group', lazy='dynamic')

    def __repr__(self):
        return '<Group %r>' % self.group


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
    user_status = db.Column(db.SmallInteger, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    phone = db.Column(db.String(11), unique=True)
    reg_date = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)

    @property
    def password(self):
        raise AssertionError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

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
