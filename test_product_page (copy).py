"""
pytest -vs --tb=line --language=en test_product_page.py
pytest -vs --tb=line --language=en test_product_page.py::test_guest_cant_see_success_message_after_adding_product_to_basket
pytest -vs --tb=line --language=en test_product_page.py::test_guest_cant_see_success_message
pytest -vs --tb=line --language=en test_product_page.py::test_message_disappeared_after_adding_product_to_cart
pytest -vs --tb=line --language=en test_product_page.py::test_guest_should_see_login_link_on_product_page
pytest -vs --tb=line --language=en test_product_page.py::test_guest_can_go_to_login_page_from_product_page
pytest -vs --tb=line --language=en test_product_page.py::test_guest_cant_see_product_in_basket_opened_from_product_page
pytest -vs --tb=line --language=en test_product_page.py::test_user_can_add_product_to_basket
"""


import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from selenium import webdriver
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
import time


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
#        page.should_not_be_message_about_adding()
        page.should_not_be_success_message()


    @pytest.fixture(scope="function", autouse=True)
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
#        page.click_add_to_cart_button()
#        page.should_be_message_about_adding()
#        page.should_be_total_price()
        page.register_new_user()
        self.browser.implicitly_wait(3)
        page.should_be_authorized_user()
        page.click_add2cart_button()
        page.should_be_add2cart_msg()
        page.should_be_add2cart_price()
        print(new_email)
        print(new_password)



"""

    def test_user_cant_see_success_message(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_cart(browser, number):
        page = LoginPage(browser, link)
        page.open()
        page.click_add2cart_button()
        page.should_be_add2cart_msg()
        page.should_be_add2cart_price()


"""




"""
@pytest.mark.parametrize('number', ['0', '1', '2', '3', '4', '5', '6',
                                  pytest.param("7", marks=pytest.mark.xfail),
                                  '8', '9'])   #parametrization adds numbers to the link
def test_guest_can_add_product_to_cart(browser, number):
    link_param = f'{link}?promo=offer{number}'
    page = ProductPage(browser, link_param)    # initializes the Page Object, passes an instance of driver and link_param to the constructor
    page.open()                         # opens the page
    page.click_add2cart_button()        # adds to cart
    page.solve_quiz_and_get_code()      # calculates the formula and inputs the answer
    page.should_be_add2cart_msg()       # checks the message is present
    page.should_be_add2cart_price()     # checks the price is correct

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add2cart_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add2cart_button()
    page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasePage(browser, link)
    page.open()                     # Гость открывает страницу товара
    page.go_to_basket_page()        # Переходит в корзину по кнопке в шапке 
    basket_page = BasketPage(browser, browser.current_url)  # change focus to the cart page
    basket_page.should_be_cart_is_empty()   # cart should be empty
    basket_page.should_be_text_cart_is_empty()    # text cart is empty exists

"""











