import pytest
import selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    """
    Fixture für einen Chrome-Driver.
    
    :return: Ein instanziiertes WebDriver-Objekt.
    """
    options = selenium.webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    service = Service(ChromeDriverManager().install())
    driver = selenium.webdriver.Chrome(service=service, options=options)
    
    yield driver
    driver.quit()
