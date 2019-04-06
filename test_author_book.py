# Author:hxj
import unittest
from booktest import Author,db,app


class DatabaseTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@39.106.44.166:3306/booktest02'
        db.create_all()

    def test_add_author(self):
        """测试添加作者"""
        author = Author(name='zhang',email='123123@123123.com',mobile='13312345678')
        db.session.add(author)
        db.session.commit()

        import time
        time.sleep(10)

        result = Author.query.filter_by(name='zhang').first()
        self.assertIsNotNone(result)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()