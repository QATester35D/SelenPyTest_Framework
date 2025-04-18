This code base implements a Test Automation Framework that uses python and pytest, using a page object model approach to test a web based application, has a setup and teardown process of seeding data in a database and resetting the database after each test so that each test has a fresh seeded data set to work with. This automation also tests APIs. From the selenium test automation approach it utilizes reuse and data driven testing.

The Test Automation Framework being implemented consists of these key components:
'pytest.ini' - Test Configuration File
- Used to configure global settings for how pytest discovers, organizes, and executes tests across the entire framework.
- It defines the markers being used.
- It defines aspects of the test execution.

'conftest.py' - Configuration File
- Used to define some global fixtures
- Contains Setup/Teardown logic

'utilities' folder:
'locators.py' – Centralized Object Repository
- This file serves as the object repository for the test framework. It contains the element locators (e.g., 'By.ID', 'By.XPATH', 'By.CSS_SELECTOR') used by the page object classes to identify and interact with UI elements across the application under test.
- Each locator is typically defined as a class attribute, grouped logically by page or feature, to promote maintainability, reusability, and readability of test code. This allows tests and page objects to reference elements consistently without hardcoding XPaths or selectors in multiple files. This separation also makes it easier to update locators when the UI changes.

'test_data.py' - a file containing some defined test data to be used globally.

'api_client.py' - centralized CRUD methods for API calls to code.

'pages' folder - this contains files for various functionality on the website that help to reduce code. It primarily consists of methods to simplify identifying objects in code.

'db' folder:
- This contains database connections, database setup logic and various methods to be used against the database.

'tests' folder:
- This contains test files that contain tests within them to test the various features of the website, grouped by functionality.
- There are also methods created to simplify code and reusability.

'API' folder: contains some tests to demonstrate executing the various CRUD processes (post, get, put, delete) for API calls in addition to capturing information returned from a call that can be used as a parameter into another API call.

'data' folder: this contains various data files in different formats. These are used in data driven testing to show the different approaches that can be used.
- users.json is used in one of the API tests.
- the other data files are used primarily in the data driven tests contained in the "DemoPytest_NoPOM" folder. 

'DemoPytest_NoPOM' folder: this folder contains various test files that perform various tests showing different capabilities of selenium, python and pytest but without the page object model applied.

'AllureReport' folder: used for generating a test results report using Allure Reports.

'AutomationPyTestReport.html' - is a test results report that uses pytest-html for a standard looking test results report in html format.