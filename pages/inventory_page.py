from selenium.webdriver.common.by import By


class InventoryPage:

    CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_product(self, product_name):
        product_button = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        )
        self.driver.find_element(*product_button).click()

    def open_cart(self):
        self.driver.find_element(*self.CART).click()
