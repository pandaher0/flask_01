# coding:utf-8
# Author:hxj

from flask import Flask, request, abort, Response

app = Flask(__name__)


# post\get都可以在url中添加查询字符串
@app.route('/', methods=['GET'])
def login():
    name = ''
    pwd = ''
    if name != 'sunyu' or pwd != 'admin':
        # abort函数可以立即终止视图函数执行
        # 并返回给前端特定信息
        # 1.传递状态码信息 必须是标准http状态码
        abort(404)
        # 2.传递相应提信息
        # abort(Response('login failed'))

    return 'login success'


# 自定义的处理错误方法
@app.errorhandler
def handle_404_error(err):
    return '出现404错误，%s' % err


if __name__ == '__main__':
    app.run(debug=True)
