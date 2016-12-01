# _*_ coding: utf-8 _*_
# from flask_wtf import Form
# from flask_wtf import FlaskForm as BaseForm
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp
from wtforms import ValidationError
from .models import User


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired(), Length(4, 20), Regexp('^[A-Za-z][A-Za-z0-9_]*$', 0,
                                                                                         '用户名只能由字母和下划线组成')])
    password = PasswordField('password', validators=[DataRequired(), Length(6, 20)])
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    username = StringField('username', validators=[DataRequired(), Length(4, 20), Regexp('^[A-Za-z][A-Za-z0-9_]*$', 0,
                                                                                         '用户名只能由字母和下划线组成')])
    password = PasswordField('password', validators=[DataRequired(), Length(6, 20)])
    submit = SubmitField('Register')

    # 自定义验证方法扩展
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')

    # def validate_email(self, field):
    #     if User.query.filter_by(email=field.data).first():
    #         raise ValidationError('Email地址已存在')



