from pages.ChromePages.LoginPage import LoginPage
from tests.ChromeTests.BaseTest import BaseTest

class TestLogin(BaseTest):

    def test_login_success(self):
        login_page = LoginPage(self.driver)
        title = login_page.getTitleText()
        assert title == "Swag Labs"

    def test_login_invalid(self):
        login_page = LoginPage(self.driver)
        login_page.logout()
        login_page.login("locked_out_user", "secret_sauce")
        error_msg = login_page.getErrorMessage()
        assert "locked out" in error_msg
