import requests
import json
import unittest
from BeautifulReport import BeautifulReport

class MyTest(unittest.TestCase):
    def setUp(self):
        print('start test')
        pass
    def tearDown(self):
        print('test end')
        pass

class login_test(MyTest):

    @BeautifulReport.add_test_img('test_success_case_img')
    def test_login1_normal(self):
        """test first: username password is normal"""
        self.url = 'http://test.chengantech.cn:8888/center/web/v1/api/login'
        print("test_login1_normal is start run ...")
        self.data = {
                    "account_type":"company",
                    "username":"caozhihong1",
                    "password":"12345678"
                    }

        r = requests.post(url = self.url, json = self.data)
        result = r.json()
        print(result)
        self.assertEqual(result['errcode'],0)
        self.assertEqual(result['errmsg'], 'ok')
        print('test_login1_normal is end ...')

    def test_login2_PasswdError(self):
        """test second: username ok password error"""
        self.url = 'http://test.chengantech.cn:8888/center/web/v1/api/login'
        print('test_login2_PasswdError is start run ...')
        self.data = {
                    "account_type":"company",
                    "username":"caozhihong1",
                    "password":""
                    }
        r = requests.post(url = self.url, json = self.data)
        result = r.json()
        print(result)
        self.assertEqual(result['errcode'],1)
        self.assertEqual(result['errmsg'],'密码输入错误,请重新输入')
        print('test_login2_PasswdError is end ...')
    
    def test_login3_UsernameError(self):
        """ test third: password ok username error"""
        self.url = 'http://test.chengantech.cn:8888/center/web/v1/api/login'
        print('test_login3_UsernameError is start run ...')
        self.data = {
                    "account_type":"company",
                    "username":"caozh",
                    "password":"12345678"
                    }
        r = requests.post(url = self.url, json = self.data)
        result = r.json()
        print(result)
        self.assertEqual(result['errcode'],2)
        self.assertEqual(result['errmsg'],'此用户不存在')
        print('test_login3_UsernameError is end ...')