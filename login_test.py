from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Verify successful login
if "inventory" in driver.current_url:
    print("PASS: Valid login successful")
else:
    print("FAIL: Login unsuccessful")

time.sleep(3)
driver.quit()