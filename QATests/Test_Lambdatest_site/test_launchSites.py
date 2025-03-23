from selenium import webdriver

def test_lambdatest_playground():
  driver = webdriver.Firefox()
  driver.maximize_window()
  driver.get("https://www.lambdatest.com/selenium-playground/")
  print("Print the Title: ", driver.title)
  driver.close()

def test2_lambdatest_ecommerce():
  driver = webdriver.Firefox()
  driver.maximize_window()
  driver.get("https://ecommerce-playground.lambdatest.io/")
  print("Print the Title: ", driver.title)
  driver.close()

def testASIWebsite():
  driver = webdriver.Firefox()
  driver.maximize_window()
  driver.get("https://asi-test.com")
  webSiteTitle2 = driver.title
  print("Print the Title: ", driver.title)
  driver.close()
