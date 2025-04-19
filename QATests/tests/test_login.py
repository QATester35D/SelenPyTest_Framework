import pytest
from QATests.pages.login_page import LoginPage
from QATests.tests.base_test import BaseTest
from QATests.utilities.test_data import TestData
from QATests.utilities.locators import LoginPageLocatorFields, AddressLocatorFields
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class TestLogin(BaseTest):

    @pytest.mark.smoke
    def test_standard_login(self):
        login_page=LoginPage(self.driver)
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        login_page.click_login_button() #This is actually a custom method that will sync and click on the login button
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(AddressLocatorFields.main_page_title))
        actual_title=login_page.get_title()
        assert actual_title == "My Account"

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
