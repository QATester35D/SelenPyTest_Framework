from QATests.pages.add_address_page import AddAddressPage
from QATests.tests.base_test import BaseTest
from QATests.utilities.test_data import TestData
from QATests.pages.login_page import LoginPage
import time

class TestAddAddress(BaseTest):

    def test_add_address(self):
        login_page=LoginPage(self.driver)
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        my_account_page=login_page.click_login_button()
        my_account_page.click_right_menu_page("Address Book")
        add_address_page=AddAddressPage(self.driver)
        actual_title=add_address_page.get_page_title()
        assert actual_title == "Address Book Entries"
        add_address_page.click_new_address_button()
        actual_title=add_address_page.get_page_title()
        assert actual_title == "Add Address"
        add_address_page.set_first_name(TestData.address1_firstname)
        add_address_page.set_last_name(TestData.address1_lastname)
        add_address_page.set_company(TestData.address1_company)
        add_address_page.set_address1(TestData.address1_address1)
        add_address_page.set_address2(TestData.address1_address2)
        add_address_page.set_city(TestData.address1_city)
        add_address_page.set_postcode(TestData.address1_postcode)
        time.sleep(1)
        add_address_page.select_country(TestData.address1_country)
        time.sleep(1)
        add_address_page.select_region_state(TestData.address1_state)
        add_address_page.select_default_address(TestData.address1_default_address)
        add_address_page.click_continue_button()
        address_success_msg = add_address_page.get_success_message()
        assert address_success_msg == "Your address has been successfully added"
        # actual_message=change_password_page.get_confirmation_error_message()
        # assert actual_message == expected_message