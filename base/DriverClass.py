import allure
from appium import  webdriver


class Driver:

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['app'] = ('C:\\Users\\150182\\Downloads\\Amazon.apk')
        # desired_caps['appPackage'] = 'com.code2lead.kwad'
        # desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver

    def allureLogs(text):
        with allure.step(text):
            pass