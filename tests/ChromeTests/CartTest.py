import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.ChromePages.HomePage import HomePage
from pages.ChromePages.CartPage import CartPage
from pages.ChromePages.LoginPage import LoginPage
from tests.ChromeTests.BaseTest import BaseTest


class CartTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_cartIsEmptyInitially(self):
        loginPage = LoginPage(self.driver)
        loginPage.load()
        loginPage.login("standard_user", "secret_sauce")

        cartPage = CartPage(self.driver)
        self.assertTrue(cartPage.isCartEmpty(), "The Cart is not empty")

    def test_addItemAndCheckCart(self):
        loginPage = LoginPage(self.driver)
        loginPage.load()
        loginPage.login("standard_user", "secret_sauce")

        homePage = HomePage(self.driver)
        homePage.addItemToCart()
        homePage.goToCart()

        cartPage = CartPage(self.driver)
        self.assertFalse(cartPage.isCartEmpty(), "The Cart is still empty after adding an item")
