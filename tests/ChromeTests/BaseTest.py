import unittest
from utils.driver_factory import get_driver
from pages.ChromePages.LoginPage import LoginPage
from utils.user_loader import load_users

class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.driver.maximize_window()
        cls.driver.get("https://www.saucedemo.com/")

        cls.login_page = LoginPage(cls.driver)

        # Perform login from json
        cls.login_as("standard_user")

    @classmethod
    def login_as(cls, user_type):
        users = load_users()
        user = users[user_type]
        cls.login_page.login(user["username"], user["password"])

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, "driver"):
            cls.driver.quit()
