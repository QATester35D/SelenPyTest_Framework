from selenium import webdriver
from selenium.webdriver.common.by import By

def test_search_lambdatest_ecommerce():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    search = driver.find_element(By.XPATH, "//input[@placeholder='Search For Products']").send_keys("iphone")
    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    search_value=driver.find_element(By.XPATH, "//h1[contains(text(),'Search')]").text
    assert "iphone" in search_value
    driver.close()
