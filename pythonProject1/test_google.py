from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.google.com/')
assert "Google" in driver.page_source
driver.quite()