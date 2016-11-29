# _*_ coding: utf-8 _*_
# account.py
import io
from app import db
from flask import render_template, redirect, request, url_for, flash, abort, session, Flask, g
from flask_login import login_user
from . import main
from ..auth import auth
from ..backend.utils import check_code
from ..form.forms import LoginForm, RegistrationForm
from ..model.models import User


# 验证码功能
@main.route('/check_code', methods=['GET'])
def check_code_handler():
    stream = io.BytesIO()
    img, code = check_code.create_validate_code()
    img.save(stream, "png")
    print(code)
    # return "<h1>OK</h1>"
    return stream.getvalue()


@auth.route('/login', methods=['POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user and User.verify_password(form.password.data):
            print('========Success!=========')
    else:
        print('eeeeeeeeeeeeeeeeeee')
    status_dic = {'status': False}
    import json
    status_str = json.dumps(status_dic)
    return status_str


@auth.route('/register', methods=['POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        print(form.username.data, form.password.data)
    else:
        print('eeeeeeeeeeeeeeeeeee')
    status_dic = {'status': False}
    import json
    status_str = json.dumps(status_dic)
    return status_str

# 异常处理
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500