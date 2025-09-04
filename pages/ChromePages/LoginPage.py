from selenium.webdriver.common.by import By
from pages.ChromePages.BasePage import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # ==== LOCATORS ====
        self.page_title = (By.CLASS_NAME, "app_logo")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    # ==== METHODS ====
    def load(self):
        """Load the login page"""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username=None, password=None):
        """
        Perform login with given credentials
        If no credentials provided, use default from BasePage
        """
        if username is None or password is None:
            super().login()
        else:
            self.type(self.username_input, username)
            self.type(self.password_input, password)
            self.click(self.login_button)

    # ==== HELPERS ====
    def getErrorMessage(self):
        """Return the text of the error message displayed on login failure"""
        return self.find(self.error_message).text

    def getTitleText(self):
        """Return the text of the page title"""
        return self.find(self.page_title).text
