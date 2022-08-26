from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-default[href$='/basket/']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")    # locator of the product name
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")  # locator of the product price
    ADD2CART_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")    # locator of the button
    ADD2CART_MSG = (By.CSS_SELECTOR, "#messages strong")
    ADD2CART_PRICE = (By.CSS_SELECTOR, "div.alertinner>p strong")

class BasketPageLocators:
    CART_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    CART_ITEMS = (By.CSS_SELECTOR, ".basket-items")



