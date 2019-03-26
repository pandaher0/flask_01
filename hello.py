# coding:utf-8
# Author:hxj
from flask import Flask

app = Flask(__name__,
            static_url_path='/python')

@app.route('/')
def index():
    return '哈哈哈哈'


if __name__ == '__main__':
    app.run()


