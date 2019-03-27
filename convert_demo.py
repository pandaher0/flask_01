# coding:utf-8
# Author:hxj
from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 转换器语法
# @app.route('/goods/<int:goods_id>')  # int类型
@app.route('/goods/<goods_id>')  # 不限制类型，默认string（除了/的字符）
def goods_detail(goods_id):
    return 'goods detail page %s' % goods_id


# 定义自定义转换器
class RegexConvert(BaseConverter):
    """"""

    def __init__(self, url_map, regex):
        # 调用父类初始化方法
        super(RegexConvert, self).__init__(url_map)
        # 将正则表达式参数保存到对象中，flask使用这个属性进行路由正则匹配
        self.regex = regex

    def to_python(self, value):
        print ('to_python被调用')
        # value是路径进行正则匹配时提取的参数
        return value

    def to_url(self, value):
        print ('使用url_for方法时被调用')
        super(RegexConvert,self).to_url(value)

# 添加自定义转换器到flask中
app.url_map.converters['re'] = RegexConvert


@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")  # 不限制类型，默认string（除了/的字符）
def send_sms(mobile):
    return 'sned sms to %s' % mobile

@app.route('/index')
def index():
    url = url_for('send_sms',mobile='13312345678')
    return redirect(url)


if __name__ == '__main__':
    print (app.url_map)
    app.run(debug=True)
