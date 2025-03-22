import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("num1, num2, expected total", [
    ("25", "25", "50"), ("10", "10", "30"), ("30", "40", "70")])

def test_lambdatest_two_input_fields(num1, num2, expected_total):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://lambdatest.com/selenium-playground/simple-form-demo")
    driver.find_element(By.ID, "sum1").send_keys(num1)
    driver.find_element(By.ID, "sum2").send_keys(num2)
    driver.find_element(By.XPATH, "//button[text()='Get Sum']").click()
    actual_total = driver.find_element(By.ID, "addmessage").text
    assert actual_total == expected_total, f"Expected total is {expected_total}, but got {actual_total}"