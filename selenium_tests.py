from selenium import webdriver
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open AWS homepage
driver.get("https://aws.amazon.com/")

# Wait 5 seconds
time.sleep(5)

# Close the browser
driver.quit()