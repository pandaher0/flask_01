# coding:utf-8
# Author:hxj

from flask import Flask, session
from flask_script import Manager  # 启动命令的管理类

app = Flask(__name__)

# 创建管理类对象
manager = Manager(app)


@app.route('/index')
def index():
    print ('index 被执行')

    return 'index page'


if __name__ == '__main__':
    manager.run()
