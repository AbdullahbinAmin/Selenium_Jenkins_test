from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile

options = Options()
options.add_argument("--headless")  # Run in headless mode (no GUI)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Create a unique user data directory
user_data_dir = tempfile.mkdtemp()
options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=options)

# Your test logic here
driver.get("https://example.com")
print(driver.title)

driver.quit()
