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


if __name__ == '__main__':
    app.run(debug=True)
