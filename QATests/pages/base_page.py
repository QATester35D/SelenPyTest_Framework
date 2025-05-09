from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    """
    The Purpose Of This BasePage Is To Contain Methods Common To All Page Objects
    """
    def __init__(self, driver):
        self.driver = driver

    def wait_for_clickable(self, locator, timeout=10):
        return self.wait_for_element(locator, timeout, EC.element_to_be_clickable)

    def find(self, *locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)
    
    def click(self, locator):
        self.find(*locator).click()
        # self.driver.find_element(*locator).click()

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text
    
    def get_page_title_text(self, locator):
        element = self.find(*locator)
        return element.text

    def get_title(self):
        return self.driver.title
    
    def click_right_menu_page(self, page_name):
        # self.click(self.page(page_name))
        page = By.XPATH, "//aside[@id='column-right']//a[text()=' "+ page_name +"']"
        self.click(page)

    # Below method allows us to click the page, check if page is visible, & more actions
    def page(sef, page_name):
        return By.XPATH, "//aside[@id='column-right']//a[text()=' "+ page_name +"']"
    
    # def select(self, locator, value):
    #     self.find(*locator).click()
    #     self.find(*locator).select_by_visible_text(value)

    def select(self, locator, value):
        time.sleep(1) # wait_until does not work: element=wait.until(EC.visibility_of_element_located(locator))
        dropdown = Select(self.find(*locator))
        dropdown.select_by_visible_text(value)

    def select_radio_button(self, locator, value):
        group_by, group_name = locator
        radio_button_locator = (By.XPATH, f"//input[@{group_by}='{group_name}'][@value='{value}']")
        radio_button = self.driver.find_element(*radio_button_locator)
        
        if not radio_button.is_selected():
            radio_button.click()
