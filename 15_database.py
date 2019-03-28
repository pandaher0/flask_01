# coding:utf-8
# Author:hxj


from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
manager = Manager(app)


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@39.106.44.166:3306/booktest'
    # 自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 显示原始sql语句
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'asdfasdfasdfadfasdfadf'


db = SQLAlchemy(app)

# 1
migrate = Migrate(app, db)
# 2 添加新的命令  'db' 为执行命令时输入的信息
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()
