from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
driver = webdriver.Chrome()

driver.get("http://test.edc.medbanks.cn/admin/login")
time.sleep(2)
driver.maximize_window()  #将浏览器最大化显示
time.sleep(2)

driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("13700000000")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("Medbanks")
time.sleep(3)
driver.find_element_by_class_name('item-button').click()
time.sleep(3)
#查看更多
driver.find_element_by_xpath('html/body/div[1]/div/section[2]/div/a').click()
time.sleep(3)
#选择项目编辑
driver.find_element_by_xpath('')
#选择项目用户管理
driver.find_element_by_xpath('/html/body/div[1]/div/aside/section/ul/li[12]/a/span')
#数量
driver.find_element_by_xpath(".//*[@id='formID']/div/input").send_keys('100')
#提交
driver.find_element_by_xpath(".//*[@id='adduser']").click()
time.sleep(5)

