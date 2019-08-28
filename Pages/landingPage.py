from Outward.Locators.locators import Locators
from selenium.webdriver.common.keys import Keys

class LandingPage():

    def __init__(self, driver):
        self.driver = driver
        self.search_text_box_id = Locators.search_bar
        self.email_campaign_popup = Locators.close_email_campaign_popup
        self.store_locator_button = Locators.store_locator_button

    def close_email_campaign_popup(self):
        self.driver.find_element_by_class_name(self.email_campaign_popup).click()

    def enter_text(self, text):
        self.driver.find_element_by_id(self.search_text_box_id).clear()
        self.driver.find_element_by_id(self.search_text_box_id).click()
        self.driver.find_element_by_id(self.search_text_box_id).send_keys(text)

    def press_enter(self):
        self.driver.find_element_by_id(self.search_text_box_id).send_keys(Keys.RETURN)

    def click_store_locator(self):
        self.driver.find_element_by_xpath(self.store_locator_button).click()