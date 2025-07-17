from QATests.utilities.formPageLocators import FormPageLocatorFields

from QATests.pages.base_page import BasePage

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
