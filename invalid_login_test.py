from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

# Enter invalid username and password
driver.find_element(By.ID, "user-name").send_keys("wrong_user")
driver.find_element(By.ID, "password").send_keys("wrong_password")

# Click Login
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Check for error message
error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text

if "Username and password do not match" in error_message:
    print("PASS: Invalid login correctly rejected")
else:
    print("FAIL: Unexpected error message")

time.sleep(3)
driver.quit()