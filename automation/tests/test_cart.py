# Automation tests for Shopping Cart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)

cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
assert "Sauce Labs Backpack" in cart_item
print("Product successfully added to cart")

driver.quit()
