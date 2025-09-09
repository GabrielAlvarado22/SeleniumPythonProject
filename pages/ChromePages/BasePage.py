from selenium.webdriver.common.by import By
from utils.WaitUtils import WaitUtils  # import our WaitUtils


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait_utils = WaitUtils(driver)  # initialize WaitUtils

        # ==== LOCATORS ====
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")

    # ==== ACTIONS ====
    def login(self, username="standard_user", password="secret_sauce"):
        self.driver.get("https://www.saucedemo.com/")
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)

    def logout(self):
        self.click(self.menu_button)
        self.click(self.logout_button)
        # confirm logout → wait for username input to be visible
        self.wait_utils.wait_for_visibility(self.username_input)

    # ==== HELPERS ====
    def find(self, by_locator):
        return self.wait_utils.wait_for_visibility(by_locator)

    def click(self, by_locator):
        """Make a click on an element"""
        element = self.wait_utils.wait_for_clickable(by_locator)
        element.click()

    def type(self, by_locator, text):
        """Insert the text into the element"""
        element = self.wait_utils.wait_for_visibility(by_locator)
        element.clear()
        element.send_keys(text)

    def is_visible(self, by_locator):
        """Verify if the element is visible"""
        return self.find(by_locator).is_displayed()

    def find_elements(self, by_locator):
        """
        Return a list of elements found by the locator
        Wait until at least one element is present or timeout occurs
        Uses WaitUtils for consistent waiting logic
        """
        return self.wait_utils.wait_for_elements_present(by_locator)

