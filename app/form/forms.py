# _*_ coding: utf-8 _*_
# from flask_wtf import Form
# from flask_wtf import FlaskForm as BaseForm
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired(), Length(4, 20)])
    password = PasswordField('password', validators=[DataRequired(), Length(6, 20)])
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    username = StringField('username', validators=[DataRequired(), Length(4, 20)])
    password = PasswordField('password', validators=[DataRequired(), Length(6, 20)])
    submit = SubmitField('Register')
