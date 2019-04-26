# -*- coding: utf-8 -*-

""" 测试工具自动生成的case """

import unittest
from src.lib import Wraps


class TestDoubanApi(unittest.TestCase):
    """这是TestDoubanApi接口测试用例"""

    def setUp(self):
        """ test setup function """

    def tearDown(self):
        """ test case tearDown function """

    @Wraps.test_case_runner
    @Wraps.test_case_parse
    def test_douban_userinfo(self, *args, **kwargs):
        """测试豆瓣获取用户api的数据"""
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        exec(kwargs.get('exec_text'))
