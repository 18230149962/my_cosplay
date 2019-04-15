from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from PIL import Image
import unittest,time, re
import pytesseract

driver = webdriver.Chrome()
driver.get("http://39.105.47.110:8890/company/setting")
time.sleep(2)
driver.maximize_window()  #将浏览器最大化显示
driver.find_elements_by_tag_name('input')[0].send_keys('chengan')
driver.find_elements_by_tag_name('input')[1].send_keys('1234567890')
time.sleep(3)
driver.find_element_by_id('bttn-login').click()
driver.implicitly_wait(30)
driver.find_element_by_link_text('系统设置').click()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[contains(text(),'自定义配置')]").click()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[contains(text(),'基金项目自定义流程')]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(),'+ 创建新流程')]").click()
driver.implicitly_wait(30)
driver.find_element_by_class_name('el-input__inner').send_keys('流程111')
driver.find_element_by_xpath("//*[contains(text(),'下一步')]").click()
driver.implicitly_wait(30)
driver.find_element_by_class_name('el-input__inner').click()
driver.find_element_by_xpath("//*[contains(text(),'项目流程')]").click()
driver.find_element_by_xpath("//*[contains(text(),'下一步')]").click()
driver.implicitly_wait(30)
# 添加几个节点点几下
driver.find_element_by_class_name('el-input__inner').click()
driver.find_element_by_xpath("//*[contains(text(),'添加步骤')]").click()
# driver.quit()

