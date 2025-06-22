from QATests.tests.base_test import BaseTest
from QATests.helpers.webFormPage_helpers import PageSynchronization, CheckboxValidation
from QATests.utilities.test_data import WebFormPageTestData
from QATests.pages.form_page import FormPage
from QATests.utilities.formPageLocators import FormPageLocatorFields
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
        #This code addresses the top 2 text fields, two buttons and 4 checkboxes
        fpFields=FormPageLocatorFields
        self.driver.get(WebFormPageTestData.webFormPageURL)
        chkbox=CheckboxValidation(self.driver)
        sync=PageSynchronization(self.driver)
        form_page=FormPage(self.driver)
        form_page.set_email_field("sloporto@asi-test.com")
        form_page.set_age_field("21")
        button_label=form_page.get_hello_there_button_label()
        assert button_label == "Hello there", f"Expected to get the button value: 'Hello there', but got {button_label}"
        alt_text=form_page.get_image_button_alt_text()
        assert alt_text == "click me!", f"Expected to get the button alt text: 'click me!', but got {alt_text}"
        form_page.click_hello_there_button()
        sync.arrival_page_sync()
        self.driver.back()
        sync.main_page_sync()
        form_page.click_image_button()
        sync.arrival_page_sync()
        self.driver.back()
        sync.main_page_sync()
        #Verify checky checkboxes now
        chkbox.validate_initial_checky_checkboxes_state()

