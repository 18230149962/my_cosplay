import time
def login(driver, username):
    driver.find_element_by_name('userName').send_keys(username)
    driver.find_element_by_xpath("//*[contains(text(),'登录')]").click()

def exit(driver):
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="top_td"]/div[1]/div[2]/span[4]').click()