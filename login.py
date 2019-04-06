from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not all([username, password]):
        return jsonify(res=1, msg='invalid params')

    if username == 'admin' and password == 'python':
        return jsonify(res=0, msg='success')
    else:
        return jsonify(res=2, msg='wrong username or password')


if __name__ == '__main__':
    app.run()
