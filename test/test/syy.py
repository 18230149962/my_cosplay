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
driver = webdriver.Chrome()
url = 'https://passport.cnblogs.com/user/signin?ReturnUrl=%2F&AspxAutoDetectCookieSupport=1'
driver.get(url)
time.sleep(2)
driver.maximize_window()  #将浏览器最大化显示
time.sleep(2)
js = '$("#input1").val("Ferry666")'
js_1 = '$("#input2").val("qwe123456.")'
js_2 = '$("#signin").click()'
driver.execute_script(js)
driver.execute_script(js_1)
driver.execute_script(js_2)

time.sleep(5)
# driver.quit()