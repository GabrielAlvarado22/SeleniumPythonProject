from pages.ChromePages.HomePage import HomePage
from pages.ChromePages.CartPage import CartPage
from tests.ChromeTests.BaseTest import BaseTest


class CartTest(BaseTest):

    def setUp(self):
        # Prepare page objects for the tests
        self.homePage = HomePage(self.driver)
        self.cartPage = CartPage(self.driver)

    def test_cartIsEmptyInitially(self):
        # Check that the cart is empty when first opened
        self.assertTrue(self.cartPage.isCartEmpty(), "The Cart is not empty")

    def test_addItemAndCheckCart(self):
        # Add an item to the cart and verify it appears
        self.homePage.addItemToCart()
        self.homePage.goToCart()
        self.assertFalse(self.cartPage.isCartEmpty(), "The Cart is still empty after adding an item")
