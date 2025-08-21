import softest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAssertionsSoft(softest.TestCase):
    pass

    def test_Lambdatest_radio_button_demo_value(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
        driver.find_element(By.XPATH,"//h4[contains(text(),'Gender')]//following::input[@value='Male']").click()
        driver.find_element(By.XPATH,"//h4[contains(text(),'Age')]//following::input[@value='15 - 50']").click()
        driver.find_element(By.XPATH,"//button[text()='Get values']").click()
        gender = driver.find_element(By.CSS_SELECTOR, ".genderbutton").text
        age_group = driver.find_element(By.CSS_SELECTOR,".groupradiobutton").text   
        self.soft_assert(self.assertIs,"Male", gender, "Gender is not correct")
        # self.soft_assert(self.assertTrue,"Male", gender)
        self.soft_assert(self.assertTrue, driver.title.__contains__("Selenium Grid Online"))
        self.soft_assert(self.assertIn, "51",age_group, "Age group is not correct") #intended to fail
        driver.close()
        self.assert_all("Verify Gender, Title and Age group")
