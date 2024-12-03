from pages.base_page import BasePage
from pages.locators import LoginPageLocators, BasePageLocators
import time
email = str(time.time()) + "@fakemail.org"
password = "securepassword123"


class LoginPage(BasePage):
    def should_be_login_url(self):
        # Проверяем, что "login" есть в текущем URL
        assert "login" in self.browser.current_url, "Login URL is incorrect"

    def should_be_login_form(self):
        # Проверяем, что форма логина присутствует на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # Проверяем, что форма регистрации присутствует на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def should_be_login_page(self):
        # Метод для проверки, что страница является страницей логина
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def login_user(self, email, password):
        """Авторизация пользователя с заданным email и паролем."""
        email_input = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        email_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()

    def should_be_authorized_user(self):
        """Проверка наличия иконки пользователя, которая указывает на авторизацию."""
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, user is not authorized"

    def register_new_user(self, email, password):
        # Найти и заполнить поле email
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        # Найти и заполнить поле пароля
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1).send_keys(password)
        # Найти и заполнить поле подтверждения пароля
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(password)
        # Нажать кнопку регистрации
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

