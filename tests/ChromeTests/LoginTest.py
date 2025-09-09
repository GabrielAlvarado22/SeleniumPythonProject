from tests.ChromeTests.BaseTest import BaseTest
from utils.user_loader import load_users

class TestLogin(BaseTest):

    def setUp(self):
        # Load user credentials for login tests
        self.users = load_users()

    def test_loginSuccess(self):
        # Verify that a valid user can log in successfully
        title = self.login_page.getTitleText()
        assert title == "Swag Labs"

    def test_loginInvalid(self):
        # Verify that a locked user cannot log in and shows an error
        self.login_page.logout()
        locked_user = self.users["locked_user"]
        self.login_page.login(locked_user["username"], locked_user["password"])
        error_msg = self.login_page.getErrorMessage()
        assert "locked out" in error_msg
