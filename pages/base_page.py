# pytest -v -s --language=en base_page.py

import pytest
from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)


