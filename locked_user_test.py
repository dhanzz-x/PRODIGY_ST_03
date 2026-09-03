from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

# Enter locked-out user credentials
driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Click Login
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Get error message
error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
print("Error message:", error_message)

if "locked out" in error_message.lower():
    print("PASS: Locked-out user correctly rejected")
else:
    print("FAIL: Unexpected error message")

time.sleep(3)
driver.quit()