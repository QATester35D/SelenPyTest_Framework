from QATests.tests.base_test import BaseTest
from QATests.helpers.page_synchronization import PageSynchronization
from QATests.helpers.checkbox_validation import CheckboxValidation
from QATests.helpers.button_validation import ButtonValidation
from QATests.utilities.test_data import WebFormPageTestData
from QATests.pages.form_page import FormPage
from QATests.utilities.formPageLocators import FormPageLocatorFields
import logging

##########################################################################################
###########                   Refactoring now...                               ###########
##########################################################################################
# Test automaton scripts using Pytest Page Object Model
# This automation is against a web form, specifically the Selenium webform:
#  https://www.selenium.dev/selenium/web/formPage.html. Normally I would automate the whole
#  form in one test, but this is not a normal form so I'm creating tests to check the form in 
#  groups/sections of "perceived functionality".
##########################################################################################

logger = logging.getLogger(__name__)

class TestWebFormPage(BaseTest):

    def test_filling_top_section(self, assert_helper):
        # This test addresses the top 2 text fields, two buttons and 4 checkboxes
        #Class instantiation
        bv=ButtonValidation(self.driver)
        fpFields=FormPageLocatorFields
        chkbox=CheckboxValidation(self.driver)
        sync=PageSynchronization(self.driver)
        form_page=FormPage(self.driver)

        logger.info("Testing the test_filling_top_section functionality.")
        self.driver.get(WebFormPageTestData.webFormPageURL)
        form_page.set_email_field("sloporto@asi-test.com")
        form_page.set_age_field("21")

        bv.validate_submit_button_label(form_page,assert_helper)
        bv.validate_submit_button_alt_text_label(form_page,assert_helper)

        form_page.click_hello_there_button()
        sync.arrival_page_sync(assert_helper)
        self.driver.back()
        sync.main_page_sync(assert_helper)
        form_page.click_image_button()
        sync.arrival_page_sync(assert_helper)
        self.driver.back()
        sync.main_page_sync(assert_helper)
        #Verify checky checkboxes now
        logger.info("Checking the checky checkboxes now.")
        chkbox.validate_initial_checky_checkboxes_state()

# twfp=TestWebFormPage()
# twfp.test_filling_top_section()
# time.sleep(1)
