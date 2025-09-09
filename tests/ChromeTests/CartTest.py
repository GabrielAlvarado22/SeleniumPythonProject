import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.ChromePages.HomePage import HomePage
from pages.ChromePages.CartPage import CartPage
from pages.ChromePages.LoginPage import LoginPage
from tests.ChromeTests.BaseTest import BaseTest


class CartTest(BaseTest):

    def setUp(self):
        self.homePage = HomePage(self.driver)
        self.cartPage = CartPage(self.driver)

    def test_cartIsEmptyInitially(self):
        self.assertTrue(self.cartPage.isCartEmpty(), "The Cart is not empty")

    def test_addItemAndCheckCart(self):
        self.homePage.addItemToCart()
        self.homePage.goToCart()
        self.assertFalse(self.cartPage.isCartEmpty(), "The Cart is still empty after adding an item")
