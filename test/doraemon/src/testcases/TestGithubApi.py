# -*- coding: utf-8 -*-

""" 测试工具自动生成的case """

import unittest
from src.lib import Wraps


class TestGithubApi(unittest.TestCase):
    """这是TestGithubApi接口测试用例"""

    def setUp(self):
        """ test setup function """

    def tearDown(self):
        """ test case tearDown function """

    @Wraps.test_case_runner
    @Wraps.test_case_parse
    def test_some_endpoint(self, *args, **kwargs):
        """测试github api可用性"""
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        exec(kwargs.get('exec_text'))
