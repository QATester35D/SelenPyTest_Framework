from QATests.pages.base_page import BasePage
from QATests.utilities.formPageLocators import FormPageLocatorFields

class FormPage(BasePage):
    def __init__(self, driver):
        self.locate = FormPageLocatorFields
        super().__init__(driver)

    def set_email_field(self, value):
        self.set(self.locate.email_field, value)
    
    def set_age_field(self, value):
        self.set(self.locate.age_field, value)

    def click_hello_there_button(self):
        self.click(self.locate.hello_there_button)

    def get_hello_there_button_label(self):
        return self.find(*self.locate.hello_there_button).get_attribute("value")
    
    def get_image_button_alt_text(self):
        return self.find(*self.locate.click_me_button).get_attribute("alt")

    def click_image_button(self):
        self.click(self.locate.click_me_button)
    
    def select_checkbox1(self):
        self.click(self.locate.checkbox1)

    #optional generic method for data-driven use cases
    def set_input_field_by_name(self, field_attr_name, value):
        """Dynamically set input fields by passing the locator attribute name as string."""
        if not hasattr(self.locate, field_attr_name):
            raise AttributeError(f"No locator named '{field_attr_name}' in FormPageLocators")
        locator = getattr(self.locate, field_attr_name)
        self.set(locator, value)

