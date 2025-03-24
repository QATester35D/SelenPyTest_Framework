import pytest
from selenium import webdriver
from QATests.utilities.test_data import TestData

@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    match request.param:
        case "chrome":
            driver = webdriver.Chrome()
        case "firefox":
            driver = webdriver.Firefox()
        case "edge":
            driver = webdriver.Edge()
    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.get(TestData.url)
    driver.maximize_window()
    yield
    print("Close Browser")
    driver.close()
