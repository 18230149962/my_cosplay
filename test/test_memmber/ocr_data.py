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

driver.get("http://localhost/project.jsp")
time.sleep(2)
driver.maximize_window()  #将浏览器最大化显示
time.sleep(2)
driver.find_element_by_name('userid').send_keys('pm')
driver.save_screenshot('f://ocr//aa.png')
driver.implicitly_wait(30)
driver.switch_to_frame('checkcodeimg')
image = driver.find_element_by_xpath('/html/head/title')
driver.switch_to_default_content()
location = image.location
size = image.size
rangle = (int(location['x']), int(location['y']), int(location['x']+size['width']), int(location['y']+size['height'])) #写成我们需要截取的位置坐标
i = Image.open("f://ocr//aa.png") #打开截图
frame4 = i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
frame4.save('f://ocr//frame4.jpg')
qq = Image.open('f://ocr//frame4.jpg')
text = pytesseract.image_to_string(qq).strip() #使用image_to_string识别验证码
driver.find_element_by_id('checkcode').send_keys(text)
driver.find_element_by_link_text('登录').click()
print('妥了')
driver.quit()