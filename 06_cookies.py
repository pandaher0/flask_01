# coding:utf-8
# Author:hxj

from flask import Flask, make_response, request
import json

app = Flask(__name__)


# post\get都可以在url中添加查询字符串
@app.route('/set_cookie')
def set_cookie():
    resp = make_response('success')
    # 默认临时有效，浏览器关闭失效
    resp.set_cookie('name', 'panda')
    resp.set_cookie('name', 'sunyu',max_age=3600)

    return resp

@app.route('/get_cookie')
def get_cookie():
    c = request.cookies.get('name')
    return c

@app.route('/del_cookie')
def del_cookie():
    resp = make_response('delete')
    resp.delete_cookie('name')
    return resp

if __name__ == '__main__':
    app.run(debug=True)
