from appium import webdriver
import time
desired_caps = {
                  "platformName": "Android",
                  "deviceName": "df7eda47",
                  "platformVersion": "8.1.0",
                  "appPackage": "com.chengantech.even",
                  "appActivity": "com.chengantech.even.ui.common.activity.LoadingActivity"
}
driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(30)
driver.find_element_by_id("com.chengantech.even:id/agency_et_account").send_keys("zhangpengfei1")
driver.find_element_by_id("com.chengantech.even:id/layout_et_confirm_pwd").send_keys("1234567890")
driver.find_element_by_id("com.chengantech.even:id/agency_tv_next").click()
driver.implicitly_wait(30)
driver.find_element_by_id("com.chengantech.even:id/main_rb_homepager").click()