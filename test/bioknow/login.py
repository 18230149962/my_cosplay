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
driver.maximize_window()
# 项目的url
driver.get("http://localhost/index.jsp?projectid=edc_kls_ystbnfp_01")
time.sleep(2)
# 登录页操作
driver.find_element_by_name('userName').send_keys('supersa')
driver.find_element_by_xpath("//*[contains(text(),'登录')]").click()
# 找到要的项目设计模块
driver.find_element_by_link_text('项目设计').click()
# 找到新自动取值
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="menu_20"]').click()
# 找到新增自动取值按钮并点击
driver.switch_to_frame('frm_content')
driver.find_element_by_tag_name('button').click()
driver.switch_to_default_content()
# 在新增页的操作
driver.switch_to_frame('maskdiv_frame_first')
# 字段生效
# Select(driver.find_element_by_name("isvalid")).select_by_value("1")
# 字段子表
Select(driver.find_element_by_name("fid_tableid")).select_by_value("dm")
# 字段子表查询条件
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="casebooktbody"]/tr[7]/td[2]/button').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="searchdiv_content"]/div[1]/input[1]').click()
# 选择要选择的
# 字段子表变量
# Select(driver.find_element_by_name("fid_table_para")).select_by_value("dm")
# 字段父表
# Select(driver.find_element_by_name("tid_tableid")).select_by_value("dm")
# 字段父表变量
# Select(driver.find_element_by_name("tid_table_para")).select_by_value("dm")
# 字段生效查询条件


# 字段关系
# Select(driver.find_element_by_name("relation")).select_by_value("3")
# driver.implicitly_wait(3)
# 点击保存按钮
# driver.find_element_by_xpath('//*[@id="bio-table_body-wrapper"]/form/div/input[1]').click()
driver.switch_to_default_content()

time.sleep(3)
driver.quit()