# coding:utf-8
# Author:hxj
from flask import Flask,current_app

app = Flask(__name__,
            static_url_path='/python',  # 访问静态资源前缀，默认/static
            static_folder='static',
            template_folder='templates')


# 1. 使用配置文件
# app.config.from_pyfile("config.cfg")

class Config(object):
    DEBUG = True
    NAME = 'python'


# 2. 使用对象配置参数
app.config.from_object(Config)


# 3. 直接操作config
# app.config['DEBUG'] = True


@app.route('/')
def index():
    # print(app.config.get("NAME"))
    print(current_app.config.get("NAME"))
    return '哈哈哈哈'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
