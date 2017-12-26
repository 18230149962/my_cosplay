from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from PIL import Image
import unittest, time, re
import pytesseract
# # option = webdriver.ChromeOptions()
# # option.add_argument('headless')# 静默模式
# driver = webdriver.Chrome(chrome_options=option)
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
# driver.find_element_by_xpath("//*[contains(text(),'添加事项')]").click()
# time.sleep(2)
# driver.save_screenshot('f://自动截图//2主页//添加事项页.png')
# driver.implicitly_wait(20)
# driver.find_element_by_xpath('//*[@id="home"]/div/div[2]/div[4]/div/main/div[2]/div[2]/div[1]/div[2]/ul/li[1]/input').send_keys('33')
driver.find_element_by_class_name('user-card').click()
driver.implicitly_wait(20)
driver.find_element_by_link_text('退出').click()
print(66)
quit()
