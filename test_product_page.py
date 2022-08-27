# pytest -vs --tb=line --language=en test_product_page.py
# pytest -vs --tb=line --language=en test_product_page.py::test_guest_cant_see_success_message_after_adding_product_to_basket
# pytest -vs --tb=line --language=en test_product_page.py::test_guest_cant_see_success_message
# pytest -vs --tb=line --language=en test_product_page.py::test_message_disappeared_after_adding_product_to_cart
# pytest -vs --tb=line --language=en test_product_page.py::test_guest_should_see_login_link_on_product_page
# pytest -vs --tb=line --language=en test_product_page.py::test_guest_can_go_to_login_page_from_product_page



import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



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















