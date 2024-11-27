from pages.base_page import BasePage
from pages.locators import LoginPageLocators


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
