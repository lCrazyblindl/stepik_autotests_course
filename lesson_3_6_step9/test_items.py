import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_buy_button_presence(browser):
    browser.implicitly_wait(60)
    browser.get(' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    buy_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    time.sleep(5)
    assert buy_button
