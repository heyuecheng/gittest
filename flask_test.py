# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 22:35:45 2021

@author: heyuecheng
"""

from flask import Flask, escape, url_for,request
import PyQt5.QtWidgets


app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
