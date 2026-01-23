# Automation tests for Shopping Cart
import pytest
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from automation.pages.cart_page import CartPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()

def test_add_product_to_cart(driver):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_inventory"))
    ).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_item = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    )

    assert cart_item.is_displayed()

