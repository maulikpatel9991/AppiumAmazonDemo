from base.BasePage import BasePage
import utilities.CustomLogger as cl

class LoginPageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _skipsignButton = "in.amazon.mShop.android.shopping:id/skip_sign_in_button" #id



    def clickskipsignButton(self):
        self.clickElement(self._skipsignButton,"id")
        cl.allureLogs("click skip sign button")

