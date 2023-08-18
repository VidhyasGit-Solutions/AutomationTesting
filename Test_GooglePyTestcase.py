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
import re

@pytest.fixture
def browser():
    # Configure Chrome options
    options = Options()
    options.add_experimental_option("detach", True)

    # Create a Chrome browser instance using ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def clean_text(text):
    return re.sub(r"<.*?>", "", text)  # Remove HTML tags

def test_search_movies_in_winnipeg(browser):
    browser.get("https://www.google.com")
    
    search_box = browser.find_element("name", "q")
    search_box.send_keys("movies in Winnipeg")
    search_box.send_keys(Keys.RETURN)
    
    # Use WebDriverWait to wait for the search results to load
    wait = WebDriverWait(browser, 10)
    search_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tF2Cxc")))
    
    assert len(search_results) > 0, "No search results found"
    
   # Asserting specific values from the search results using regular expressions
    expected_values = ["Scotiabank Theatre Winnipeg"]
    
    for value in expected_values:
        clean_expected = clean_text(value)
        found = any(clean_expected.lower() in clean_text(result.get_attribute("innerHTML")).lower() for result in search_results)
        assert found, f"'{value}' not found in search results"

if __name__ == "__main__":
    pytest.main()