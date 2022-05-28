from appium.webdriver.common.touch_action import TouchAction
from base.BasePage import BasePage
import utilities.CustomLogger as cl

class PincodePageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _pincodeButton = "Enter an Indian pincode"  #text
    _applyButton = "Apply"  #text


    def clickPincodeButton(self):
        self.clickElement(self._pincodeButton,"text")
        cl.allureLogs("click pincode button")

    def clickapplyButton(self):
        self.clickElement(self._applyButton,"text")
        cl.allureLogs("click Apply Button")

