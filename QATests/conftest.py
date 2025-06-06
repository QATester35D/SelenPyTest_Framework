from dotenv import load_dotenv
load_dotenv()
import json
import pytest
from selenium import webdriver
from QATests.db.db_connection import DatabaseOperations
from QATests.utilities.test_data import LambdaTestSiteTestData
import os

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

    yield # Run tests

    print("Close Browser")
    driver.quit()

# @pytest.fixture
# def open_url(request):
#     url = request.param
#     driver = request.cls.driver 
#     driver.get(url)
#     return driver

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