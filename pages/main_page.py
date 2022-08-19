# pytest -v --tb=line --language=en test_main_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage): # imports * from base_page and describes methods applicable on the main page
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # * means a tuple
        login_link.click() 

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
