# pytest -vs --tb=line --language=en test_main_page.py

#from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
link = "http://selenium1py.pythonanywhere.com/"

# 1st way
def test_guest_can_go_to_login_page(browser):
    page = BasePage(browser, link)   # initialize the Page Object, pass an instance of driver and url to the constructor
    page.open()                      # open the page
    page.go_to_login_page()          # use the page method - go to the login page
    login_page = LoginPage(browser, browser.current_url) # in the 2nd way this is moved to the MainPage class
    login_page.should_be_login_page()                    # check the current url is the login page

# 2nd way
"""
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()
"""

def test_guest_should_see_login_link(browser):
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()























