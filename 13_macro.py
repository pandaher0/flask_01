# coding:utf-8
# Author:hxj

from flask import Flask, render_template, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adfadsfasdfasdf'

@app.route('/',methods=['GET','POST'])
def index():
    flash('adfasdfasdfa')
    return render_template('macro.html')


if __name__ == '__main__':
    app.run(debug=True)
