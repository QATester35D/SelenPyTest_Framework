from selenium.webdriver.common.by import By

class ChangePasswordLocatorFields:
    password_field = (By.ID, "input-password")
    confirm_password_field = (By.ID, "input-confirm")
    continue_button = (By.XPATH, "//div[@id='content']//input[@value='Continue']")
    confirmation_error_message = (By.CSS_SELECTOR, "#content .text-danger")

class LoginPageLocatorFields:
    email_address_field = (By.ID, "input-email")
    password_field = (By.ID, "input-password")
    login_button = (By.XPATH, "//div[@id='content']//input[@value='Login']")
    warning_message = (By.CSS_SELECTOR, "#account-login .alert-danger")
    new_customer_message = (By.CLASS_NAME, "card-body")
    website_main_message = (By.ID, "entry_217838")

class AddressLocatorFields:
    @staticmethod
    def get_edit_button_locator(index):
        """Returns the locator tuple for the Edit button of a specific row."""
        return (By.XPATH, f"//table[@class='table table-bordered table-hover']//tbody/tr[{index}]/td[2]/a[contains(@class, 'btn-info')]")
    
    @staticmethod
    def get_delete_button_locator(index):
        """Returns the locator tuple for the Edit button of a specific row."""
        return (By.XPATH, f"//table[@class='table table-bordered table-hover']//tbody/tr[{index}]/td[2]/a[contains(@class, 'btn-danger')]")

    main_page_title = (By.XPATH, "//h2[contains(text(), 'My Account')]")
    address_book_page_titles = (By.XPATH, "//div[@id='content']//h1")
    firstname_field = (By.ID, "input-firstname")
    lastname_field = (By.ID, "input-lastname")
    company_field = (By.ID, "input-company")
    address1_field = (By.ID, "input-address-1")
    address2_field = (By.ID, "input-address-2")
    city_field = (By.ID, "input-city")
    postcode_field = (By.ID, "input-postcode")
    country_field = (By.ID, "input-country")
    region_state_field = (By.ID, "input-zone")
    default_address_radio = (By.NAME, "default")
    new_address_button = (By.XPATH, "//a[contains(@class, 'btn-primary') and text()='New Address']")
    continue_button = (By.XPATH, "//div[@id='content']//input[@value='Continue']")
    success_message = (By.CSS_SELECTOR, "#content .alert-success")
    address_success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    return_all_addresses = (By.XPATH, "//table[@class='table table-bordered table-hover']//tbody/tr")
