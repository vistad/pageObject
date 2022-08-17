# pytest -v --tb=line --language=en test_main_page.py

import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
"""
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)               
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
"""
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # initialize the Page Object, pass an instance of driver and url to the constructor
    page.open()                      # open the page
    page.go_to_login_page()          # use the page method - go to the login page
