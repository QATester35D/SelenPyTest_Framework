from QATests.utilities.formPageLocators import FormPageLocatorFields
from QATests.pages.base_page import BasePage

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
