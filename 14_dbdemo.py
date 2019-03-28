# coding:utf-8
# Author:hxj


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@39.106.44.166:3306/test3'
    # 自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 显示原始sql语句
    SQLALCHEMY_ECHO = True


app.config.from_object(Config)

# 创建数据库对象
db = SQLAlchemy(app)


class Role(db.Model):  # type:SQLAlchemy
    """角色表"""
    __tablename__ = 'tbl_roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    users = db.relationship("User", backref='role')

    def __repr__(self):
        """定义后，对象显示更直观"""
        return self.name


class User(db.Model):
    """用户表"""
    __tablename__ = 'tbl_users'

    id = db.Column(db.Integer, primary_key=True)  # 整型主键，默认自增
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'))

    def __repr__(self):
        """定义后，对象显示更直观"""
        return self.name


if __name__ == '__main__':
    # 清除当前数据库里所有数据
    db.drop_all()
    # 创建所有的表
    db.create_all()

    # 创建对象
    role1 = Role(name='admin')
    role2 = Role(name='stuff')
    db.session.add_all([role1, role2])
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=role1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=role2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=role2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=role1.id)

    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()
