from QATests.tests.base_test import BaseTest
from QATests.helpers.webFormPage_helpers import PageSynchronization
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

    def test_filling_top_section(self):
        self.driver.get(WebFormPageTestData.webFormPageURL)
        sync=PageSynchronization(self.driver)
        form_page=FormPage(self.driver)
        form_page.set_email_field("sloporto@asi-test.com")
        form_page.set_age_field("21")
        form_page.click_hello_there_button()
        sync.arrival_page_sync()
        self.driver.back()
        sync.main_page_sync()
        form_page.click_image_button()
        sync.arrival_page_sync()
        self.driver.back()
        sync.main_page_sync()
