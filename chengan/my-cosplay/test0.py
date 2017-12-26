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
driver.get("http://chengantech.com/")
time.sleep(2)
driver.maximize_window()  #将浏览器最大化显示
time.sleep(2)
driver.find_element_by_link_text('登录').click()
time.sleep(2)
driver.find_element_by_class_name('hinttext').click()
driver.implicitly_wait(20)
driver.find_elements_by_tag_name('input')[0].send_keys('张鹏飞')
driver.find_elements_by_tag_name('input')[1].send_keys('1234567890')
time.sleep(3)
driver.find_element_by_id('bttn-login').click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(),'登录 机构版')]").click()
time.sleep(2)
driver.find_element_by_link_text('项目管理').click()
time.sleep(2)
driver.find_element_by_link_text('添加项目').click()
driver.implicitly_wait(20)
driver.find_element_by_xpath('//*[@id="home"]/div/div[2]/div[5]/div[1]/div/div[2]/form/div[2]/div/div/div[1]/div/div/div/div[1]/input').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/ul/li[2]/span').click()
time.sleep(15)
driver.quit()