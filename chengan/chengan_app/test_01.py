from appium import webdriver
desired_caps = {
                'platformName': 'Android',
                'deviceName': 'df7eda47',
                'platformVersion': '8.1.0',
                'appPackage': 'app-release',
                'LoadingActivity': 'com.chengan.even.ui.common.activity.LoadingActivity'
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)