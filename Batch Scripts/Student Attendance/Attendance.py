#Requires Selenium and Firefox Webdriver (Geckodriver) installed in Enviornmental Path.

from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

# Retrieve command line arguments as names list
names = sys.argv[1:]

# Set up Firefox driver
driver = webdriver.Firefox()

# Navigate to webpage
driver.get("https://ahmadac.github.io/")

# Find input box element and input variable value
input_box = driver.find_element(By.ID, "inputText2")
input_box.send_keys(names)  # Join names list into a comma-separated string

# Find and click submit button
button = driver.find_element(By.ID, "submitBtn2")
button.click()

# Wait for user input before closing the browser
input('Press any key to exit...')

# Quit the driver to close the browser
driver.quit()
