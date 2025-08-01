import pytest
from QATests.pages.address_page import AddressPage, MethodRegistry
from QATests.tests.base_test import BaseTest
from QATests.helpers.login_helpers import perform_standard_login
from QATests.utilities.test_data import LambdaTestSiteTestData
from QATests.utilities.locators import AddressLocatorFields
from selenium.webdriver.common.by import By
import os

#This is for the website: https://ecommerce-playground.lambdatest.io/index.php?route=account/login

class TestAddAddress(BaseTest):

    #This is a test case to add an address into the Address Book
    @pytest.mark.smoke
    def test_add_address(self):
        self.driver.get(LambdaTestSiteTestData.url)
        perform_standard_login(self.driver, LambdaTestSiteTestData.email, LambdaTestSiteTestData.password)
        add_address_page=AddressPage(self.driver)
        add_address_page.click_right_menu_page("Address Book")
        actual_title=add_address_page.get_page_title()
        assert actual_title == "Address Book Entries"
        add_address_page.click_new_address_button()
        actual_title=add_address_page.get_page_title()
        assert actual_title == "Add Address"
        nameCounter=TestAddAddress.increment_get_address_name_counter()
        makingFirstNameUnique=LambdaTestSiteTestData.address1_firstName+nameCounter
        add_address_page.firstName(makingFirstNameUnique)
        add_address_page.lastName(LambdaTestSiteTestData.address1_lastName)
        add_address_page.company(LambdaTestSiteTestData.address1_company)
        add_address_page.address1(LambdaTestSiteTestData.address1_address1)
        add_address_page.address2(LambdaTestSiteTestData.address1_address2)
        add_address_page.city(LambdaTestSiteTestData.address1_city)
        add_address_page.postcode(LambdaTestSiteTestData.address1_postcode)
        add_address_page.country(LambdaTestSiteTestData.address1_country)
        add_address_page.state(LambdaTestSiteTestData.address1_state)
        add_address_page.default_address(LambdaTestSiteTestData.address1_default_address)
        add_address_page.click_continue_button()
        address_success_msg = add_address_page.get_success_message()
        assert address_success_msg == "Your address has been successfully added"
        return nameCounter # Return the name counter for further use
    
    @pytest.mark.functional
    def test_verify_address_info(self):
        # Login into the application, add an address, and verify the data
        val = TestAddAddress.test_add_address(self)
        rows = TestAddAddress.select_address_book_right_menu(self)
        address_page = AddressPage(self.driver)
        firstName=LambdaTestSiteTestData.address1_firstName+str(val) #Used to identify the address to edit
        TestAddAddress.perform_action_on_address(self, rows, TestAddAddress.build_target_address(self, firstName), "edit")
        #setup a loop to get the address info from the form and verify it is correct
        for address_method in MethodRegistry.ADDRESS_PAGE_GET_METHODS:
            # Get the method name from the registry
            fieldName = MethodRegistry.ADDRESS_PAGE_GET_METHODS[address_method]
            dataFieldName = "address1_"+fieldName
            # Call the method dynamically using getattr
            if fieldName == "firstName":
                firstNameValueFromPage = getattr(address_page, fieldName)()
                actualFieldValue = firstNameValueFromPage[:-len(str(val))]
            elif fieldName == "default_address":
                selected_radio_value = next(rb.get_attribute("value") for rb in self.driver.find_elements(*AddressLocatorFields.default_address_radio) if rb.is_selected())
                actualFieldValue = selected_radio_value if selected_radio_value else "0"
            else:                   
                actualFieldValue = getattr(address_page, fieldName)()
            expectedFieldValue = getattr(LambdaTestSiteTestData, dataFieldName)
            assert actualFieldValue == expectedFieldValue, f"Expected {fieldName} to be {expectedFieldValue}, but got {actualFieldValue}"
            print(f"Expected the value: {expectedFieldValue} and the Actual value is: {actualFieldValue}")

    @pytest.mark.integration
    def test_delete_address_info(self):
        val = TestAddAddress.test_add_address(self)
        rows = TestAddAddress.select_address_book_right_menu(self)
        address_page = AddressPage(self.driver)
        firstName = LambdaTestSiteTestData.address1_firstName+str(val) #Used to identify the address to edit
        TestAddAddress.perform_action_on_address(self, rows, TestAddAddress.build_target_address(self, firstName), "delete")
        # Verify the address is deleted
        rows = address_page.get_addresses_from_table() # re-retrieve the rows after deletion
        targetAddress = TestAddAddress.build_target_address(self, firstName)
        if TestAddAddress.verify_deletion(self, rows, targetAddress):
            print(f"Address {firstName} successfully deleted.")

    # This test case is intended to show the same logic as the one above while demonstrating getting the test data from a database instead
    @pytest.mark.integration
    def test_delete_address_db_info(self, setup_database):
        rowCount=setup_database.db_check_count("users")
        if rowCount != 0:
            userInfo=setup_database.db_get_full_user_info()
            TestAddAddress.map_data_from_db(userInfo)
        val = TestAddAddress.test_add_address(self)
        rows = TestAddAddress.select_address_book_right_menu(self)
        address_page = AddressPage(self.driver)
        firstName = LambdaTestSiteTestData.address1_firstName+str(val) #Used to identify the address to edit
        TestAddAddress.perform_action_on_address(self, rows, TestAddAddress.build_target_address(self, firstName), "delete")
        # Verify the address is deleted
        rows = address_page.get_addresses_from_table() # re-retrieve the rows after deletion
        targetAddress = TestAddAddress.build_target_address(self, firstName)
        if TestAddAddress.verify_deletion(self, rows, targetAddress):
            print(f"Address {firstName} successfully deleted.")

####################################################
### Methods to perform actions on addresses
####################################################
    def select_address_book_right_menu(self):
        address_page=AddressPage(self.driver)
        address_page.click_right_menu_page("Address Book")
        actual_title=address_page.get_page_title()
        assert actual_title == "Address Book Entries"
        return address_page.get_addresses_from_table()
    
    def increment_get_address_name_counter():
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "addressNameCounter.txt"))
        file = open(filename, 'r+')
        ctr = file.read().strip()
        new_ctr = int(ctr) + 1
        file.seek(0)
        file.write(str(new_ctr))
        file.close()
        return ctr

    def get_address_name_counter():
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "addressNameCounter.txt"))
        file = open(filename, 'r')
        ctr = file.read().strip()
        file.close()
        return ctr
    
    def perform_action_on_address(self, rows, target_address, action):
        address_page=AddressPage(self.driver)
        #Need to update to handle if the address is not found
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
                        address_page.click_address_book_entries_edit_button(index)
                        break
                    case "delete":
                        print(f"Clicking Delete for: {target_address}")
                        address_page.click_address_book_entries_delete_button(index)
                        break
                    case _:
                        print("Invalid action. Use 'edit' or 'delete'.")
                        break

    def verify_deletion(self, rows, target_address):
        # Check if the address is still present in the table
        for index, row in enumerate(rows, start=1):
            address_data = row.find_element(By.XPATH, ".//td[1]").text.strip()
            if target_address in address_data:
                print(f"Address {target_address} still exists in row {index}. Deletion failed.")
                return False
        print(f"Address {target_address} successfully deleted.")
        return True
    
    def build_target_address(self, firstName):
        addressDataName=["firstName","lastName","company","address1","address2","city","state","postcode","country"]
        for dataName in addressDataName:
            # Get the method name from the registry
            match dataName:
                case "firstName":
                    targetAddress = firstName
                case "lastName":
                    dataFieldName = "address1_"+dataName
                    value = getattr(LambdaTestSiteTestData, dataFieldName)
                    targetAddress += " " + value
                case "company" | "address1" | "address2" | "city":
                    dataFieldName = "address1_"+dataName
                    value = getattr(LambdaTestSiteTestData, dataFieldName)
                    targetAddress += "\n" + value
                case "state":
                    dataFieldName = "address1_"+dataName
                    value = getattr(LambdaTestSiteTestData, dataFieldName)
                    targetAddress += ", " + value
                case "postcode":
                    dataFieldName = "address1_"+dataName
                    value = getattr(LambdaTestSiteTestData, dataFieldName)
                    targetAddress += " " + value
                case "country":
                    dataFieldName = "address1_"+dataName
                    value = getattr(LambdaTestSiteTestData, dataFieldName)
                    targetAddress += "\n" + value
        return targetAddress
    
    def map_data_from_db(db_data):
        LambdaTestSiteTestData.address1_firstName = db_data[0]["first_name"]
        LambdaTestSiteTestData.address1_lastName = db_data[0]["last_name"]
        LambdaTestSiteTestData.address1_company = db_data[0]["company_name"]
        LambdaTestSiteTestData.address1_address1 = db_data[0]["address1"]
        LambdaTestSiteTestData.address1_address2 = db_data[0]["address2"]
        LambdaTestSiteTestData.address1_city = db_data[0]["city"]
        LambdaTestSiteTestData.address1_postcode = db_data[0]["zip_code"]
        LambdaTestSiteTestData.address1_country = db_data[0]["country"]
        LambdaTestSiteTestData.address1_state = db_data[0]["state"]
        LambdaTestSiteTestData.address1_default_address = "0"
