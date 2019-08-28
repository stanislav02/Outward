from Outward.Locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException

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
            print(Exception)
