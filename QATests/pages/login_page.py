from QATests.pages.base_page import BasePage
from QATests.pages.my_account_page import MyAccountPage
from QATests.utilities.locators import LoginPageLocatorFields

class LoginPage(BasePage):

    def __init__(self, driver):
        self.locate = LoginPageLocatorFields
        super().__init__(driver)

    def click_login_button(self):
        login_btn = self.wait_for_element(LoginPageLocatorFields.login_button)
        login_btn.click()

    def set_email_address(self, email_address):
        self.set(self.locate.email_address_field, email_address)

    def set_password(self, password):
        self.set(self.locate.password_field, password)

    def click_login_button(self):
        self.click(self.locate.login_button)
        return MyAccountPage(self.driver)

    def log_into_application(self, email, password):
        self.set_email_address(email)
        self.set_password(password)
        return self.click_login_button()

    def get_warning_message(self):
        return self.get_text(self.locate.warning_message)
    
    def get_new_customer_message(self):
        div_element=self.find(*self.locate.new_customer_message)
        div_text = div_element.text
        elements=div_text.split("\n")
        return elements
    
    def get_website_main_message(self):
        return self.get_text(self.locate.website_main_message)