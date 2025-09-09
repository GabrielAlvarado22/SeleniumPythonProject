import unittest
from selenium import webdriver
from pages.ChromePages.LoginPage import LoginPage
from utils.user_loader import load_users

class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the WebDriver, configure Chrome, open the site, and perform login
        cls.driver = webdriver.Chrome(options=cls._get_chrome_options())
        cls.driver.maximize_window()
        cls.driver.get("https://www.saucedemo.com/")
        cls.login_page = LoginPage(cls.driver)

        # Perform login using a standard user from JSON
        cls.login_as("standard_user")

    @classmethod
    def _get_chrome_options(cls):
        # Return Chrome options to configure browser behavior and disable automation alerts
        options = webdriver.ChromeOptions()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-password-manager-reauthentication")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument(
            "--disable-features=IsolateOrigins,site-per-process,PasswordLeakDetection,SafeBrowsing")
        options.add_argument("--incognito")
        return options

    @classmethod
    def login_as(cls, user_type):
        # Log in as a specified user type using credentials from JSON
        users = load_users()
        user = users[user_type]
        cls.login_page.login(user["username"], user["password"])

    @classmethod
    def tearDownClass(cls):
        # Close the WebDriver after all tests are finished
        if hasattr(cls, "driver"):
            cls.driver.quit()
