from Locators.locators import Locators

class ProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.image_url = Locators.product_image_url
        self.page_url = Locators.product_image_url
        self.item_image = Locators.item_image

    def get_page_url(self):
        return self.driver.current_url

    def get_image_url(self):
        return self.driver.find_element_by_id("hero").get_attribute("src")

    def get_image_title(self):
        return self.driver.current_url.get_attribute("alt")

