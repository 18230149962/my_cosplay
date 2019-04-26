import time
def login(driver, username):#此处的driver是个形参,如果不在此处定义就不可以使用
    # 输入用户名
    driver.find_element_by_name('userName').send_keys(username)
    time.sleep(2)
    # 输入密码(用的时候加在参数化的那加上参数)
    # driver.find_element_by_name('password').send_keys(password)
    # time.sleep(2)
    driver.find_element_by_xpath("//*[contains(text(),'登录')]").click()

def exit(driver):
    time.sleep(2)
    driver.find_element_by_class_name('exit user-btn').click()
