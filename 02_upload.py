# coding:utf-8
# Author:hxj

from flask import Flask, request

app = Flask(__name__)

# post\get都可以在url中添加查询字符串
@app.route('/upload', methods=['POST'])
def upload():
    file_obj = request.files.get('pic')
    if not file_obj:
        return '未上传文件'

    file_obj.save('demo.png')


    return  '上传成功'


if __name__ == '__main__':
    app.run(debug=True)
