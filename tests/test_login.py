import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")
def test_successful_login(driver):
    """
    Testfall für einen erfolgreichen Login.
    
    :param driver: Ein instanziiertes WebDriver-Objekt.
    """
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url


@pytest.mark.usefixtures("driver")
def test_invalid_login(driver):
    """
    Testfall für einen fehlgeschlagenen Login.
    
    :param driver: Ein instanziiertes WebDriver-Objekt.
    """
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "wrongpassword")
    assert "Username and password do not match" in login.error_message()

