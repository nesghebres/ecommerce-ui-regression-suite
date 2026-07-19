import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.usefixtures("driver")
def test_add_product(driver):
    """
    Testfall: Produkt hinzufügen und Warenkorb öffnen.
    
    :param driver: Ein instanziiertes WebDriver-Objekt.
    """
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    # Testfall: Produkt hinzufügen
    product_name = "Sauce Labs Backpack"
    inventory.add_product(product_name)

    # Testfall: Warenkorb öffnen und prüfen, ob die Seite korrekt geladen wurde
    inventory.open_cart()
    assert "cart" in driver.current_url

    # Optional: Prüfen, ob das Produkt im Warenkorb vorhanden ist
    # inventory.verify_product_in_cart(product_name)
