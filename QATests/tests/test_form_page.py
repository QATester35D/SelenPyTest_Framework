from selenium.webdriver.common.by import By
from selenium import webdriver
from QATests.tests.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from QATests.utilities.formPageLocators import FormPageLocatorFields
from QATests.utilities.test_data import WebFormPageTestData
from QATests.pages.form_page import FormPage
import random
import requests
import time

##########################################################################################
#                               Refactoring now...
##########################################################################################
# Test automaton scripts using Pytest Page Object Model
# This automation is against a web form. Normally I would automate the whole
#   form in one test, but this is not a normal form so I'm creating tests to 
#   check the form in groups/sections of perceived "functionality".
##########################################################################################
# Methods
#Needs refactoring
# Done - 1. Pull out object definitions into page definitions
#   2. Create page methods for each object type
#   3. Group the functionality into perceived "features"

class TestWebFormPage(BaseTest):
    # def __init__(self, url):
    #     #Attributes of the WebOrderForm class here
    #     self.url = url   # self.url = "https://www.selenium.dev/selenium/web/formPage.html"

    # #The following are methods for the behavior and actions - this is mixed and why it should be refactored later
    # def launchPage(self):
    #     seleniumDevbrowser = webdriver.Firefox()
    #     print("Now working with the Selenium Dev webpages - the web form page")
    #     seleniumDevbrowser.get(self.url)
    #     seleniumDevbrowser.set_window_size(900, 800)
    #     return(seleniumDevbrowser)
    def test_filling_top_section(self):
        self.driver.get(WebFormPageTestData.webFormPageURL)
        form_page=FormPage(self.driver)
        form_page.set_email_field("sloporto@asi-test.com")
        form_page.set_age_field("21")
        form_page.click_hello_button()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
