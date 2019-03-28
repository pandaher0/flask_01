# coding:utf-8
# Author:hxj

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    data = {
        'name': 'panda',
        'age': 18,
        'mydict': {'city': 'beijing'},
        'mylist': [1, 2, 3, 4, 5],
        'myint':0
    }

    return render_template('index.html', **data)

# 自定义过滤器
def list_step_2(list):
    return list[::2]

# 注册过滤器
app.add_template_filter(list_step_2,'li2')


@app.template_filter('li3')
def list_step_3(list):
    return list[::3]

if __name__ == '__main__':
    app.run(debug=True)
