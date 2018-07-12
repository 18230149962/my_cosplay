import requests
import json
import unittest
import login


class MyTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

class test_externalfof(MyTest):
    """外部子基金"""
    def test_listexternalfund(self):
        """获取外部子基金列表"""
        data = {
               "page_num": 1,
               "page_size": 20,
               "fund_status": "待募集",
               "manager": 1,
               "process_status": "已投",
               "keyword" : "xx基金"
               }
        url = 'http://test.chengantech.cn:8888/web/v1/api/listexternalfund'

        session = login.login()
        r = session.post(url, json = data)
        result = r.json()
        self.assertEqual(result['errcode'], 0)
        self.assertEqual(result['errmsg'], 'ok')

    def test_createexternalfund_intended(self):
        """创建一支外部子基金(拟投)"""
        data = {
               "fund_name" : "sub",
               "fund_num": 1,
               "process_status": "拟投",
               "fund_status": "待募集",
               "fund_size" : {
                             "num": "90.00",
                             "unit_id":2
                             },
               "allotted_time": "1~3年",
               "dt_found": "2017-12-21T16:00:00.000Z",
               "fund_address" : "北京",
               "fund_type" : "生活",
               "fund_invest_size" : "11111",
               "invest_strategy": "看天命",
               "income_division": "5-5",
               "cost_desc" : "吃饭",
               "gp_name" : "xx基金",
               "manager": 1
               }

        url = 'http://test.chengantech.cn:8888/web/v1/api/createexternalfund'

        session = login.login()
        r = session.post(url, json = data)
        result = r.json()
        self.assertEqual(result['errcode'], 0)
        self.assertEqual(result['errmsg'], 'ok')
    def test_createexternalfund_invested(self):
        """创建一支外部子基金(已投)"""
        data = {
                "process_status": "已投",
                "manager": 1,
                "fund_num": "",
                "fund_name": "111",
                "allotted_time": "1~3年",
                "dt_found": "2018-01-04T16:00:00.000Z",
                "fund_address": "",
                "fund_size": {"unit_id": 1, "num": 111},
                "gp_name": "",
                "fund_status": "运行中",
                "fof_id":4,
                "dt_invest":"2016-12-04T00:00:00.000000Z",
                "invest_amount": {
                                    "num": "44.000000",
                                    "unit_id":1
                                },
                "invest_ratio":"30.33"
                }
        url = 'http://test.chengantech.cn:8888/web/v1/api/createexternalfund'
        session = login.login()
        r = session.post(url, json = data)
        result = r.json()
        self.assertEqual(result['errcode'], 0)
        self.assertEqual(result['errmsg'], 'ok')

    def test_deleteexternalfund(self):
        """删除一支外部子基金"""
        data = {
                  "fund_id": 1
                }

        url ='http://test.chengantech.cn:8888/web/v1/api/deleteexternalfund'
        session = login.login()
        r = session.post(url, json = data)
        result = r.json()
        self.assertEqual(result['errcode'], 0)
        self.assertEqual(result['errmsg'], 'Delete ok')

    def test_queryexternalfunddetail(self):
        """获取一支子基金的详情"""
        data = {
                "fund_id": 1
                }

        url = 'http://test.chengantech.cn:8888/web/v1/api/queryexternalfunddetail'
        session = login.login()
        r = session.post(url, json = data)
        result = r.json()
        self.assertEqual(result['errcode'], 0)
        self.assertEqual(result['errmsg'], 'ok')

    def test_updateexternalfund(self):
        """更新一支外部子基金"""
        data = {
                "allotted_time": "1~3年",
                "company_id": 1,
                "related_expense": "",
                "dt_found": "2016-12-04T00:00:00.000000Z",
                "fund_address": "bj",
                "fund_invest_size": "10000~50000",
                "fund_name": "外部子基金",
                "fund_num": "2333",
                "target": {
                            "num": "10000000.00000000",
                            "unit_id": 2
                        },
                "status": "运作中",
                "fund_type": "",
                "gp_name": "",
                "fund_id": 1,
                "income_division": "50-50",
                "invest_strategy": "",
                "process_status": "拟投",
                "fund_desc": ""
                }

        url = 'http://test.chengantech.cn:8888/web/v1/api/updateexternalfund'
        session = login.login()
        r = session.post(url, json = data)
        result = r.json()
        self.assertEqual(result['errcode'], 0)
        self.assertEqual(result['errmsg'], 'update  ok')

    def test_changeprocessstatus(self):
        """将外部子基金的进展状态由拟投改成已投"""
        data = {
                "fund_id":1,
                "fof_id":1,
                "dt_invest":"2016-12-04T00:00:00.000000Z",
                "invest_amount": {
                                    "num": "44.000000",
                                    "unit_id":2
                                },
                "invest_ratio":"30.33"
                }

        url = 'http://test.chengantech.cn:8888/web/v1/api/changeprocessstatus'
        session = login.login()
        r = session.post(url, json = data)
        result = r.json()
        self.assertEqual(result['errcode'], 0)
        self.assertEqual(result['errmsg'], '基金成功进入已投')

    def test_createexternalfundinvest(self):
        """添加母基金认缴"""
        data = {
                "fund_id":3,
                "fof_id":1,
                "dt_invest":"2016-12-04T00:00:00.000000Z",
                "invest_amount": {
                                    "num": "44.000000",
                                    "unit_id":2
                                },
                "invest_ratio":"30.33"

            }

        url = 'http://test.chengantech.cn:8888/web/v1/api/createexternalfundinvest'
        session = login.login()
        r = session.post(url, json = data)
        result = r.json()
        self.assertEqual(result['errcode'], 0)
        self.assertEqual(result['errmsg'], '认缴记录添加成功')

    def test_updateexternalfundinvest(self):
        """编辑认缴记录"""
        data = {
                "fund_id":3,
                "fof_id":1,
                "dt_invest":"2016-12-04T00:00:00.000000Z",
                "invest_amount": {
                                    "num": "4455555.000000",
                                    "unit_id":2
                                },
                "invest_ratio":"35.33"

            }
        url = 'http://test.chengantech.cn:8888/web/v1/api/updateexternalfundinvest'
        session = login.login()
        r = session.post(url, json = data)
        result = r.json()
        self.assertEqual(result['errcode'], 0)
        self.assertEqual(result['errmsg'], '认缴记录更新成功')

