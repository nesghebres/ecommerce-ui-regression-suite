from selenium.webdriver.common.by import By

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

    def customer(self, first, last, zip_code):
        """
        Füllt die Kundeninformationen aus.
        
        :param first: Vorname des Kunden.
        :param last: Nachname des Kunden.
        :param zip_code: Postleitzahl des Kunden.
        """
        self.driver.find_element(*self.FIRSTNAME).send_keys(first)
        self.driver.find_element(*self.LASTNAME).send_keys(last)
        self.driver.find_element(*self.ZIP).send_keys(zip_code)

        self.driver.find_element(*self.CONTINUE).click()

    def finish(self):
        """
        Klickt auf den "Finish"-Button.
        """
        self.driver.find_element(*self.FINISH).click()

    def is_success(self):
        """
        Überprüft, ob die Bestellung erfolgreich abgeschlossen wurde.
        
        :return: True, wenn die Bestellung erfolgreich abgeschlossen wurde, False sonst.
        """
        return self.driver.find_element(*self.COMPLETE).text != ""
