from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://www.google.com")
driver.maximize_window()


print("Page Title is:", driver.title)

driver.quit()