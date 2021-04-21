import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def is_element_present(browser, by, text):
    try:
        return WebDriverWait(browser, 12).until(EC.presence_of_element_located((by, text)))
    except TimeoutException:
        return False


def test_add_to_cart_present(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    assert is_element_present(browser, By.CSS_SELECTOR, ".btn-add-to-basket"), "Button for adding item to the cart was not found."