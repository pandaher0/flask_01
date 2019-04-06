# coding:utf-8


from flask import Flask
from orders import app_orders
from cart import app_cart


app = Flask(__name__)


# app.route('/....')(函数名)

# 注册蓝图
# app.register_blueprint(app_orders)
app.register_blueprint(app_orders,url_prefix='/orders')
app.register_blueprint(app_cart,url_prefix='/cart')



@app.route('/')
def index():
    print('send mail')
    return 'sucess'


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
