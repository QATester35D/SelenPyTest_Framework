from QATests.utilities.formPageLocators import FormPageLocatorFields
from QATests.pages.base_page import BasePage

class CheckboxValidation(BasePage):
    def __init__(self, driver):
        self.locate = FormPageLocatorFields
        super().__init__(driver)

    def validate_initial_checky_checkboxes_state(self, assert_helper):
        checky_checkboxes = {
            "checky": {
                "locator": self.locate.checkbox1,
                "expected_selected": False,
                "expected_display": True,
                "expected_enabled": True,
                "expected_value": "furrfu" #This is the correct value
                # "expected_value": "furfu" #This is intentional to force a failure
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
            self.assert_checkbox_value(checkbox.is_selected(),check["expected_selected"],f"{name} checkbox, verifying the 'selected' state. Expected: {check['expected_selected']}, Actual is: {checkbox.is_selected()}", assert_helper)
            self.assert_checkbox_value(checkbox.is_displayed(),check["expected_display"],f"{name} checkbox, verifying the 'displayed' state. Expected: {check['expected_display']}, Actual is: {checkbox.is_displayed()}", assert_helper)
            self.assert_checkbox_value(checkbox.is_enabled(),check["expected_enabled"],f"{name} checkbox, verifying the 'enabled' state. Expected: {check['expected_enabled']}, Actual is: {checkbox.is_enabled()}", assert_helper)
            if name == "checky":
                self.assert_checkbox_value(checkbox.get_attribute("value"),check["expected_value"],f"{name} checkbox, verifying the 'value' attribute. Expected: {check["expected_value"]}, Actual is: {checkbox.get_attribute("value")}", assert_helper)

    def assert_checkbox_value(self, actual_title, expected_title, message, assert_helper):
        assert_helper.equal(
            actual=actual_title,
            expected=expected_title,
            requirement_id="REQ-104",
            description=message
        )    