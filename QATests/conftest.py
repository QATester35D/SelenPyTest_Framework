import json
import pytest
from selenium import webdriver
from QATests.utilities.test_data import TestData
import os

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
    # driver.close()
    driver.quit()

@pytest.fixture
def load_api_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__), "data", "users.json")
    with open(json_file_path, "r") as file:
        data = json.load(file)
    return data