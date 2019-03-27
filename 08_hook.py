# coding:utf-8
# Author:hxj

from flask import Flask, session

app = Flask(__name__)

# 执行顺序
# handle_before_first_request
# handle_before_request
# index 被执行
# handle_after_request
# handle_teardown_request



@app.route('/index')
def index():
    print ('index 被执行')
    # a = 1/0
    return 'index page'


@app.before_first_request
def handle_before_first_request():
    """第一次请求前执行"""
    print ('handle_before_first_request')


@app.before_request
def handle_before_request():
    """每次请求前执行"""
    print ('handle_before_request')

@app.after_request
def handle_after_request(response):
    """无异常，请求后执行"""
    print ('handle_after_request')
    return response

# teardown不能运行在debug模式，工作在非调试模式时，debug=false
@app.teardown_request
def handle_teardown_request(response):
    """有异常，请求后执行"""
    print ('handle_teardown_request')
    return response





if __name__ == '__main__':
    app.run()
