from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class MainPage(BasePage):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # локатор для логин-ссылки

    def should_be_login_link(self):
        assert self.is_element_present(*self.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*self.LOGIN_LINK)  # используем локатор
        login_link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
            return True
        except NoSuchElementException:
            return False
