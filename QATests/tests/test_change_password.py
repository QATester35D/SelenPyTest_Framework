import pytest
from QATests.pages.change_password_page import ChangePasswordPage
from QATests.pages.login_page import LoginPage
from QATests.tests.base_test import BaseTest
from QATests.utilities.test_data import LambdaTestSiteTestData

#This is for the website: https://ecommerce-playground.lambdatest.io/index.php?route=account/login

class TestChangePassword(BaseTest):

    @pytest.mark.regression
    def test_changing_password(self):
        self.driver.get(LambdaTestSiteTestData.url)
        login_page=LoginPage(self.driver)
        change_password_page=ChangePasswordPage(self.driver)
        expected_message="Password confirmation does not match password!"
        login_page.set_email_address(LambdaTestSiteTestData.email)
        login_page.set_password(LambdaTestSiteTestData.password)
        my_account_page=login_page.click_login_button()
        my_account_page.click_right_menu_page("Password")
        change_password_page.change_password("InvalidPassword", "InvalidConfirmPassword")
        actual_message=change_password_page.get_confirmation_error_message()
        assert actual_message == expected_message
        