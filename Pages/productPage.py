from Outward.Locators.locators import Locators

class ProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.image_url = Locators.product_image_url
        self.page_url = Locators.product_image_url
        self.item_image = Locators.item_image

    def get_page_url(self, url):
        try:
            assert url == self.driver.current_url
            print(f'{url} matches {self.driver.current_url}')
        except AssertionError as error:
            print(error)
            print(f'{url} does not match {self.driver.current_url}')

    def get_image_url(self, image_url):
        try:
            assert image_url == self.driver.find_element_by_id("hero").get_attribute("src")
            print(f'{image_url} matches {self.driver.find_element_by_id("hero").get_attribute("src")}')
        except AssertionError as error:
            print(error)
            print(f'{image_url} does not match {self.driver.find_element_by_id("hero").get_attribute("src")}')

    def get_image_title(self, image_title):
        try:
            assert image_title == self.driver.current_url.get_attribute("alt")
            print(f'{image_title} matches {driver.current_url.get_attribute("alt")}')
        except AssertionError as error:
            print(error)
            print(f'{image_title} does not match {driver.current_url.get_attribute("alt")}')

