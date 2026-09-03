from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

# Enter username only
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Leave password empty
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
print("Error message:", error_message)

if "Password is required" in error_message:
    print("PASS: Empty password correctly rejected")
else:
    print("FAIL: Unexpected error message")

time.sleep(3)
driver.quit()