import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    global driver
    driver = Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(30)
    print("Launching the chrome browser")
    return driver;