from selenium import webdriver

driver = webdriver.Safari()

driver.get("http://www.google.com")

driver.maximize_window()

print("Page Title is:", driver.title)

driver.quit()
