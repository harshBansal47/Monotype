from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def login(self, username, password):
        """Perform login using the provided username and password."""
        self.wait.until(EC.element_to_be_clickable((By.ID, "login_homepage"))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(username)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='action' and @value='default']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'][contains(.,'Continue')]"))).click()

    def is_logged_in(self):
        """Check if the user is successfully logged in."""
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//a[@data-qa-id='userdropdown']"))).is_displayed()

