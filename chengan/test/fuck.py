from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re
import random
from datetime import datetime
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://passport.cnblogs.com/user/signin?ReturnUrl=%2F&AspxAutoDetectCookieSupport=1')

    def test_01(self):
        # 密码正确，登陆成功
        self.driver.find_element_by_id('input1').send_keys('Ferry666')
        self.driver.find_element_by_id('input2').send_keys('qwe123456.')
        self.driver.find_element_by_id('signin').click()
        time.sleep(3)
        you_data = self.driver.find_element_by_id('header_user_left').text
        my_data = '欢迎你，Ferry6666666'
        self.assertEqual(you_data, my_data)

    def test_02(self):
         # 密码错误，登陆失败
         self.driver.find_element_by_id('input1').send_keys('Ferry666')
         self.driver.find_element_by_id('input2').send_keys('qwe123456')
         self.driver.find_element_by_id('signin').click()
         time.sleep(3)
         you_data = self.driver.find_element_by_id('tip_btn').text
         my_data = '用户名或密码错误\n\n联系 contact@cnblogs.com'
         self.assertEqual(you_data, my_data)


    def tearDown(self):
        self.driver.quit()

if __name__ == "main":
    unittest.main()