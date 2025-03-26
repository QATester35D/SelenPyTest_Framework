from QATests.pages.base_page import BasePage
from QATests.pages.my_account_page import MyAccountPage
from QATests.utilities.locators import AddAddressLocatorFields
from selenium.webdriver.common.by import By

class AddAddressPage(BasePage):

    def __init__(self, driver):
        self.locate = AddAddressLocatorFields
        super().__init__(driver)

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
    