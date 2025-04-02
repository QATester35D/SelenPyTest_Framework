from QATests.pages.add_address_page import AddAddressPage
from QATests.tests.base_test import BaseTest
from QATests.utilities.test_data import TestData
from QATests.pages.login_page import LoginPage
from QATests.tests.test_login import TestLogin
import time
import os
from selenium.webdriver.common.by import By

class TestAddAddress(BaseTest):

    #This is a test case to add an address into the Address Book
    def test_add_address(self):
        TestLogin.test_standard_login(self)
        add_address_page=AddAddressPage(self.driver)
        add_address_page.click_right_menu_page("Address Book")
        actual_title=add_address_page.get_page_title()
        assert actual_title == "Address Book Entries"
        add_address_page.click_new_address_button()
        actual_title=add_address_page.get_page_title()
        assert actual_title == "Add Address"
        nameCounter=TestAddAddress.read_address_name_counter()
        makingFirstNameUnique=TestData.address1_firstname+nameCounter
        add_address_page.set_first_name(makingFirstNameUnique)
        add_address_page.set_last_name(TestData.address1_lastname)
        add_address_page.set_company(TestData.address1_company)
        add_address_page.set_address1(TestData.address1_address1)
        add_address_page.set_address2(TestData.address1_address2)
        add_address_page.set_city(TestData.address1_city)
        add_address_page.set_postcode(TestData.address1_postcode)
        add_address_page.select_country(TestData.address1_country)
        add_address_page.select_region_state(TestData.address1_state)
        add_address_page.select_default_address(TestData.address1_default_address)
        add_address_page.click_continue_button()
        address_success_msg = add_address_page.get_success_message()
        assert address_success_msg == "Your address has been successfully added"
        TestAddAddress.test_verify_address_info(add_address_page)
        # find the address just added
        # verify the address info is correct
    
    def test_verify_address_info(self):
        # Locate all table rows inside the table
        add_address_page=AddAddressPage(self.driver)
        rows = add_address_page.get_addresses_from_table()
        # Example usage: Click Edit or Delete for a specific row
        TestAddAddress.perform_action_on_address(self, rows, "Shawn20 LoPorto\nASI\n123 Forest Road\nAspen clone 2\nOuray, Colorado 81427\nUnited States", "edit")

    def test_delete_address_info(self):
        # login_page=LoginPage(self.driver)
        # login_page.set_email_address(TestData.email)
        # login_page.set_password(TestData.password)
        # my_account_page=login_page.click_login_button()
        TestLogin.test_standard_login(self)
        add_address_page=AddAddressPage(self.driver)
        add_address_page.click_right_menu_page("Address Book")
        add_address_page=AddAddressPage(self.driver)
        actual_title=add_address_page.get_page_title()
        assert actual_title == "Address Book Entries"
        # Locate all table rows inside the table
        rows = add_address_page.get_addresses_from_table()
        # Example usage: Click Edit or Delete for a specific row
        TestAddAddress.perform_action_on_address(self, rows, "Shawn20 LoPorto\nASI\n123 Forest Road\nAspen clone 2\nOuray, Colorado 81427\nUnited States", "delete")

### Methods to perform actions on addresses
    def read_address_name_counter():
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "addressNameCounter.txt"))
        file = open(filename, 'r+')
        ctr = file.read().strip()
        new_ctr = int(ctr) + 1
        file.seek(0)
        file.write(str(new_ctr))
        file.close()
        return ctr
    
    def perform_action_on_address(self, rows, target_address, action):
        add_address_page=AddAddressPage(self.driver)
        for index, row in enumerate(rows, start=1):
            # Extract the address text from the first column
            address_data = row.find_element(By.XPATH, ".//td[1]").text.strip()
            print(f"Row {index}: {address_data}")

            # Check if this is the target address
            if target_address in address_data:
                print(f"Found matching row for: {target_address}")

                match action:
                    case "edit":
                        print(f"Clicking Edit for: {target_address}")
                        add_address_page.click_address_book_entries_edit_button(index)
                        break
                    case "delete":
                        print(f"Clicking Delete for: {target_address}")
                        add_address_page.click_address_book_entries_delete_button(index)
                        break
                    case _:
                        print("Invalid action. Use 'edit' or 'delete'.")
                        break

###Create some test casses that are self-contained and do not depend on other test cases.
#Create a test that just logs in
#Create a test case that will add an address, verify the data, and then delete the address that was just created.
#Create a test case that will add an address, verify the data, and then edit the address info.