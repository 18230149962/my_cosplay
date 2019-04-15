import json
import datetime
from tests import TestCase


class TestFund(TestCase):

    def login(self):
        data = {
            'username': 'test',
            'password': '123456',
        }
        self.client.post('/web/v1/api/login',
                      data=json.dumps(data),
                      content_type='application/json')

    def test_create_fund(self):
        data = {
                'fund_name': '基金名称 001',
                'status': 'raising',
                'allotted_time': '1-3年',
                'dt_found':'2017-1-1 08:00:00',
                'target':100000,
                }
        resp = self.client.post('/web/v1/web/v1/api/createfund',
                                data=json.dumps(data),
                                content_type='application/json')
        ret = json.loads(resp.data.decode('utf-8'))
        expect = {
            'data': {'fund_id': 3},
            'errcode': 0,
            'errmsg': 'ok'
         }

        self.assertEqual(expect, ret)


    def test_list_fund(self):
        login_data = {
            'username': 'TestUser 测试用户 01',
            'password': '123456',
        }
        self.client.post('/web/v1/web/v1/api/login',data=json.dumps(login_data),content_type='application/json')
        # 测试fund_id
        data = {
                'fund_id':1,
                }
        resp = self.client.post('/web/v1/web/v1/api/listfund',
                                data=json.dumps(data),
                                content_type='application/json')
        ret = json.loads(resp.data.decode('utf-8'))
        for item in ret['data']:
            item.pop('dt_create')
            item.pop('dt_update')
        expect = {'data': [{'dt_found': '2015-01-04 00:00:00', 'target': '1000000.00000000', 'status': 'raising', 'allotted_time': '1-3年', 'manager_name': '张三', 'company_id': 1, 'fund_desc': '老鹰基金是一家关注TMT投资与新媒体投资的股权投资基金', 'fund_name': '老鹰基金001', 'id': 1}], 'errmsg': 'ok', 'errcode': 0}
        self.assertEqual(expect, ret)

        # 测试target
        data = {
                'target':10000000,
                }
        resp = self.client.post('/web/v1/web/v1/api/listfund',
                                data=json.dumps(data),
                                content_type='application/json')
        ret = json.loads(resp.data.decode('utf-8'))
        for item in ret['data']:
            item.pop('dt_create')
            item.pop('dt_update')
        expect = {'data':[{'fund_name': '老鹰基金002', 'allotted_time': '3-5年',
            'fund_desc': '老鹰基金是一家关注TMT投资与新媒体投资的股权投资基金',
            'id': 2, 'manager_name': '李四', 'target': '10000000.00000000',
            'company_id': 1, 'status': 'raising', 'dt_found': '2016-12-04 00:00:00'}],'errcode':0,'errmsg':'ok'}
        self.assertEqual(expect, ret)


        # 组合测试
        data = {
                'target':10000000,
                'status':'raising',
                }
        resp = self.client.post('/web/v1/web/v1/api/listfund',
                                data=json.dumps(data),
                                content_type='application/json')
        ret = json.loads(resp.data.decode('utf-8'))
        for item in ret['data']:
            item.pop('dt_create')
            item.pop('dt_update')
        expect = {'data':[{'fund_name': '老鹰基金002', 'allotted_time': '3-5年',
            'fund_desc': '老鹰基金是一家关注TMT投资与新媒体投资的股权投资基金',
            'id': 2, 'manager_name': '李四', 'target': '10000000.00000000',
            'company_id': 1, 'status': 'raising', 'dt_found': '2016-12-04 00:00:00'}],'errcode':0,'errmsg':'ok'}
        self.assertEqual(expect, ret)

    def test_create_fundlp(self):
        data = {
                'fund_id': 1,
                'lp_id': 1,
                'amount':20000,
                'status':'received',
                }
        resp = self.client.post('/web/v1/web/v1/api/createfundlp',
                                data=json.dumps(data),
                                content_type='application/json')
        ret = json.loads(resp.data.decode('utf-8'))
        expect = {
            'data': {'fundlp_id': 3},
            'errcode': 0,
            'errmsg': 'ok'
         }

        self.assertEqual(expect, ret)


    def test_list_fundraising(self):
        data = {
            'fund_id':1,
            }
        resp = self.client.post('web/v1/api/listfundraising',
                                data = json.dumps(data),
                                content_type='application/json')
        ret = json.loads(resp.data.decode('utf-8'))
        for item in ret['data']:
            item.pop('dt_create')
            item.pop('dt_update')
        expect = {'data':[{'amount': '300000.00000000', 'status': 'received', 'company_id': 1, 'id': 2, 'fund_id': 1, 'lp_id': 2},
            {'amount': '60000.00000000', 'status': 'received', 'company_id': 1, 'id': 1, 'fund_id': 1, 'lp_id': 1}],
            'errmsg':'ok','errcode':0}
        self.assertEqual(expect, ret)


    def test_query_fundraising_progress(self):
        data = {
            'fund_id':1,
            }
        resp = self.client.post('web/v1/api/queryfundraisingprogress',
                                data = json.dumps(data),
                                content_type='application/json')
        ret = json.loads(resp.data.decode('utf-8'))
        expect = {'errmsg':'ok','errcode':0,'data':{'QueryFunderRaisingProgress': '360000.00000000'}}
        self.assertEqual(expect, ret)


    def test_list_fund_project(self):
        data = {
            'fund_id':1,
            }
        resp = self.client.post('web/v1/api/listfundproject',
                                data = json.dumps(data),
                                content_type='application/json')
        ret = json.loads(resp.data.decode('utf-8'))
        for item in ret['data']['ProjectDetail']:
            item.pop('dt_create')
            item.pop('dt_update')
        expect = {'errcode':0,'errmsg':'ok','data':{'ApprovalProjectCount': 2, 'QuitProjectCount': 0, 'InvestedProjectCount': 0, 'TotalProjectCount': 2, 'ProjectDetail': [{'brief_intro': '出行行业的独角兽', 'source': '介绍人介绍', 'project_name': 'TestProject 测试项目 02', 'project_logo': 'http://example.com/logo', 'valuation_method': '创始人估值', 'valuation': '18000000', 'invest_logic': '投资逻辑', 'id': 2, 'introduction': '滴滴出行改变了传统打车方式balabala', 'privacy': 'secret', 'category_id': 2, 'status': 'ready', 'invest_stage': '天使轮', 'project_area': 'Beijing 北京', 'company_id': 1}, {'brief_intro': '出行行业的独角兽', 'source': '介绍人介绍', 'project_name': 'TestProject 测试项目 01', 'project_logo': 'http://example.com/logo', 'valuation_method': '创始人估值', 'valuation': '13000000', 'invest_logic': '投资逻辑', 'id': 1, 'introduction': '滴滴出行改变了传统打车方式balabala', 'privacy': 'public', 'category_id': 3, 'status': 'ready', 'invest_stage': 'B轮', 'project_area': 'Beijing 北京', 'company_id': 1}]}}
        self.assertEqual(expect, ret)


    def test_query_fund_detail(self):
        data = {
            'fund_id':1,
            }
        resp = self.client.post('web/v1/api/queryfunddetail',
                                data = json.dumps(data),
                                content_type='application/json')
        ret = json.loads(resp.data.decode('utf-8'))
        ret['data'].pop('dt_create')
        ret['data'].pop('dt_update')
        expect = {'errmsg':'ok','errcode':0,'data':
        {'status': 'raising', 'id': 1, 'manager_name': '张三', 'dt_found': '2015-01-04 00:00:00', 'company_id': 1, 'target': '1000000.00000000', 'allotted_time': '1-3年', 'fund_name': '老鹰基金001', 'fund_desc': '老鹰基金是一家关注TMT投资与新媒体投资的股权投资基金'}}
        self.assertEqual(expect, ret)

    def test_change_fund(self):
        data = {"fund_id":"1","fund_name":"老鹰基金001","status":"募集中","allotted_time":"1~3年","dt_found":"2015-01-04T00:00:00.000000Z","target":1000000,"target_temp":100,"manager_name":"张三","fund_num":"10000001"}
        self.client.post('web/v1/api/changefund',
                                data = json.dumps(data),
                                content_type='application/json')
        data = {'fund_id':1}
        resp = self.client.post('web/v1/api/queryfunddetail',
                                data = json.dumps(data),
                                content_type='application/json')
        ret = json.loads(resp.data.decode('utf-8'))
        ret['data'].pop('dt_create')
        ret['data'].pop('dt_update')
        expect = {'errmsg': 'ok', 'errcode': 0, 'data': {'target': '1000000.00000000', 'fund_desc': '老鹰基金是一家关注TMT投资与新媒体投资的股权投资基金', 'status': '募集中', 'fund_num': '10000001', 'id': 1, 'dt_found': '2015-01-04T00:00:00.000000Z', 'fund_name': '老鹰基金001', 'manager_name': '张三', 'allotted_time': '1-3年', 'is_deleted': False, 'company_id': 1}}
        self.assertEqual(expect, ret)

    def test_change_fund_lp(self):
        self.login()
        data = {"fund_id":"1","lp_id":2,"amount":3000000,"status":"沟通中","fund_lp_id":2}
        resp = self.client.post('web/v1/api/changefundlp',
                                data = json.dumps(data),
                                content_type='application/json')
        ret = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(0,ret['errcode'])

        data = {'fund_id':1}
        resp = self.client.post('web/v1/api/listfundraising',
                                data = json.dumps(data),
                                content_type='application/json')
        ret = json.loads(resp.data.decode('utf-8'))
        for i in ret['data']:
            i.pop('dt_create')
            i.pop('dt_update')
        print(ret)
        expect = {'errcode': 0, 'data': [{'amount': '3000000.00000000', 'lp_avatar': '/static/pic/avatar.jpg', 'company_id': 1, 'lp_id': 2, 'status': '沟通中', 'lp_name': '刘小英', 'fund_id': 1, 'id': 2}, {'amount': '60000.00000000', 'lp_avatar': '/static/pic/avatar.jpg', 'company_id': 1, 'lp_id': 1, 'status': '已打款', 'lp_name': '雷军', 'fund_id': 1, 'id': 1}], 'errmsg': 'ok'}
        self.assertEqual(expect, ret)

