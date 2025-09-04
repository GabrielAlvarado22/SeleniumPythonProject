from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.ChromePages.BasePage import BasePage


class CartPage(BasePage):
    #==== LOCATORS ====
    cartItem = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ==== METHODS ====
    def isCartEmpty(self):
        """Return True if the cart is empty, False if it has items"""
        items = self.find_elements(self.cartItem, timeout=1)
        return len(items) == 0
