from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,threading
import time,os
driver = webdriver.Chrome()

# time.sleep(2)
driver.get("https://edc.medbanks.cn/admin/login")
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

driver.find_element_by_xpath('/html/body/div/div/section[3]/div/table/tbody/tr[1]/td[1]/div/a').click()
time.sleep(3)
#选择访视式设置
driver.find_element_by_xpath("/html/body/div/div/aside/section/ul/li[3]/a/span").click()
time.sleep(3)
js=('window.scrollTo(10000,10000)')
driver.execute_script(js)
#编辑
driver.find_element_by_xpath(".//*[@id='formID']/section/div[2]/a").click()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[1]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[1]/td[2]/input").send_keys("51")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[2]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[2]/td[2]/input").send_keys("2")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[3]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[3]/td[2]/input").send_keys("3")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[4]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[4]/td[2]/input").send_keys("4")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[5]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[5]/td[2]/input").send_keys("5")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[6]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[6]/td[2]/input").send_keys("6")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[7]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[7]/td[2]/input").send_keys("7")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[8]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[8]/td[2]/input").send_keys("8")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[9]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[9]/td[2]/input").send_keys("9")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[10]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[10]/td[2]/input").send_keys("10")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[11]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[11]/td[2]/input").send_keys("11")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[12]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[12]/td[2]/input").send_keys("12")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[13]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[13]/td[2]/input").send_keys("13")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[14]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[14]/td[2]/input").send_keys("14")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[15]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[15]/td[2]/input").send_keys("15")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[16]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[16]/td[2]/input").send_keys("16")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[17]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[17]/td[2]/input").send_keys("17")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[18]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[18]/td[2]/input").send_keys("18")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[19]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[19]/td[2]/input").send_keys("19")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[20]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[20]/td[2]/input").send_keys("20")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[21]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[21]/td[2]/input").send_keys("21")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[22]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[22]/td[2]/input").send_keys("22")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[23]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[23]/td[2]/input").send_keys("23")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[24]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[24]/td[2]/input").send_keys("24")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[25]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[25]/td[2]/input").send_keys("25")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[26]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[26]/td[2]/input").send_keys("26")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[27]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[27]/td[2]/input").send_keys("27")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[28]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[28]/td[2]/input").send_keys("28")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[29]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[29]/td[2]/input").send_keys("29")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[30]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[30]/td[2]/input").send_keys("30")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[31]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[31]/td[2]/input").send_keys("31")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[32]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[32]/td[2]/input").send_keys("32")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[33]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[33]/td[2]/input").send_keys("33")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[34]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[34]/td[2]/input").send_keys("34")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[35]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[35]/td[2]/input").send_keys("35")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[36]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[36]/td[2]/input").send_keys("36")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[37]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[37]/td[2]/input").send_keys("37")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[38]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[38]/td[2]/input").send_keys("38")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[39]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[39]/td[2]/input").send_keys("39")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[40]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[40]/td[2]/input").send_keys("40")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[41]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[41]/td[2]/input").send_keys("41")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[42]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[42]/td[2]/input").send_keys("42")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[43]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[43]/td[2]/input").send_keys("43")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[44]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[44]/td[2]/input").send_keys("44")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[45]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[45]/td[2]/input").send_keys("45")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[46]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[46]/td[2]/input").send_keys("46")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[47]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[47]/td[2]/input").send_keys("47")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[48]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[48]/td[2]/input").send_keys("48")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[49]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[49]/td[2]/input").send_keys("49")
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[50]/td[2]/input").clear()
driver.find_element_by_xpath(".//*[@id='formID']/section/div[1]/table/tbody/tr[50]/td[2]/input").send_keys("50")