from Outward.Locators.locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import datetime

now = f'{datetime.datetime.now():%Y-%m-%d}'

class StoreLocatorPage():

    def __init__(self, driver):
        self.driver = driver
        self.state_dropdown = Locators.store_locator_dropdown
        self.view_all_stores_button = Locators.view_all_stores_button

    def click_view_all_stores_button(self):
        self.driver.find_element_by_xpath(self.view_all_stores_button).click()

    def select_state(self,state):
        dropdown_element = self.driver.find_element_by_css_selector(Locators.store_locator_dropdown)

        wait_for_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, Locators.store_locator_dropdown))
        )
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(state)

    def verify_store_count_accurate(self, state, expected_store_count):
        if expected_store_count == 1:
            store_noun = 'store'
        store_noun = 'stores'
        try:
            assert self.driver.find_element_by_id(Locators.store_count).text == f'We have {expected_store_count} {store_noun} in {state} :'

        except AssertionError as Exception:
            if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Reports', 'Screenshots')):
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Reports', 'Screenshots'))
            print(Exception)
            print('Capturing screenshot')
            self.driver.save_screenshot(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Reports', 'Screenshots',
                             f'store_locator_test_failure_screenshot{now}.png'))
