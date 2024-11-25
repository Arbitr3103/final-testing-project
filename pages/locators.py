from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")  # Обновленный селектор


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  # селектор для формы логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  # селектор для формы регистрации
