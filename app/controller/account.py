# _*_ coding: utf-8 _*_
# account.py
from app import db
import io
import json
from flask import render_template, redirect, request, url_for, flash, abort, session, Flask, g, Response
from flask_login import login_user, logout_user, login_required
from . import main
from ..auth import auth
from ..backend.utils import check_code
from ..forms import LoginForm, RegistrationForm
from ..models import User


# 验证码功能
@main.route('/check_code', methods=['GET'])
def check_code_handler():
    stream = io.BytesIO()
    img, code = check_code.create_validate_code()
    img.save(stream, "png")
    print(code)
    # return "<h1>OK</h1>"
    return stream.getvalue()





@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    status_dic = {'status': False}
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            nextx = request.args.get('next')
            print('---------------')
            print(nextx)
            status_dic['status'] = True
            status_str = json.dumps(status_dic)
            return status_str
        else:
            status_str = json.dumps(status_dic)
            return status_str
    elif request.method == 'GET':
        return redirect(url_for('main.index'))
    else:
        print('eeeeeeeeeeeeeeeeeee')
    status_str = json.dumps(status_dic)
    return status_str


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['POST'])
def register():
    print('============')
    print(request.cookies.get('username'))
    form = RegistrationForm(request.form)
    status_dic = {'status': False}
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data,
                    password=form.password.data,
                    group_id=1,
                    user_status=1,
                    email='admin@example.com',
                    phone='13800138001')
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        import time
        time.sleep(2)
        status_dic['status'] = True
        status_str = json.dumps(status_dic)
        return status_str
    else:
        status_str = json.dumps(status_dic)
        return status_str


# 异常处理
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
