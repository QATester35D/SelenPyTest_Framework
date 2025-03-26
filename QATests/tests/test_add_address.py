from QATests.pages.add_address_page import AddAddressPage
from QATests.tests.base_test import BaseTest
from QATests.utilities.test_data import TestData
from QATests.pages.login_page import LoginPage

class TestAddAddress(BaseTest):

    def test_add_address(self):
        login_page=LoginPage(self.driver)
        add_address_page=AddAddressPage(self.driver)
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        my_account_page=login_page.click_login_button()
        my_account_page.click_right_menu_page("Address Book")
        add_address_page.set_first_name(TestData.address1_firstname)
        add_address_page.set_last_name(TestData.address1_lastname)
        add_address_page.set_company(TestData.address1_company)
        add_address_page.set_address1(TestData.address1_address1)
        add_address_page.set_address2(TestData.address1_address2)
        # actual_message=change_password_page.get_confirmation_error_message()
        # assert actual_message == expected_message