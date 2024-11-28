from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # Локатор для ссылки на логин
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")  # Локатор для невалидной ссылки
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group > a")  # Локатор для ссылки на корзину


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")  # Локатор для элементов в корзине
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")  # Локатор для сообщения "Корзина пуста"


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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")  # Пример локатора для сообщения
