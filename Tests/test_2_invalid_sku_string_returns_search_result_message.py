import time
import datetime
import unittest
import sys
import os
from selenium import webdriver
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.landingPage import LandingPage
from Pages.productPage import ProductPage
from Pages.searchResultPage import SearchResultPage
import HtmlTestRunner

class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver_path = os.getenv('CHROME_DRIVER_PATH', 'C:/Users/ASUS Zenbook/Desktop/ChromeDriver/chromedriver.exe')
        assert driver_path, 'Environment variable not set for Chromedriver path, please set it'
        cls.driver = webdriver.Chrome(driver_path)
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_1_invalid_sku_search_functionality(self):
        driver = self.driver
        driver.get('https://www.westelm.com')

        test_invalid_sku_search_functionality = LandingPage(driver)
        test_invalid_sku_search_functionality.close_email_campaign_popup()
        test_invalid_sku_search_functionality.enter_text('123456')
        test_invalid_sku_search_functionality.press_enter()

    def test_2_invalid_search_query_message_displayed(self):
        driver = self.driver
        test_invalid_search_query_message_displayed = SearchResultPage(driver)
        test_invalid_search_query_message_displayed.verify_element_present()

    @classmethod
    def tearDownClass(cls):
        cls.driver.delete_all_cookies()
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')

