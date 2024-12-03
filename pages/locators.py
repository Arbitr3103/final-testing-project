from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # Локатор для ссылки на логин
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")  # Локатор для невалидной ссылки
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group > a")  # Локатор для ссылки на корзину
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")  # Локатор для иконки авторизованного пользователя


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  # Форма логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  # Форма регистрации
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")  # Поле для ввода email (логин)
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")  # Поле для ввода пароля (логин)
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")  # Кнопка логина

    # Локаторы для регистрации:
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")  # Поле для ввода email (регистрация)
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")  # Поле для пароля
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")  # Поле для подтверждения пароля
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")  # Кнопка регистрации


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")  # Локатор для элементов в корзине
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")  # Локатор для сообщения "Корзина пуста"


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")  # Кнопка добавления в корзину
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")  # Название продукта
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")  # Цена продукта
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")  # Название товара в корзине
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")  # Цена в сообщении корзины
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")  # Проверить дублирование
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")  # Сообщение об успешном добавлении


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # Локатор для ссылки на логин
