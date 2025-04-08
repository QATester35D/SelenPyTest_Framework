from QATests.pages.base_page import BasePage
from QATests.pages.my_account_page import MyAccountPage
from QATests.utilities.locators import AddressLocatorFields
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MethodRegistry:
    """Registry of method names for dynamic execution."""
    ADDRESS_PAGE_GET_METHODS = {
        "get_first_Name":"firstName",
        "get_last_name":"lastName",
        "get_company":"company",
        "get_address1":"address1",
        "get_address2":"address2",
        "get_city":"city",
        "get_postcode":"postcode",
        "get_country":"country",
        "get_region_state":"state",
        "get_default_address":"default_address"
    }

class AddressPage(BasePage):

    def __init__(self, driver):
        self.locate = AddressLocatorFields
        super().__init__(driver)

    def click_new_address_button(self):
        self.click(self.locate.new_address_button)

    def firstName(self, first_name=None):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locate.firstname_field)
        )
        if first_name is None:
            return element.get_attribute("value")
        else:
            self.set(self.locate.firstname_field, first_name)

    def lastName(self, last_name=None):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locate.lastname_field)
        )
        if last_name is None:
            return element.get_attribute("value")
        else:
            self.set(self.locate.lastname_field, last_name)

    def company(self, company_name=None):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locate.company_field)
        )
        if company_name is None:
            return element.get_attribute("value")
        else:
            self.set(self.locate.company_field, company_name)

    def address1(self, address1=None):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locate.address1_field)
        )
        if address1 is None:
            return element.get_attribute("value")
        else:
            self.set(self.locate.address1_field, address1)

    def address2(self, address2=None):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locate.address2_field)
        )
        if address2 is None:
            return element.get_attribute("value")
        else:
            self.set(self.locate.address2_field, address2)

    def city(self, city_name=None):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locate.city_field)
        )
        if city_name is None:
            return element.get_attribute("value")
        else:
            self.set(self.locate.city_field, city_name)

    def postcode(self, postcode=None):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locate.postcode_field)
        )
        if postcode is None:
            return element.get_attribute("value")
        else:
            self.set(self.locate.postcode_field, postcode)

    def country(self, country_name=None):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locate.country_field)
        )
        if country_name is None:
            dropdown = Select(self.find(*self.locate.country_field))
            selected_option = dropdown.first_selected_option
            return selected_option.text
        else:
            self.select(self.locate.country_field, country_name)

    def state(self, region_state_name=None):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locate.region_state_field)
        )
        if region_state_name is None:
            dropdown = Select(self.find(*self.locate.region_state_field))
            selected_option = dropdown.first_selected_option
            return selected_option.text
        else:
            self.select(self.locate.region_state_field, region_state_name)
    
    def default_address(self, value=None):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locate.default_address_radio)
        )
        if value is None:
            return element.get_attribute("value")
        else:
            self.select_radio_button(self.locate.default_address_radio, value)
    
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