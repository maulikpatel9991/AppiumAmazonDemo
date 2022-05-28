import time
import unittest
import pytest
from base.BasePage import BasePage
from pages.LanguageSelectPage import LanguageslectPageTest
from pages.LoginPage import LoginPageTest
from pages.SearchPage import SearchPageTest
from pages.ProductItemPage import ProductItemPageTest
from pages.PincodePage import PincodePageTest
from pages.AddcartPage import AddtocartPageTest
import utilities.CustomLogger as cl



@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class EndtoEndTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = LanguageslectPageTest(self.driver)
        self.bp = BasePage(self.driver)
        self.lg = LoginPageTest(self.driver)
        self.sr = SearchPageTest(self.driver)
        self.pd = ProductItemPageTest(self.driver)
        self.pn = PincodePageTest(self.driver)
        self.ad = AddtocartPageTest(self.driver)

    @pytest.mark.run(order=2)
    def test_2login(self):
        self.lg.clickskipsignButton()
        time.sleep(5)

    @pytest.mark.run(order=1)
    def test_1selectlanguage(self):
        self.cf.clicklanguageselectButton()
        time.sleep(5)
        self.cf.clickcontinuButton()
        time.sleep(5)

    @pytest.mark.run(order=3)
    def test_3search(self):
        self.sr.clicksearchbox()
        time.sleep(4)
        self.sr.enterItem()
        time.sleep(3)
        self.sr.clickItemName()
        time.sleep(4)

    @pytest.mark.run(order=4)
    def test_4Product(self):
        self.pd.clickProductButton()
        time.sleep(4)

    @pytest.mark.run(order=5)
    def test_5Pincode(self):
        self.pn.clickPincodeButton()
        time.sleep(2)
        self.pn.clickapplyButton()
        time.sleep(10)
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Add to Cart").instance(0));')


    @pytest.mark.run(order=6)
    def test_6AddToCart(self):
        self.ad.clickaddtocartButton()
        self.ad.clickcartButton()
        time.sleep(20)
        self.ad.clickprocessbuyButton()






