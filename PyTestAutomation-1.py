import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    # Configure Chrome options
    options = Options()
    options.add_experimental_option("detach", True)

    # Create a Chrome browser instance using ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_successful_login(browser):
    # Open the login page
    browser.get("https://www.demoblaze.com")
    browser.maximize_window()

    # Click on the "Sign up" button
    signup_button = browser.find_element(By.XPATH, "//a[contains(text(), 'Home')]")
    signup_button.click()

    # Wait for the welcome message containing "PRODUCT STORE" to be present
    welcome_message_locator = (By.XPATH, "//div[contains(text(), 'PRODUCT STORE')]")