from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from PIL import Image
import unittest, time, re
import pytesseract
def jianhuashizhazha():
    driver = webdriver.Chrome()
    driver.get("http://test.chengantech.cn:8888/company/login")
    time.sleep(2)
    driver.maximize_window()  #将浏览器最大化显示
    driver.find_elements_by_tag_name('input')[0].send_keys('zhangpengfei1')
    driver.find_elements_by_tag_name('input')[1].send_keys('1234567890')
    time.sleep(3)
    driver.find_element_by_id('bttn-login').click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath('//*[@id="home"]/div/div[2]/div[3]/div/div[3]/span').click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/div/div[3]/div[6]/div[1]/div/ul/li[1]/div/div[1]/div/b').click()
    time.sleep(1)
    driver.quit()

