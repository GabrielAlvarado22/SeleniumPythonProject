import unittest
from selenium import webdriver

from pages.ChromePages.LoginPage import LoginPage

class BaseTest(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
        }

        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-password-manager-reauthentication")
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument(
            "--disable-features=IsolateOrigins,site-per-process,PasswordLeakDetection,SafeBrowsing")
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        self.login_page = LoginPage(self.driver)
        self.login_page.login("standard_user", "secret_sauce")

    def tearDown(self):
        self.driver.quit()
