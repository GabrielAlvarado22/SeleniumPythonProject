from selenium.webdriver.common.by import By
from pages.ChromePages.BasePage import BasePage

class HomePage(BasePage):
    # ==== LOCATORS ====
    cart_icon = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
    add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        super().__init__(driver)

    # ==== METHODS ====
    def load(self):
        """Load the home page"""
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def addItemToCart(self):
        """Click on the 'Add to Cart' button for the backpack"""
        self.click(self.add_to_cart_button)

    def isItemInCart(self):
        """
        Check if the cart badge is present, indicating at least
        one item has been added to the cart
        """
        return len(self.driver.find_elements(*self.cart_badge)) > 0

    def goToCart(self):
        """Navigate to the cart page"""
        self.click(self.cart_icon)
