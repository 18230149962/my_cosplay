# coding=utf8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time,os,select
driver=webdriver.Chrome()

driver.get("http://test.edc.medbanks.cn/admin/login")
time.sleep(3)
driver.maximize_window()  #将浏览器最大化显示
#用户名输入
driver.find_element_by_name('username').send_keys('13700000000')
#密码输入
driver.find_element_by_name('password').send_keys('Medbanks')
time.sleep(1)
driver.find_element_by_class_name('item-button').click()
time.sleep(3)
#新建项目
driver.find_element_by_xpath("html/body/div[1]/div/aside/section/ul/li[2]/a/span").click()
time.sleep(3)
driver.find_element_by_name('study_name').send_keys('最新的项目')
driver.find_element_by_name('study_short_name').send_keys('最新的you')
driver.find_element_by_name('study_number').send_keys('1001')
driver.find_element_by_name('study_leader_name').send_keys('测试')
driver.find_element_by_name('study_leader_phone').send_keys('18230149962')
driver.find_element_by_name('study_leader_email').send_keys('18230149962@163.com')
driver.find_element_by_name('study_version').send_keys('3.2')
driver.find_element_by_name('study_version_date').send_keys('2017-08-24')
driver.find_element_by_name('study_organization').send_keys('思派测试组')
driver.find_element_by_name('study_experimental').send_keys('测试组')
Select(driver.find_element_by_name("project_org_id")).select_by_value("1")
time.sleep(3)
#中心组数
driver.find_element_by_id('site_group_count').send_keys('1')
#中心组名
driver.find_element_by_xpath('//*[@id="site_group_html"]/tr/td[1]/input').send_keys('中心组1')
#中心组编号
driver.find_element_by_xpath('//*[@id="site_group_html"]/tr/td[2]/input').send_keys('default')
#受试者人数
driver.find_element_by_xpath('//*[@id="site_group_html"]/tr/td[3]/input').send_keys('500')
#方案数
driver.find_element_by_name('group_trial_count').send_keys('2')
#方案名称
driver.find_element_by_xpath('//*[@id="group_trial_html"]/tr/td[1]/input').send_keys('方案1')
#方案编号
driver.find_element_by_xpath('//*[@id="group_trial_html"]/tr/td[2]/input').send_keys('1001')
#计划病例数
driver.find_element_by_xpath('//*[@id="group_trial_html"]/tr/td[3]/input').send_keys('150')
#备注
driver.find_element_by_xpath('//*[@id="group_trial_html"]/tr/td[4]/input').send_keys('没有备注')

driver.find_element_by_xpath('//*[@id="group_trial_html"]/tr[2]/td[1]/input').send_keys('方案2')
driver.find_element_by_xpath('//*[@id="group_trial_html"]/tr[2]/td[2]/input').send_keys('1002')
driver.find_element_by_xpath('//*[@id="group_trial_html"]/tr[2]/td[3]/input').send_keys('200')
driver.find_element_by_xpath('//*[@id="group_trial_html"]/tr[2]/td[4]/input').send_keys('没有备注')

#driver.quit()


