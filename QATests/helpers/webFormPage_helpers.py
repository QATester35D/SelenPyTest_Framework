from QATests.pages.form_page import FormPage
from QATests.utilities.formPageLocators import FormPageLocatorFields
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageSynchronization:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_page_title(self, title_locator, expected_title):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(title_locator)
        )
        actual_title=FormPage(self.driver).get_title()
        assert actual_title == expected_title, f"Expected to get page title: {expected_title}, but got {actual_title}"

    def arrival_page_sync(self):
        self.wait_for_page_title(FormPageLocatorFields.arrival_page_title, "We Arrive Here")

    def main_page_sync(self):
        self.wait_for_page_title(FormPageLocatorFields.main_page_title, "We Leave From Here")

