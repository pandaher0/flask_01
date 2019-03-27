# coding:utf-8
# Author:hxj

from flask import Flask, request

app = Flask(__name__)

# post\get都可以在url中添加查询字符串
@app.route('/', methods=['GET', 'POST'])
def index():
    # request包含前端全部数据
    # request.form 包含全部表单格式数据，类字典的对象
    name = request.form.get('name')
    name_li = request.form.getlist('name')
    age = request.form.get('age')
    print (request.data)

    city = request.args.get('city')
    # get 方法只可以获得多个重名参数中的第一个
    # getlist可以获取多个

    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass




    return 'name=%s,age=%s,city=%s,name_li=%s' % (name, age,city,name_li)


if __name__ == '__main__':
    app.run(debug=True)
