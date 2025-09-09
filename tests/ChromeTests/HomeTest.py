from pages.ChromePages.HomePage import HomePage
from tests.ChromeTests.BaseTest import BaseTest

class HomeTest(BaseTest):

    def setUp(self):
        # Initialize the HomePage object for use in tests
        super().setUp()
        self.homePage = HomePage(self.driver)

    def test_addItemToCart(self):
        # Verify that an item can be added to the cart from the home page
        self.homePage.load()
        self.homePage.addItemToCart()
        self.assertTrue(self.homePage.isItemInCart(), "The item was not added to the cart")
