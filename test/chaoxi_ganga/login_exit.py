import time
def login(driver, username, password):#此处的driver是个形参,如果不在此处定义就不可以使用
    driver.find_element_by_link_text("登录").click()
    # 切换机构ban
    driver.find_element_by_class_name('hinttext').click()
    # 输入用户名
    driver.find_elements_by_tag_name('input')[0].send_keys(username)
    time.sleep(2)
    # 输入密码
    driver.find_elements_by_tag_name('input')[1].send_keys(password)
    time.sleep(2)
    driver.find_element_by_id('bttn-login').click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[contains(text(),'登录 机构版')]").click()

def exit(driver):
    time.sleep(2)
    driver.find_element_by_class_name('user-card').click()
    driver.implicitly_wait(20)
    driver.find_element_by_link_text('退出').click()
    time.sleep(2)