# _*_ coding: utf-8 _*_
# home.py
from app import app,db
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g
from . import main


@main.route('/')
def hello_world():
    return render_template('index.html')


@main.route('/index')
def index():
    return render_template('index.html')


@main.route('/show')
def show():
    return render_template('show.html')
