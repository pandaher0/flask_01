# coding:utf-8
# Author:hxj
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@39.106.44.166:3306/booktest02'
    # 自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 显示原始sql语句
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'asdfasdfasdfadfasdfadf'


app.config.from_object(Config)
db = SQLAlchemy(app)

manager = Manager(app)
# 创建迁移工具对象
Migrate(app, db)
manager.add_command('db', MigrateCommand)


# author
class Author(db.Model):
    __tablename__ = 'tbl_authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    books = db.relationship('Book', backref='author')
    email = db.Column(db.String(64))
    mobile = db.Column(db.String(64))


# book
class Book(db.Model):
    __tablename__ = 'tbl_books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('tbl_authors.id'))


class BookForm(FlaskForm):
    author = StringField(label=u'作者名称', validators=[DataRequired(u'作者名称不能为空')])
    book = StringField(label=u'图书名称', validators=[DataRequired(u'图书名称不能为空')])
    submit = SubmitField(label=u'提交')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = BookForm()
    if form.validate_on_submit():
        authorname = form.author.data
        bookname = form.book.data

        author = Author(name=authorname)
        db.session.add(author)
        db.session.commit()

        book = Book(name=bookname, author_id=author.id)
        # book = Book(name=bookname, author=author)
        db.session.add(book)
        db.session.commit()

        # 查询数据库
    author_li = Author.query.all()

    data = {'author_li': author_li, 'form': form}
    return render_template('booktest.html', **data)


@app.route('/del', methods=['POST'])
def delbook():
    # get_json前提，前端传递过来的数据必须是Content-Type:application/json
    req_dict = request.get_json()
    bookid = req_dict.get('book_id')
    book = Book.query.get(bookid)
    db.session.delete(book)
    db.session.commit()

    # return redirect(url_for('index'))
    return jsonify(res=0, msg='success')


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    #
    # au_xi = Author(name='我吃西红柿')
    # au_qian = Author(name='萧潜')
    # au_san = Author(name='唐家三少')
    # db.session.add_all([au_qian, au_san, au_xi])
    # db.session.commit()
    #
    # bk_xi = Book(name='吞噬星空',author_id=au_xi.id)
    # bk_xi2 = Book(name='寸芒',author_id=au_xi.id)
    # bk_qian = Book(name='飘渺之旅',author_id=au_qian.id)
    # bk_san = Book(name='冰火魔厨',author_id=au_san.id)
    # db.session.add_all([bk_qian,bk_san,bk_xi,bk_xi2])
    # db.session.commit()

    manager.run()
