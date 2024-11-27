from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # Локатор для ссылки на логин


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  # Локатор для формы логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  # Локатор для формы регистрации
