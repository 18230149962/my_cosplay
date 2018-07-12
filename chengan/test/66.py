from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from PIL import Image
import unittest, time, re
import pytesseract
driver = webdriver.Chrome()
driver.get('http://test.chengantech.cn:8888/company/login')
time.sleep(2)
driver.maximize_window()  #将浏览器最大化显示
driver.find_elements_by_tag_name('input')[0].send_keys('zhangpengfei1')
driver.find_elements_by_tag_name('input')[1].send_keys('1234567890')
driver.find_element_by_id('bttn-login').click()
driver.implicitly_wait(30)
driver.find_element_by_link_text('全部项目').click()
driver.implicitly_wait(30)
driver.find_element_by_link_text("成安科技1").click()
driver.implicitly_wait(30)
driver.find_element_by_link_text("投后管理").click()
driver.implicitly_wait(30)
driver.find_element_by_link_text("融资记录").click()
time.sleep(5)
driver.find_element_by_link_text("添加记录").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="financingRecord"]/div/div/form[1]/div[1]/div/div/input').click()
driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[2]/table[1]/tbody/tr[4]/td[6]/div/span').click()
time.sleep(5)
driver.quit()
