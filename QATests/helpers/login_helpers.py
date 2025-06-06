from QATests.pages.login_page import LoginPage
# from QATests.utilities.test_data import LambdaTestSiteTestData
from QATests.utilities.locators import AddressLocatorFields
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform_standard_login(driver, email, password):
    login_page=LoginPage(driver)
    login_page.set_email_address(email)
    login_page.set_password(password)
    login_page.click_login_button() #This is actually a custom method that will sync and click on the login button
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(AddressLocatorFields.main_page_title))
    actual_title=login_page.get_title()
    assert actual_title == "My Account"
