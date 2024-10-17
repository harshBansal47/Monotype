import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("login")
def test_login(login):
    assert login.is_logged_in()

