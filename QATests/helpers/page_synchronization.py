from QATests.pages.form_page import FormPage
from QATests.utilities.formPageLocators import FormPageLocatorFields
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageSynchronization:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_page_title(self, page_title, expected_title, assert_helper):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(page_title)
        )
        actual_title=FormPage(self.driver).get_title()
        self.validate_page_title(actual_title, expected_title, assert_helper)

    def arrival_page_sync(self, assert_helper):
        self.wait_for_page_title(FormPageLocatorFields.arrival_page_title, "We Arrive Here", assert_helper)

    def main_page_sync(self, assert_helper):
        self.wait_for_page_title(FormPageLocatorFields.main_page_title, "We Leave From Here", assert_helper)

    def validate_page_title(self, actual_title, expected_title, assert_helper):
        assert_helper.equal(
            actual=actual_title,
            expected=expected_title,
            requirement_id="REQ-103",
            description=f"Page title should be '{expected_title}'"
        )