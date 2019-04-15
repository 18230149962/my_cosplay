# -*- coding: utf-8 -*-

""" 测试工具自动生成的case """

import unittest
from src.lib import Wraps


class TestMychengangg(unittest.TestCase):
    """这是TestMychengangg接口测试用例"""

    def setUp(self):
        """ test setup function """

    def tearDown(self):
        """ test case tearDown function """

    @Wraps.test_case_runner
    @Wraps.test_case_parse
    def test_1_ip_api(self, *args, **kwargs):
        """测试httpbin的ip接口返回正常"""
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        exec(kwargs.get('exec_text'))

    @Wraps.test_case_runner
    @Wraps.test_case_parse
    def test_2_headers_api(self, *args, **kwargs):
        """测试httpbin headers 接口返回正常"""
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        exec(kwargs.get('exec_text'))

    @Wraps.test_case_runner
    @Wraps.test_case_parse
    def test_3_post_api(self, *args, **kwargs):
        """测试httpbin/post接口的请求与返回结果正确"""
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        exec(kwargs.get('exec_text'))
