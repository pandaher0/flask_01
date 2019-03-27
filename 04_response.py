# coding:utf-8
# Author:hxj

from flask import Flask, request, make_response

app = Flask(__name__)


# post\get都可以在url中添加查询字符串
@app.route('/')
def index():
    # 1.使用元祖、字典，返回自定义响应信息
    # 响应体  状态码  响应头
    # return 'index page', 400, [('city', 'beijing'), ('name', 'panda')]
    # return 'index page', 400, {'city': 'beijing', 'name': 'panda'}
    # return 'index page', 666, {'city': 'beijing', 'name': 'panda'}
    # return 'index page', '666 hahaha', {'city': 'beijing', 'name': 'panda'}

    # 2.使用mske_response 来构造信息
    resp = make_response('index page 2')
    resp.status = '999 oooo'
    resp.header = {'city': 'beijing', 'name': 'panda'}
    return resp


if __name__ == '__main__':
    app.run(debug=True)
