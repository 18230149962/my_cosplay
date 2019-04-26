from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,threading
import time,os
def run13():
    driver = webdriver.Chrome()
    # time.sleep(2)
    js=('window.scrollTo(1000,1000)')
    driver.get("http://test.edc.medbanks.cn/admin/login")
    time.sleep(2)
    driver.maximize_window()  #将浏览器最大化显示
    time.sleep(2)
    driver.find_element_by_name("username").send_keys("13700000000")
    driver.find_element_by_name("password").send_keys("Medbanks")
    time.sleep(3)
    driver.find_element_by_class_name('item-button').click()
    time.sleep(3)
    # EDC用户管理
    driver.find_element_by_xpath("/html/body/div[1]/div/aside/section/ul/li[4]/a").click()
    time.sleep(3)
    #跳转第二页
    driver.find_element_by_link_text('2').click()
    time.sleep(3)
    #选择人(1380000001)
    driver.find_element_by_xpath("/html/body/div[1]/div/section[4]/div/table/tbody/tr[5]/td[10]/a[3]").click()
    time.sleep(3)
    #点击管理库和角色
    driver.find_element_by_id('managestudy').click()
    driver.implicitly_wait('15')
    #进入iframe
    driver.switch_to_frame('layui-layer-iframe1')
    #选择项目
    driver.find_element_by_xpath('/html/body/div[1]/section/section[2]/div[1]/table/tbody/tr[1]/td[6]/span').click()
    #退出iframe
    driver.switch_to_default_content()
    #关闭管理库和角色
    driver.find_element_by_xpath('//*[@id="layui-layer1"]/span/a').click()
    driver.quit()
