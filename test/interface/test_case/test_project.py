import requests
import unittest
import json
from login import Blog
class MyTest(unittest.TestCase):

    def setUp(self):
        print('start test')
        s = requests.session()
        self.blog = Blog(s)
    def tearDown(self):
        print('end test')
        pass

class switch_account_test(MyTest):
    def test_login(self):
        result=self.blog.login()


if __name__ == '__main__':
    unittest.main()
