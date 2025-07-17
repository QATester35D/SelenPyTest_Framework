This project implements a Test Automation Framework that uses selenium, python and pytest using a page object model approach to test several web based applications, has a setup and teardown process of seeding data in a MySQL database and resetting the database after each test so that each test has a fresh seeded dataset to work with. It demonstrates data-driven testing for some of the tests, and also performs some API testing and utilizes Webhooks and API calls for reporting into Slack. The test automation approach utilizes code/method reuse and helper methods.

The tests can also be run from Jenkins CI/CD.

The main public websites used in testing are:
- "https://ecommerce-playground.lambdatest.io/index.php?route=account/login" (this site limits automation capabilities when running from a test agent or Jenkins CI)
- "https://www.selenium.dev/selenium/web/formPage.html" (this is a site created by Selenium)

API coding & testing: several sites are used including Slack. Most API sites either restrict you from performing Post or Put calls since those calls are updating the remote host or they implement a mock stub so the data isn't really updated there so you can't execute a Get after a Post to validate that the data was successfully updated like you would in normal testing. The Post or Put will execute and return a 200 response but the data doesn't get updated. Due to this I created a Slack workspace and implemented some Slack notifications using the Slack API and Webhooks since I can then actually do posts to the Slack workspace to simulate notifications.

Database testing is done with a MySQL database locally. This is used to demonstrate interacting with a database using SQL commands and implementing a Setup and Teardown as part of the the test automation process.

The Test Automation Framework being implemented consists of these key components:

'pytest.ini' - Test Configuration File
- Used to configure global settings for how pytest discovers, organizes, and executes tests across the entire framework.
- It defines the markers being used.
- It defines aspects of the test execution.

'conftest.py' - Configuration File
- Used to define some global fixtures
- Contains Setup/Teardown logic

'assertions' folder: This is for my custom assertion approach. A normal assert won't log anything when the assert passes and will terminate execution if there is a failure. I implemented an assertion approach to log both pass and fail results, requirement IDs, description and continue testing. If there is a validation that should fail the test execution, then a regular assert statement will be used.

'helpers' folder: 
- contains helper files for the various sites that includes methods to help with common processes and simplify test code.
- contains files for handling the custom assertions

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