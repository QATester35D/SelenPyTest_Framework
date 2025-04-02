from QATests.pages.base_page import BasePage
from QATests.pages.my_account_page import MyAccountPage
from QATests.utilities.locators import AddAddressLocatorFields
from selenium.webdriver.common.by import By

class AddAddressPage(BasePage):

    def __init__(self, driver):
        self.locate = AddAddressLocatorFields
        super().__init__(driver)

    def click_new_address_button(self):
        self.click(self.locate.new_address_button)

    def set_first_name(self, first_name):
        self.set(self.locate.firstname_field, first_name)

    def set_last_name(self, last_name):
        self.set(self.locate.lastname_field, last_name)

    def set_company(self, company_name):
        self.set(self.locate.company_field, company_name)

    def set_address1(self, address1):
        self.set(self.locate.address1_field, address1)

    def set_address2(self, address2):
        self.set(self.locate.address2_field, address2)

    def set_city(self, city_name):
        self.set(self.locate.city_field, city_name)

    def set_postcode(self, postcode):
        self.set(self.locate.postcode_field, postcode)

    def select_country(self, country_name):
        self.select(self.locate.country_field, country_name)

    def select_region_state(self, region_state_name):
        self.select(self.locate.region_state_field, region_state_name)
    
    def select_default_address(self, value):
        self.select_radio_button(self.locate.default_address, value)
    
    def click_continue_button(self):
        self.click(self.locate.continue_button)
        return MyAccountPage(self.driver)
    
    def get_page_title(self):
        return self.get_page_title_text(self.locate.address_book_page_titles)
    
    def get_success_message(self):
        return self.get_text(self.locate.address_success_message)
    
    def get_addresses_from_table(self):
        rows = self.find_elements(*self.locate.return_all_addresses)
        return rows
    
    # def get_individual_address(self):
    #     address_data = self.find(By.XPATH, "./td[1]").text  # Extracts only the first <td> (Address content)
    #     return address_data
    
    def click_address_book_entries_edit_button(self, index):
        edit_button_locator = self.locate.get_edit_button_locator(index)  # Get locator tuple
        edit_button = self.driver.find_element(*edit_button_locator)  # Unpack tuple
        edit_button.click() 

    def click_address_book_entries_delete_button(self, index):
        delete_button_locator = self.locate.get_delete_button_locator(index)  # Get locator tuple
        delete_button = self.driver.find_element(*delete_button_locator)  # Unpack tuple
        delete_button.click() 