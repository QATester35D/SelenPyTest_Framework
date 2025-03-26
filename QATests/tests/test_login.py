from QATests.pages.login_page import LoginPage
from QATests.tests.base_test import BaseTest
from QATests.utilities.test_data import TestData

class TestLogin(BaseTest):

    def test_valid_credentials(self):
        login_page=LoginPage(self.driver)
        mainMessage=login_page.get_website_main_message()
        # track_requirement("WE2025R1-3 - ReqId: 1")
        assert mainMessage == "This is a dummy website for Web Automation Testing"
        elements=login_page.get_new_customer_message()
        typeOfCustomer=elements[0]
        accountAction=elements[1]
        customerMessage=elements[2]
        assert typeOfCustomer == "New Customer"
        assert accountAction == "Register Account"
        assert customerMessage == "By creating an account you will be able to shop faster, be up to date on an order's status, and keep track of the orders you have previously made."
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        login_page.click_login_button()
        actual_title=login_page.get_title()
        assert actual_title == "My Account"

    def test_invalid_credentials(self):
        login_page=LoginPage(self.driver)
        login_page.log_into_application("Invalid Email", "Invalid Password")
        actual_message = login_page.get_warning_message()
        assert actual_message.__contains__("Warning")
