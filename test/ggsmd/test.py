from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()

driver.get("http://localhost/index.jsp?projectid=edc_model_030")
time.sleep(3)
driver.maximize_window()  #将浏览器最大化显示
driver.find_element_by_name('userName').send_keys('13800000000')
driver.find_element_by_name('password').send_keys('Qwe123456')
driver.find_element_by_xpath("//*[contains(text(),'登录')]").click()
driver.find_element_by_link_text('受试者').click()
driver.implicitly_wait(3)
driver.find_element_by_id('menu_2').click()
driver.implicitly_wait(3)
driver.switch_to_frame('frm_content')
driver.switch_to_frame('iframe_subject')
driver.find_element_by_xpath('/html/body/div[8]/div[1]/div[1]/button[1]').click()

driver.quit()