from base.BasePage import BasePage
import utilities.CustomLogger as cl

class AddtocartPageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _addtocartButton="Add to Cart"  #text
    _cartButton="Cart"  #text
    # _proceedbuyButton = "Proceed to Buy (1 item)" #text
    _proceedbuyButton = "Proceed to Buy (1 item)"  #text

    def clickaddtocartButton(self):
        self.clickElement(self._addtocartButton,"text")
        cl.allureLogs("Click addtocard button")

    def clickcartButton(self):
        self.clickElement(self._cartButton,"text")
        cl.allureLogs("click cart Button")

    def clickprocessbuyButton(self):
        self.clickElement(self._proceedbuyButton,"text")
        cl.allureLogs("click proceedBuy Button click")


