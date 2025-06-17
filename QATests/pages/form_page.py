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

    def click_hello_button(self):
        self.click(self.locate.hello_there_button)
        #This opens a new page with "Success!" and some text; need assert

    def click_image_button(self):
        self.click(self.locate.click_me_button)
        #This opens same page as "Hello there" button, with "Success!" and some text; need assert
    
    def select_checkbox1(self):
        self.click(self.locate.checkbox1)
        

    #optional generic method for data-driven use cases
    def set_input_field_by_name(self, field_attr_name, value):
        """Dynamically set input fields by passing the locator attribute name as string."""
        if not hasattr(self.locate, field_attr_name):
            raise AttributeError(f"No locator named '{field_attr_name}' in FormPageLocators")
        locator = getattr(self.locate, field_attr_name)
        self.set(locator, value)
