# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 11:18:18 2021

@author: manoranjan.parida
"""

import flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/home', methods = ['Get'])
def printYay():
    return "Yay its working"

@app.route('/home/work', methods = ['Get'])
def printWork():
    return "Yay API is working"

app.run(host='127.0.0.1', port = 8000)
# print(printYay())
