import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from pages.ChromePages.LoginPage import LoginPage
from pages.ChromePages.HomePage import HomePage

from tests.ChromeTests.BaseTest import BaseTest


class HomeTest(BaseTest):

    @classmethod
    def setUp(cls):
        super().setUp()
        cls.homePage = HomePage(cls.driver)

    def test_addItemToCart(self):

        self.homePage.load()
        self.homePage.addItemToCart()

        self.assertTrue(self.homePage.isItemInCart(), "The item was not added to the cart")
