def xiaolei1():
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    import random
    import time,os,select

    list_str = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    veri_str = random.sample(list_str, 4)
    center = ''.join(veri_str)

    driver = webdriver.Chrome()
    driver.get("http://192.168.1.94:18010/loginfront/#/")
    time.sleep(1)
    driver.maximize_window()  #将浏览器最大化显示
    time.sleep(1)
    driver.find_elements_by_tag_name('input')[0].send_keys('zhiyong.guo@bioknow.net')
    driver.find_elements_by_tag_name('input')[1].send_keys('AAaa1111')
    driver.find_elements_by_tag_name('input')[2].send_keys('1')
    driver.find_element_by_tag_name('button').click()
    time.sleep(1)
    driver.find_elements_by_class_name('pro-number')[7].click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//*[@id="home"]/div[3]/section/div/div[3]/div[2]/div/div/div/ul[1]/li[2]').click()
    driver.find_element_by_xpath('//*[@id="home"]/div[3]/section/div/div[3]/div[2]/div/div/div/ul[2]/ul/li/a').click()
    time.sleep(2)
    driver.find_elements_by_class_name('top-group__button__text')[0].click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="index-page"]/div/div/div[1]/div/section/div[4]/div/div[2]/div/div[1]/div/div/form[1]/div[2]/div/div/div[1]/input').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
    driver.find_element_by_xpath('//*[@id="index-page"]/div/div/div[1]/div/section/div[4]/div/div[2]/div/div[1]/div/div/form[1]/div[3]/div/div/input').send_keys(center)
    driver.find_element_by_xpath('//*[@id="index-page"]/div/div/div[1]/div/section/div[4]/div/div[2]/div/div[1]/div/div/form[1]/div[4]/div/div/label[1]/span[1]/span').click()
    driver.find_element_by_xpath('//*[@id="index-page"]/div/div/div[1]/div/section/div[4]/div/div[2]/div/div[1]/div/div/form[1]/div[6]/div/div/div/input').click()
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
    # driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[2]').click()
    driver.find_element_by_xpath('//*[@id="index-page"]/div/div/div[1]/div/section/div[4]/div/div[2]/div/div[1]/div/div/form[1]/div[7]/div/div/div[1]/input').click()
    # driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[2]').click()
    driver.find_element_by_xpath('//*[@id="index-page"]/div/div/div[1]/div/section/div[4]/div/div[2]/div/div[1]/div/div/div[2]/button[2]/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="mainTable"]/div[3]/table/tbody/tr/td[6]/div/button[1]/span').click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="index-page"]/div/div/div[1]/div/section/div[3]/div/div[4]/div/div[2]/div/div[1]/div/div/div[2]/button/span').click()
    time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    xiaolei1()