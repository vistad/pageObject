# pytest -vs --tb=line --language=en test_product_page.py

import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


@pytest.mark.parametrize('number', ['0', '1', '2', '3', '4', '5', '6',
                                  pytest.param("7", marks=pytest.mark.xfail),
                                  '8', '9'])

#@pytest.mark.parametrize('number', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])   #parametrization adds numbers to the link
def test_guest_can_add_product_to_cart(browser, number):
    url = f'{link}{number}'
    page = ProductPage(browser, url)    # initializes the Page Object, passes an instance of driver and url to the constructor
    page.open()                         # opens the page
    page.click_add2cart_button()        # adds to cart
    page.solve_quiz_and_get_code()      # calculates the formula and inputs the answer
    page.should_be_add2cart_msg()       # checks the message is present
    page.should_be_add2cart_price()     # checks the price is correct



