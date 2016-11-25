# _*_ coding: utf-8 _*_
# account.py
import io
from app import app,db
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g
from . import main
from ..backend.utils import check_code


# 验证码功能
@main.route('/check_code', methods=['GET'])
def check_code_handler():
    stream = io.BytesIO()
    img, code = check_code.create_validate_code()
    img.save(stream, "png")
    print(code)
    # return "<h1>OK</h1>"
    return stream.getvalue()

@main.route('')



# 异常处理
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500