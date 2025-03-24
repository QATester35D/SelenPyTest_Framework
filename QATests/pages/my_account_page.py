from QATests.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MyAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.my_account_page_header = (By.XPATH, "//h1[text()='My Account']")