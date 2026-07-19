from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_checkout(driver):
    """
    Testfall für den vollständigen Checkout-Prozess.
    
    :param driver: Ein instanziiertes WebDriver-Objekt.
    """
    # Login-Seite öffnen und anmelden
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    # Inventar-Seite besuchen und Backpack hinzufügen
    inventory = InventoryPage(driver)
    inventory.add_product("Sauce Labs Backpack")
    inventory.open_cart()

    # Warenkorb-Seite besuchen und Checkout durchführen
    cart = CartPage(driver)
    cart.checkout()

    # Checkout-Seite besuchen und Bestellung abschließen
    checkout = CheckoutPage(driver)
    checkout.customer("Max", "Mustermann", "60311")
    checkout.finish()

    # Prüfen, ob die Bestellung erfolgreich abgeschlossen wurde
    assert checkout.success() == "Thank you for your order!"
