import pytest
from config.config import Config
from config.driver import SetUpWebDriver
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def Setup():
    driver = SetUpWebDriver(Config.BROWSER)
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def load_credentials():
    credentials = {
        "username": "carry.workspace@gmail.com",
        "password": "Cfgdf#dfgdfh#)((V*("
    }
    return credentials

@pytest.fixture(scope="function")
def login(Setup,load_credentials):
    driver = Setup
    credentials = load_credentials

    login_page = LoginPage(driver)
    login_page.login(credentials["username"],credentials["password"])

    assert  login_page.is_logged_in()
