from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Create a Chrome browser instance using ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.demoblaze.com")
driver.maximize_window()

# Click on the "Sign up" button
signup_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign up')]")
signup_button.click()

# Switch the focus to the pop-up window
main_window = driver.current_window_handle
popup_window = driver.window_handles[0]  # Index 0 is usually the main window
driver.switch_to.window(popup_window)

wait = WebDriverWait(driver, 20)
# Fill in the registration form
# Wait for the element to be clickable (visible and enabled)
username_field = wait.until(EC.element_to_be_clickable((By.ID, "sign-username")))
username_field.send_keys("testuser")

password_field = driver.find_element(By.ID, "sign-password")
password_field.send_keys("testpassword")

signup_button = driver.find_element(By.XPATH, "//button[text()='Sign up']")
signup_button.click()

main_window = driver.current_window_handle
popup_window = driver.window_handles[0]  # Index 0 is usually the main window
driver.switch_to.window(popup_window)

wait = WebDriverWait(driver, 20)

# Wait for the alert to appear
wait = WebDriverWait(driver, 10)
alert = wait.until(EC.alert_is_present())

# Retrieve the error message from the alert
error_message = alert.text
print("Error Message:", error_message)

# Click the "OK" button in the alert
alert.accept()

driver.close()

driver.quit()