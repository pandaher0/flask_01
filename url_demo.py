# coding:utf-8
# Author:hxj
from flask import Flask, current_app,redirect,url_for

app = Flask(__name__)


@app.route('/')
def index():
    return '哈哈哈哈'


# 限定请求方法
@app.route('/post_only', methods=['POST'])
def post_only():
    return 'post only page'


@app.route('/hello', methods=['GET'])
def hello1():
    return 'hello 1'


@app.route('/hello', methods=['POST'])
def hello2():
    return 'hello 2'


@app.route('/hi2')
@app.route('/hi1')
def hi():
    return 'hi'

@app.route('/login')
def login():
    # redirect 重定向
    # url_for 反向解析 与django的reverse相同
    return redirect(url_for('index'))



if __name__ == '__main__':
    print (app.url_map)
    app.run(debug=True)
