from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAssertionsHard():
    pass

    def test_Lambdatest_radio_button_demo_value():
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
        driver.find_element(By.XPATH,"//h4[contains(text(),'Gender')]//following::input[@value='Male']").click()
        driver.find_element(By.XPATH,"//h4[contains(text(),'Age')]//following::input[@value='15 - 50']").click()
        driver.find_element(By.XPATH,"//button[text()='Get values']").click()
        # gender = driver.find_element(By.CLASS_NAME,"genderbutton").text
        gender = driver.find_element(By.CSS_SELECTOR, ".genderbutton").text
        age_group = driver.find_element(By.CSS_SELECTOR,".groupradiobutton").text   
        # age_group = driver.find_element(By.CLASS_NAME,"groupradiobutton").text
        assert gender == "Male", "Gender is not correct"
        assert age_group == "15 - 50", "Age group is not correct"
        assert driver.title.__contains__("Selenium Grid Online")
        # assert "51" in age_group, "Age group is not correct" #intended to fail
        driver.close()
