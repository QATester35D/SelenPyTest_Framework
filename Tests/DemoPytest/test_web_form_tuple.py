import pytest
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Test Data
formTestData = [
    ("Jerry", "Seinfeld", "Comedian", "Grad", "Male", "4", "+40"),
    ("Cosmos", "Kramer", "Schmooch", "HighSchool", "NotSay", "1", "0"),
    ("George", "Costanza", "Yankees Executive", "College", "Male", "2", "+20"),
    ("Elaine", "Benes", "Copy Editor", "Grad", "Female", "1", "-12"),
    ("Estelle", "Costanza", "Mom", "HighSchool", "Female", "4", "+42"),
    ("Francis", "Newman", "Postman", "HighSchool", "NotSay", "3", "-24"),
    ("Helen", "Seinfeld", "Mom", "Grad", "Female", "2", "-2"),
]

# Helper Function to Calculate Date
def findDate(dateValue):
    """Converts a relative date string (e.g., "+40", "-12", "0") into a formatted date string."""
    if dateValue == "0":
        return date.today().strftime("%m/%d/%Y")

    symbol = dateValue[0]
    days_offset = int(dateValue[1:])
    
    if symbol == "+":
        new_date = date.today() + timedelta(days=days_offset)
    elif symbol == "-":
        new_date = date.today() - timedelta(days=days_offset)
    else:
        raise ValueError(f"Invalid date format: {dateValue}")

    return new_date.strftime("%m/%d/%Y")

# Pytest Fixture to Set Up and Tear Down WebDriver
# @pytest.fixture(scope="function") #Launch a new browser session for each data test iteration
@pytest.fixture(scope="session") #Reuse the same browser session for all data test iterations
def browser():
    driver = webdriver.Firefox()
    driver.set_window_size(800, 800)
    yield driver  # Provide the driver to the test
    driver.quit()

# Parametrize Test Function
@pytest.mark.parametrize(
    "first_name, last_name, job, education, gender, experience, dateAdjustment",
    formTestData
)
def test_form_submission(browser, first_name, last_name, job, education, gender, experience, dateAdjustment):
    """Fills out and submits the form, then verifies success message."""
    
    # Navigate to Form Page
    browser.get("https://formy-project.herokuapp.com/form")

    # Wait for the form to be ready
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )

    # Locate elements
    first_name_field = browser.find_element(By.ID, "first-name")
    last_name_field = browser.find_element(By.ID, "last-name")
    job_title_field = browser.find_element(By.ID, "job-title")
    ed_rb1 = browser.find_element(By.ID, "radio-button-1")  # HighSchool
    ed_rb2 = browser.find_element(By.ID, "radio-button-2")  # College
    ed_rb3 = browser.find_element(By.ID, "radio-button-3")  # Grad
    sex_male = browser.find_element(By.ID, "checkbox-1")
    sex_female = browser.find_element(By.ID, "checkbox-2")
    sex_not_say = browser.find_element(By.ID, "checkbox-3")
    experience_dropdown = Select(browser.find_element(By.ID, "select-menu"))
    date_picker = browser.find_element(By.ID, "datepicker")
    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")

    # Fill in form fields
    first_name_field.send_keys(first_name)
    last_name_field.send_keys(last_name)
    job_title_field.send_keys(job)

    # Education selection
    education_map = {
        "HighSchool": ed_rb1,
        "College": ed_rb2,
        "Grad": ed_rb3
    }
    education_map.get(education, lambda: print("Invalid education value")).click()

    # Gender selection
    gender_map = {
        "Male": sex_male,
        "Female": sex_female,
        "NotSay": sex_not_say
    }
    gender_map.get(gender, lambda: print("Invalid gender value")).click()

    # Experience selection
    experience_dropdown.select_by_value(experience)

    # Date selection
    date_picker.send_keys(findDate(dateAdjustment))
    date_picker.send_keys(Keys.TAB)

    # Submit form
    submit_button.click()

    # Verify submission success
    success_alert = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
    )
    
    assert success_alert.text == "The form was successfully submitted!", "Form submission failed!"
