import time
import unittest

from selenium import webdriver

from bioknow.test import login_exit


class Test_Log(unittest.TestCase):
    def setUp(self):
        url="http://www.chengantech.com/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)

    def test_01(self):
    # 调用login函数,并向它传参
        login_exit.login(driver=self.driver, username=u"张鹏飞", password=u"1234567890")
        time.sleep(5)
        login_exit.exit(driver=self.driver)
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()