import json
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from QATests.db.db_connection import DatabaseOperations
from QATests.utilities.test_data import LambdaTestSiteTestData
from QATests.helpers.webFormPage_assertLoggingHelpers import AssertHelper, AssertTracker
from datetime import datetime
import os
import sys
import logging

load_dotenv()
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def page_factory(driver):
    def _get_page(PageClass):
        return PageClass(driver)
    return _get_page

@pytest.fixture
def assert_helper():
    AssertTracker().reset()
    return AssertHelper()

@pytest.fixture(autouse=True)
def finalize_assertions():
    yield  # Run the test
    AssertTracker().assert_all()

def pytest_metadata(metadata):
    metadata['Project'] = "Webpage Customer Portal"
    metadata['PI'] = "Program Increment - PI 2025_2"
    metadata['Sprint'] = "Sprint 3"
    metadata['Tester'] = "Shawn LoPorto"

# === Browser Fixture ===
@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    match request.param:
        case "chrome":
            driver = webdriver.Chrome()
        case "firefox":
            driver = webdriver.Firefox()
        # case "edge":
        #     driver = webdriver.Edge()
    request.cls.driver = driver
    print("Browser: ", request.param)
    # driver.get(TestData.url)
    # driver.maximize_window()

    yield driver # Run tests

    print("Close Browser")
    driver.quit()

# @pytest.fixture
# def open_url(request):
#     url = request.param
#     driver = request.cls.driver 
#     driver.get(url)
#     return driver

# Automatically enable caplog logging for all tests
@pytest.fixture(autouse=True)
def enable_caplog(caplog):
    yield caplog

# This will store captured log output per test
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()
    # Only act on actual test calls, not setup/teardown, and only write out screenshots on failures
    #  The "enable_caplog" above writes out the log info from the logger calls
    if report.when == "call":
        # Screenshot on failure
        if report.failed:
            driver = getattr(item.cls, "driver", None) or item.funcargs.get("driver", None)
            if driver:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"{item.name}_{timestamp}.png"
                screenshot_dir = os.path.join("reports", "screenshots")
                os.makedirs(screenshot_dir, exist_ok=True)
                screenshot_path = os.path.join(screenshot_dir, filename)

                driver.save_screenshot(screenshot_path)

                # Attach screenshot to HTML report (if using pytest-html)
                if item.config.pluginmanager.hasplugin("html"):
                    from pytest_html import extras
                    extra = getattr(report, "extra", [])
                    extra.append(extras.image(screenshot_path))
                    report.extra = extra

# === Database Setup/Teardown ===
@pytest.fixture(scope="function", autouse=True)
def setup_database():
    dbHelpers=DatabaseOperations()
    cursor=dbHelpers.cur
    # Load and run schema.sql
    base_path = os.path.dirname(__file__)
    db_path = os.path.join(base_path, "db")
    with open(os.path.join(db_path, "schema.sql"), "r") as f:
        schema_sql = f.read()
        for stmt in schema_sql.split(';'):
            if stmt.strip():
                cursor.execute(stmt)

    # Load and run seed_data.sql
    with open(os.path.join(db_path, "seed_data.sql"), "r") as f:
        seed_sql = f.read()
        for stmt in seed_sql.split(';'):
            if stmt.strip():
                cursor.execute(stmt)

    dbHelpers.mydb.commit()
    print("Database setup complete.")

    yield dbHelpers # Run tests and pass in the database helper object 

    # Teardown: drop the test tables
    cursor.execute("DROP TABLE IF EXISTS products;")
    cursor.execute("DROP TABLE IF EXISTS users;")
    dbHelpers.mydb.commit()
    cursor.close()
    dbHelpers.mydb.close()
    print("Database teardown complete.")

@pytest.fixture
def load_api_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__), "data", "users.json")
    with open(json_file_path, "r") as file:
        data = json.load(file)
    return data