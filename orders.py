# Author:hxj


from flask import Blueprint


# 创建蓝图对象,蓝图就是一个小模块的抽象
app_orders = Blueprint('app_orders',__name__)

@app_orders.route('/get_orders')
def get_orders():
    return 'get orders page'
