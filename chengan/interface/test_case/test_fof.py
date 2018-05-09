import requests
import json
import unittest
import login


class MyTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass


class test_fof(MyTest):

    def test_listfof(self):
        """获取母基金列表"""
        data = {
               "page_num": 1,
               "page_size": 999
               }

        session = login.login()
        r = session.post(url = 'http://test.chengantech.cn:8888/web/v1/api/listfof', json = data)
        result = r.json()
        print(result)

        self.assertEqual(result['errcode'],0)
        self.assertEqual(result['errmsg'],'ok')


    def test_createfof(self):
        """创建一支母基金"""
        data = {
               "fof_name": "某某母基金",
               "status": "待募集",
               "allotted_time": "1~3年",
               "dt_found": "2017-12-21T16:00:00.000Z",
               "target": {
                         "num": 12000000,
                         "unit_id": 1
                         },
               "manager_id": 12,
               "fof_num": "基金编号/字符串"
               }
        url = 'http://test.chengantech.cn:8888/web/v1/api/createfof'

        session = login.login()
        r = session.post(url, json = data)
        result = r.json()
        print(result)

        self.assertEqual(result['errcode'], 0)
        self.assertEqual(result['errmsg'], 'ok')

    def test_deletefof(self):
        """删除一支母基金"""
        data = {
               "fof_id": 1
               }

        url = 'http://test.chengantech.cn:8888/web/v1/api/deletefof'
        session = login.login()
        r = session.post(url, json = data)
        result = r.json()
        print(result)

        self.assertEqual(result['errcode'],0)
        self.assertEqual(result['errmsg'],'ok')

    def test_changefof(self):
        """更新一支母基金"""
        data = {
               "fof_id": 1 ,
               "fof_name": "某某母基金",
               "status": "待募集",
               "allotted_time": "1~3年",
               "dt_found": "2017-12-21T16:00:00.000Z",
               "target": {
                         "num": 12000000,
                         "unit_id": 1
                         },
               "manager_id": 12,
               "fof_num": "基金编号/字符串",
               "income_division": "收入分配",
               "fund_desc": "描述信息(备注)",
               "fund_address": "北京是朝阳区",
               "invest_strategy": "投资策略",
               "related_expense": "相关费用",
               "fund_type": "基金类型",
               "fund_invest_size": "单项投资规模"
               }

        url = 'http://test.chengantech.cn:8888/web/v1/api/changefof'
        session = login.login()
        r = session.post(url , json = data)
        result = r.json()
        print(result)
        self.assertEqual(result['errcode'],0)
        self.assertEqual(result['errmsg'],'ok')
