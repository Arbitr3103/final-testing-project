from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # Локатор для ссылки на логин


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  # Локатор для формы логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  # Локатор для формы регистрации


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")
