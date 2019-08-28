import time
import datetime
import unittest
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.landingPage import LandingPage
from Pages.storeLocatorPage import StoreLocatorPage
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

    def test_1_verify_valid_selection_returns_expected_result(self):
        driver = self.driver
        driver.get('https://www.westelm.com')

        test_verify_valid_selection_returns_expected_result = LandingPage(driver)
        test_verify_valid_selection_returns_expected_result.close_email_campaign_popup()
        test_verify_valid_selection_returns_expected_result.click_store_locator()

        test_verify_valid_selection_returns_expected_result = StoreLocatorPage(driver)
        test_verify_valid_selection_returns_expected_result.click_view_all_stores_button()
        test_verify_valid_selection_returns_expected_result.select_state("Arizona")

        #Verify that state "Arizona" has "2" expected store results
        test_verify_valid_selection_returns_expected_result.verify_store_count_accurate('Arizona','2')

    @classmethod
    def tearDownClass(cls):
        cls.driver.delete_all_cookies()
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')

