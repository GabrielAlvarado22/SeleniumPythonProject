from pages.ChromePages.LoginPage import LoginPage
from tests.ChromeTests.BaseTest import BaseTest
from utils.user_loader import load_users

class TestLogin(BaseTest):

    def setUp(self):
        self.users = load_users()

    def test_loginSuccess(self):
        title = self.login_page.getTitleText()
        assert title == "Swag Labs"

    def test_loginInvalid(self):
        self.login_page.logout()
        locked_user = self.users["locked_user"]
        self.login_page.login(locked_user["username"], locked_user["password"])
        error_msg = self.login_page.getErrorMessage()
        assert "locked out" in error_msg
