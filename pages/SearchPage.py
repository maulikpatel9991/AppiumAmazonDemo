from base.BasePage import BasePage
import utilities.CustomLogger as cl

class SearchPageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _searchboxclick = "Search Amazon.in"  #text
    _searchboxenteritem = "android.widget.EditText"  #class
    _clickitem = "mi mobile" #text

    def clicksearchbox(self):
        self.clickElement(self._searchboxclick,"text")
        cl.allureLogs("click serch box")

    def enterItem(self):
        self.sendText("mi ",self._searchboxenteritem,"class")
        cl.allureLogs("Enter Item Name")

    def clickItemName(self):
        self.clickElement(self._clickitem,"text")
        cl.allureLogs("Click Item Name")


