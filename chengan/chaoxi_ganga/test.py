from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from PIL import Image
from chaoxi_ganga import login_exit
import unittest, time, re
import pytesseract
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