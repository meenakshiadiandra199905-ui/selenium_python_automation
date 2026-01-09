# Automation tests for Shopping Cart
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_open_browser():
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get("https://www.google.com")
  time.sleep(5)
  driver.quit()

test_open_browser()
