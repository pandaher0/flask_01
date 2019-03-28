# coding:utf-8
# Author:hxj

from flask import Flask, render_template, request, redirect, url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfasdfasdfasdfasdfadsf'


# 定义表单模型类
class RegisterForm(FlaskForm):
    """自定义注册表单模型类"""
    username = StringField(label=u'用户', validators=[DataRequired(u'用户名不能为空')])
    password = PasswordField(label=u'密码', validators=[DataRequired(u'密码不能为空')])
    password02 = PasswordField(label=u'确认密码', validators=[DataRequired(u'密码不能为空'), EqualTo('password', u'两次密码不同')])
    submit = SubmitField(label=u'提交')


@app.route('/register', methods=['GET', 'POST'])
def register():
    # 创建表单对象
    form = RegisterForm()
    # 判断form表单数据是否合理
    if form.validate_on_submit():
        # 表示验证合格
        username = form.username.data
        password = form.password.data
        password02 = form.password02.data
        print (username, password, password02)
        session['username'] = username
        return redirect(url_for('index'))

    return render_template('register.html', form=form)


@app.route('/')
def index():
    username = session.get('username','')
    return username


if __name__ == '__main__':
    app.run(debug=True)
