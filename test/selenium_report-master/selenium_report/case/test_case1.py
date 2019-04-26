import time
import unittest

from selenium import webdriver

from bioknow.test import login_exit


class Test_Log(unittest.TestCase):
    @classmethod
    def setUp(cls):
        url="http://www.chengantech.com/"
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(url)

    def test_01(self):
    # 调用login函数,并向它传参
        login_exit.login(driver=self.driver, username=u"张鹏飞", password=u"1234567890")
        time.sleep(5)
        login_exit.exit(driver=self.driver)
        time.sleep(3)

    def test_02(self):
        login_exit.login(driver=self.driver, username=u"张鹏飞", password=u"1234567890")
        time.sleep(3)
        my_data = self.driver.find_element_by_link_text('主页').text
        you_data = '主'
        self.assertEqual(my_data, you_data)

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()