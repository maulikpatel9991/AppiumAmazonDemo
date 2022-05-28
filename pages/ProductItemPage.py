from base.BasePage import BasePage
import utilities.CustomLogger as cl

class ProductItemPageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _ProductButton = "Redmi 9A Sport (Carbon Black, 2GB RAM, 32GB Storage) | 2GHz Octa-core Helio G25 Processor | 5000 mAh Battery" #text



    def clickProductButton(self):
        self.clickElement(self._ProductButton,"text")
        cl.allureLogs("click product button")


