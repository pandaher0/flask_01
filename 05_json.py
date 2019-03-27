# coding:utf-8
# Author:hxj

from flask import Flask, jsonify
import json

app = Flask(__name__)


# post\get都可以在url中添加查询字符串
@app.route('/')
def index():
    data = {'city': 'beijing', 'name': 'sunyu'}
    # json_str = json.dumps(data)
    #
    # return json_str,400,{'Content-Type':'Application/Json'}
    # jsonify帮助转换为json数据并设置响应头
    # return jsonify(data)
    return jsonify(city='beijing',name='sunyu')

if __name__ == '__main__':
    app.run(debug=True)
