from QATests.pages.form_page import FormPage
from QATests.utilities.formPageLocators import FormPageLocatorFields
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from QATests.pages.base_page import BasePage

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

class CheckboxValidation(BasePage):
    def __init__(self, driver):
        self.locate = FormPageLocatorFields
        super().__init__(driver)

    def validate_initial_checky_checkboxes_state(self):
        checky_checkboxes = {
            "checky": {
                "locator": self.locate.checkbox1,
                "expected_selected": False,
                "expected_display": True,
                "expected_enabled": True,
                "expected_value": "furrfu"
            },
            "checkedchecky": {
                "locator": self.locate.checkbox2,
                "expected_selected": True,
                "expected_display": True,
                "expected_enabled": True
            },
            "disabledchecky": {
                "locator": self.locate.checkbox3,
                "expected_selected": False,
                "expected_display": True,
                "expected_enabled": False
            },
            "randomly_disabled_checky": {
                "locator": self.locate.checkbox4,
                "expected_selected": True,
                "expected_display": True,
                "expected_enabled": False
            }
        }

        for name, check in checky_checkboxes.items():
            checkbox = self.find(*check["locator"])
            match name:
                case "checky":
                    assert checkbox.is_selected() == check["expected_selected"], (f"{name} checkbox selected state mismatch. Expected: {check['expected_selected']}, but got: {checkbox.is_selected()}")
                    assert checkbox.is_displayed() == check["expected_display"], (f"{name} checkbox displayed state mismatch. Expected: {check['expected_display']}, but got: {checkbox.is_displayed()}")
                    assert checkbox.is_enabled() == check["expected_enabled"], (f"{name} checkbox enabled state mismatch. Expected: {check['expected_enabled']}, but got: {checkbox.is_enabled()}")
                    assert checkbox.get_attribute("value") == check["expected_value"], f"Expected the checkbox value to be: {check["expected_value"]}, but got {checkbox.get_attribute("value")}"
                case "checkedchecky" | "disabledchecky" | "randomly_disabled_checky":
                    assert checkbox.is_selected() == check["expected_selected"], (f"{name} checkbox selected state mismatch. Expected: {check['expected_selected']}, but got: {checkbox.is_selected()}")
                    assert checkbox.is_displayed() == check["expected_display"], (f"{name} checkbox displayed state mismatch. Expected: {check['expected_display']}, but got: {checkbox.is_displayed()}")
                    assert checkbox.is_enabled() == check["expected_enabled"], (f"{name} checkbox enabled state mismatch. Expected: {check['expected_enabled']}, but got: {checkbox.is_enabled()}")
                case _:
                    print ("Invalid checky checkbox name. The name passed was ",name)

class ButtonValidation(BasePage):
    def __init__(self, driver):
        self.locate = FormPageLocatorFields
        super().__init__(driver)

    def validate_submit_button_label(self, form_page, assert_helper):
        label = form_page.get_hello_there_button_label()
        assert_helper.equal(
            actual=label,
            expected="Hello there",
            requirement_id="REQ-101",
            description="Submit button should be labeled 'Hello there'"
        )

    def validate_submit_button_alt_text_label(self, form_page, assert_helper):
        label = form_page.get_image_button_alt_text()
        assert_helper.equal(
            actual=label,
            expected="click me!",
            requirement_id="REQ-102",
            description="Image Button alt label should be 'click me!'"
        )
