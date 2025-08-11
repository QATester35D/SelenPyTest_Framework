SelenPyTest Framework
A robust Selenium-based Test Automation Framework implemented in Python using pytest and the Page Object Model (POM) design pattern.
This framework supports UI testing, API testing, database integration, and continuous integration with Jenkins, while incorporating custom assertion handling, data-driven testing, and automated test reporting.

📌 Features
- Page Object Model (POM) for modular, maintainable UI automation
- Selenium WebDriver for browser-based functional testing
- pytest for test discovery, execution, and reporting
- MySQL Database Integration with automated setup, teardown, and seeded test data
- Data-Driven Testing using JSON, CSV, and other formats
- API Testing (CRUD operations) with integrated Slack API/Webhooks for real-time notifications
- Custom Assertions with pass/fail logging and requirement traceability
- Jenkins CI/CD support for scheduled or on-demand test runs
- GitHub Actions CI/CD support for automatic test runs upon check-ins
- Allure Reports and pytest-html for rich test result visualization

🗂 Project Structure

SelenPyTest_Framework
 - pytest.ini                   # Global pytest configuration
 - conftest.py                  # Global fixtures, setup/teardown logic
 - assertions folder            # Custom assertion handlers
 - helpers folder               # Helper functions & reusable utilities
 - utilities folder             # Contains utility files of common functions
 - locators.py                  # Centralized object repository
 - test_data.py                 # Global test data definitions
 - api_client.py                # Centralized API CRUD methods
 - API folder                   # API test cases
 - pages folder                 # Page Object Model classes
 - db folder                    # DB connections, schema, and seed logic
 - data folder                  # External data files for data-driven tests
 - tests folder                 # Main pytest test suites (grouped by feature)
 - DemoPytest_NoPOM  folder     # Example tests without POM
 - AllureReport folder          # Allure report output
 - AutomationPyTestReport.html  # HTML test report output

🔍 Key Components
- pytest.ini – Defines global pytest settings, markers, and execution options
- conftest.py – Global fixtures and setup/teardown logic
- assertions/ – Custom assertions that log pass/fail outcomes without halting execution unless critical
- helpers/ – Utility methods for site interactions and assertion handling
- utilities/locators.py – Centralized locators for all POM classes
- api_client.py – CRUD methods for interacting with APIs
- db/ – Database connection handling, schema loading, and test data seeding
- data/ – JSON/CSV/other data files for parameterized tests
- pages/ – Page classes encapsulating locators and actions for specific application pages
- API/ – API test cases demonstrating GET, POST, PUT, DELETE operations
- DemoPytest_NoPOM/ – Standalone pytest/Selenium examples without the POM pattern

🌐 Target Applications
The framework includes tests against:
- E-commerce Playground
https://ecommerce-playground.lambdatest.io/index.php?route=account/login
(Some automation features limited in CI environments)
- Selenium Form Page
https://www.selenium.dev/selenium/web/formPage.html
- Slack API & Webhooks for notification and integration testing

🛠 Setup & Installation
1. Clone the repository
git clone https://github.com/QATester35D/SelenPyTest_Framework.git
cd SelenPyTest_Framework

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables
(e.g., database credentials, Slack webhook URL)

▶️ Running Tests
- Run all tests
pytest

- Run with HTML report
pytest --html=AutomationPyTestReport.html

- Run with Allure Report
pytest --alluredir=AllureReport
allure serve AllureReport

- Run specific test file
pytest tests/test_form_page.py

📊 Reporting
- pytest-html – Generates AutomationPyTestReport.html
- Allure Reports – Interactive, visual test reporting
- Slack Notifications – Optional integration for posting results to Slack channels

🚀 CI/CD Integration
This framework is Jenkins-ready and setup in GitHub Actions:
- Configure a Jenkins pipeline
- Install necessary plugins (Allure Jenkins Plugin, HTML Publisher Plugin)
- Trigger tests on commit, schedule, or manually
- This GitHub repository has GitHub Actions setup to run syntax checks, builds and run tests.

📜 License
This project is licensed under the MIT License.