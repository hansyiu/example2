# _*_ coding: utf-8 _*_
# home.py
from app import db
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g
from . import main
from flask_login import login_required

@main.route('/')
def index():
    return render_template('index.html')


# @main.route('/index')
# def index():
#     return render_template('index.html')


@main.route('/show')
@login_required
def show():
    return render_template('show.html')
