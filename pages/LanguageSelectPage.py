from base.BasePage import BasePage
import utilities.CustomLogger as cl

class LanguageslectPageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form

    _languageselectButton = '//android.widget.ImageView[@content-desc="Select English"]' #xpath
    _continueButton = "in.amazon.mShop.android.shopping:id/continue_button"  #id


    def clicklanguageselectButton(self):
        self.clickElement(self._languageselectButton,"xpath")
        cl.allureLogs("slect language")

    def clickcontinuButton(self):
        self.clickElement(self._continueButton,"id")
        cl.allureLogs("click continu Button")
