from Outward.Locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException
import datetime
import os

now = f'{datetime.datetime.now():%Y-%m-%d}'

class SearchResultPage():

    def __init__(self, driver):
        self.driver = driver
        self.message_present = Locators.unrecognized_query_message
        self.page_url = Locators.invalid_search_result_page_url

    def get_page_url(self):
        return self.driver.current_url

    def verify_element_present(self):
        try:
            self.driver.find_element_by_xpath(Locators.unrecognized_query_message)
        except NoSuchElementException as Exception:
            if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),'Reports', 'Screenshots')):
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'Reports', 'Screenshots'))
            print(Exception)
            print('Capturing screenshot')
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.abspath(__file__)),'Reports', 'Screenshots', f'product_search_test_failure_screenshot{now}.png'))
