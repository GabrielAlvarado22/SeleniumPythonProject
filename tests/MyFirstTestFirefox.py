from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Firefox(options=options)

driver.get("http://www.google.com")

print("Page Title is:", driver.title)

driver.quit()
