import unittest
import sys
import os
from selenium import webdriver
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Outward.Pages.productPage import ProductPage
from Outward.Pages.landingPage import LandingPage
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

    def test_1_valid_sku_search_functionality(self):
        driver = self.driver
        driver.get('https://www.westelm.com')

        test_search_functionality = LandingPage(driver)
        test_search_functionality.close_email_campaign_popup()
        test_search_functionality.enter_text('2613243')
        test_search_functionality.press_enter()

    def test_2_sku_search_returned_expected_url(self):
        driver = self.driver
        test_sku_search_returned_expected_url = ProductPage(driver)
        assert test_sku_search_returned_expected_url.page_url == 'https://www.westelm.com/products/build-your-own-andes-sectional-extra-deep-h2517/?words=2613243&pkey=k2613243&sku=2613243'

    def test_3_correct_image_url_returned(self):
        driver = self.driver
        test_correct_image_url_returned = ProductPage(driver)
        assert test_correct_image_url_returned.image_url == 'https://www.westelm.com/weimgs/ab/images/wcm/products/201932/0002/img28c.jpg'

    @classmethod
    def tearDownClass(cls):
        cls.driver.delete_all_cookies()
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')

if __name__ == '__main__':
    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),'Reports')):
        os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'Reports'))
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=os.path.join(os.path.dirname(os.path.abspath(__file__)),'Reports')))