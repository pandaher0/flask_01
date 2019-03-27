# coding:utf-8
# Author:hxj

from flask import Flask, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfasdgfasgafdsafaeagasgasd'


# post\get都可以在url中添加查询字符串
@app.route('/login')
def login():
    session['name'] = 'panda'
    session['mobile'] = '18612345678'

    return 'login success'


@app.route('/index')
def index():
    name = session.get('name')
    return name


if __name__ == '__main__':
    app.run(debug=True)
