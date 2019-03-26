# coding:utf-8
# Author:hxj
from flask import Flask

app = Flask(__name__,
            static_url_path='/python',#访问静态资源前缀，默认/static
            static_folder='static',
            template_folder='templates')

@app.route('/')
def index():
    return '哈哈哈哈'


if __name__ == '__main__':
    app.run()


