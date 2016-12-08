# _*_ coding: utf-8 _*_
# home.py
from app import db
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g
from . import main
from flask_login import login_required, current_user
from ..forms import LoginForm
from ..backend.utils.token_create import TToken


@main.route('/')
def index():
    form = LoginForm()
    return render_template('index.html', form=form)


@main.route('/api/get_key', methods=['GET'])
@login_required
def get_key():
    username = session.get('username')
    if username:
        ttoken = TToken(username)
        token_bytes = ttoken.generate_auth_token(expiration=300)
        token_str = str(token_bytes, encoding='utf-8')
        print(token_str)
    return '<h1>get_key</h1>'


@main.route('/show')
@login_required
def show():
    form = LoginForm()
    return render_template('show.html', form=form)
