import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from pages.ChromePages.LoginPage import LoginPage
from pages.ChromePages.HomePage import HomePage
from webdriver_manager.chrome import ChromeDriverManager

from tests.ChromeTests.BaseTest import BaseTest


class HomeTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.wait = WebDriverWait(self.driver, 10)

    def test_addItemToCart(self):

        homePage = HomePage(self.driver)
        homePage.load()
        homePage.addItemToCart()

        self.assertTrue(homePage.isItemInCart(), "The item was not added to the cart")
