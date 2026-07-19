from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    """
    Klasse für die Checkout-Seite.
    
    :param driver: Ein WebDriver-Objekt.
    """

    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")

    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")

    COMPLETE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        """
        Initialisiert die Checkout-Seite.
        
        :param driver: Ein WebDriver-Objekt.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def customer(self, first, last, zip_code):
        """
        Füllt die Kundeninformationen aus.
        
        :param first: Vorname des Kunden.
        :param last: Nachname des Kunden.
        :param zip_code: Postleitzahl des Kunden.
        """
        self.wait.until(EC.visibility_of_element_located(self.FIRSTNAME)).send_keys(first)

        self.driver.find_element(*self.LASTNAME).send_keys(last)
        self.driver.find_element(*self.ZIP).send_keys(zip_code)

        self.wait.until(EC.element_to_be_clickable(self.CONTINUE)).click()

    def finish(self):
        """
        Schließt die Bestellung ab.
        """
        self.wait.until(EC.element_to_be_clickable(self.FINISH)).click()

    def success(self):
        
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE)).text
