from QATests.pages.base_page import BasePage
from QATests.utilities.formPageLocators import FormPageLocatorFields

class FormPage(BasePage):
    def __init__(self, driver):
        self.locate = FormPageLocatorFields
        super().__init__(driver)

    