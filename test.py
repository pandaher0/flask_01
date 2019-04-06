# Author:hxj
import unittest

from login import app
import json


class LoginTest(unittest.TestCase):
    """构造单元测试案例"""

    def setUp(self):
        """进行测试之前先执行"""
        #设置flask在测试模式
        # app.config['TESTING'] = True
        app.testing = True
        self.client = app.test_client()

    def test_empty_user_name_password(self):
        """测试用户名、密码不完整"""
        # 都不传
        ret = self.client.post('/login', data={})
        # ret 是视图函数的响应对象 data是响应体数据
        resp = ret.data
        # 返回的是json字符串
        resp = json.loads(resp)

        # 进行断言测试
        self.assertIn('res', resp)
        self.assertEqual(resp['res'], 1)
        # 只传用户名
        ret = self.client.post('/login', data={'username': 'admin'})
        resp = ret.data
        resp = json.loads(resp)
        self.assertIn('res', resp)
        self.assertEqual(resp['res'], 1)
        # 只传密码
        ret = self.client.post('/login', data={'password': 'python'})
        resp = ret.data
        resp = json.loads(resp)
        self.assertIn('res', resp)
        self.assertEqual(resp['res'], 1)

    def test_wrong_user_name_password(self):
        # 用户名密码都错误
        ret = self.client.post('/login', data={'username': 'adadad', 'password': 'adfasdfa'})
        resp = ret.data
        resp = json.loads(resp)
        self.assertIn('res', resp)
        self.assertEqual(resp['res'], 2)
        # 用户名错误
        ret = self.client.post('/login', data={'username': 'adadad', 'password': 'pytohn'})
        resp = ret.data
        resp = json.loads(resp)
        self.assertIn('res', resp)
        self.assertEqual(resp['res'], 2)
        # 密码错误
        ret = self.client.post('/login', data={'username': 'admin', 'password': 'adfasdfa'})
        resp = ret.data
        resp = json.loads(resp)
        self.assertIn('res', resp)
        self.assertEqual(resp['res'], 2)


if __name__ == '__main__':
    unittest.main()
