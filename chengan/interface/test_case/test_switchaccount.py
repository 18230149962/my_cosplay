import requests
import unittest
import json

class MyTest(unittest.TestCase):
    
    def setUp(self):
        print('start test')
        pass
    def tearDown(self):
        print('end test')
        pass

class switch_account_test(MyTest):
    def test_switch(self):
        """切换账号"""
        self.url = 'http://test.chengantech.cn:8888/center/web/v1/api/switchaccount'
        self.body = {
                    "account_id":1,
                    "account_type":"company"
                    }

        r = requests.post(url = self.url, json = self.body)
        result = r.json()
        print(result)
        self.assertEqual(result['errcode'], 0)
        self.assertEqual(result['errmsg'], 'ok')