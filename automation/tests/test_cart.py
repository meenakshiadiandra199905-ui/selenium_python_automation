# Automation tests for Shopping Cart
from automation.pages.login_page import LoginPage
from automation.pages.cart_page import CartPage

def test_add_product_to_cart(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    cart = CartPage(driver)

    login.login("standard_user", "secret_sauce")

    cart.add_product_to_cart()
    cart.open_cart()

    assert "cart" in driver.current_url

