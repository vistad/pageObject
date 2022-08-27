# imports * from base_page and describes objects and methods applicable on main page

from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    pass

"""
alternative class definiton:
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
"""

