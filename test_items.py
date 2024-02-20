import time
import pytest
from selenium.webdriver.common.by import By


def test_should_be_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    element = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(element) > 0, "No <add_to_basket> button"
