# Author:hxj

# # 邮箱设置
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.163.com'
# EMAIL_PORT = 25
# # 发送邮件的邮箱
# EMAIL_HOST_USER = 'houxj_100@163.com'
# # 在邮箱中设置的客户端授权密码
# EMAIL_HOST_PASSWORD = 'maeda710hxj'
# # 收件人看到的发件人
# EMAIL_FROM = 'python<houxj_100@163.com>'

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.163.com',
    MAIL_PROT=25,
    # MAIL_USE_TLS=True,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='houxj_100@163.com',
    MAIL_PASSWORD='maeda710hxj',
)

mail = Mail(app)


@app.route('/')
def index():
    msg = Message(u'今天吃什么', sender='python<houxj_100@163.com>', recipients=['912331011@qq.com'])
    msg.body = u"今天吃什么"
    mail.send(msg)
    print('send mail')
    return 'sucess'


if __name__ == '__main__':
    app.run()
