from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()

# 通过id定位
driver.find_element_by_xpath('//*[@id="kw"]').send_keys(22)
# 通过name定位
driver.find_element_by_xpath("//*[@name='wd']").send_keys(23)
# 通过class定位
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys(24)
# 通过标签定位
driver.find_element_by_xpath("//input[@id='kw']").send_keys(25)
# 层级定位
driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys(26)
# 索引定位
driver.find_element_by_xpath('//select[@id="nr"]/option[2]').click()
# 逻辑运算
driver.find_element_by_xpath('//*[@id="kw" or @name="wd"]').send_keys(222)
# 模糊匹配（1）文字
driver.find_element_by_xpath("//*[contains(text(),'新闻')]").click()
# 模糊匹配（2）某个属性
driver.find_element_by_xpath("//*[contains(@id,'kw')]").send_keys('27')
# 模糊匹配以什么开头
driver.find_element_by_xpath("//*[starts-with(@id,'kw')]").send_keys('28')
# 模糊匹配以什么结尾(没试出来尴尬)
driver.find_element_by_xpath('//*[ends-with(@id,"kw_wrap")]').click()
# 模糊匹配正则（我曹，还有这种操作？）(没试出来这是最尴尬的。。。。)
driver.find_element_by_xpath("//[matchs(text(),'hao123')]").click()
driver.quit()
