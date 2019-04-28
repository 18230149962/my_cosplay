import time
import unittest

from selenium import webdriver

from BK_EDC.public import login_exit


class Test_Log(unittest.TestCase):
    def setUp(self):
        url = "http://localhost/index.jsp?projectid=edc_kls_ystbnfp_01"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)

    def test_01(self):
    # 调用login函数,并向它传参
        login_exit.login(driver=self.driver, username=u"supersa")
        time.sleep(5)
        login_exit.exit(driver=self.driver)
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()