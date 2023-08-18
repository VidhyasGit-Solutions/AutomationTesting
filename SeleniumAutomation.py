from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "path/to/chrome/exe"  # Optional, if you want to specify Chrome's path
options.add_argument("--start-maximized")       # Optional, maximize the browser window

# Initialize the web driver (here, using Chrome)
driver = webdriver.Chrome(options=options, executable_path='path/to/chromedriver')

# Navigate to the web application
url = 'http://vidha80.pythonanywhere.com/login'  # Replace with the URL of your web application
driver.get(url)

# Perform actions on the web application
element = driver.find_element_by_id('username')
element.send_keys('Vidhya')

element = driver.find_element_by_id('password')
element.send_keys('Canada@2023')

element = driver.find_element_by_id('login_button')
element.click()

# Perform assertions to validate the results
assert "Welcome" in driver.title  # Assuming the title contains "Welcome" after successful login

# Close the web driver
driver.quit()