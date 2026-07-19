from selenium.webdriver.common.by import By


class LoginPage:
    """
    Klasse für die Login-Seite.
    
    :param driver: Ein WebDriver-Objekt.
    """

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        """
        Konstruktor für die Login-Seite.
        
        :param driver: Ein WebDriver-Objekt.
        """
        self.driver = driver

    def open(self):
        """
        Öffnet die Login-Seite im Browser.
        """
        self.driver.get(self.URL)

    def login(self, username, password):
        """
        Loggt den Benutzer ein.
        
        :param username: Der Benutzernamen.
        :param password: Das Passwort.
        """
        self._clear_and_fill_input(self.USERNAME_INPUT, username)
        self._clear_and_fill_input(self.PASSWORD_INPUT, password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def error_message(self):
        """
        Gibt den Fehlermeldungstext zurück.
        
        :return: Der Fehlermeldungstext.
        """
        return self.driver.find_element(*self.ERROR_MESSAGE).text.replace("\u2018", "").replace("\u2019", "").strip()

    
    def _clear_and_fill_input(self, locator, value):
        """
        Leert einen Input-Feld und füllt es mit einem Wert.
        
        :param locator: Der Locator für das Input-Feld.
        :param value: Der Wert für das Input-Feld.
        """
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)


