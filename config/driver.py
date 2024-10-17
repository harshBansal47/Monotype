from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config.config import Config


def SetUpWebDriver(profile):
    """Set up WebDriver based on the provided browser profile (chrome, firefox, edge) with options."""

    # Dictionary to hold the browser setup logic with headless mode
    if profile == "chrome":
        options = ChromeOptions()
        if Config.HEADLESS:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")  # For compatibility with headless mode
        options.add_argument("--start-maximized")  # Optional: Start maximized
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif profile == "firefox":
        options = FirefoxOptions()
        if Config.HEADLESS:
            options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    elif profile == "edge":
        options = webdriver.EdgeOptions()  # Edge uses its own options class
        if Config.HEADLESS:
            options.add_argument("--headless")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    else:
        raise ValueError(f"Unsupported browser profile: {profile}")

    driver.maximize_window()  # Optional: Start browser maximized if not headless
    return driver
