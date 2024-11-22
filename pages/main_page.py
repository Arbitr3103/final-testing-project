from .base_page import BasePage

from selenium.webdriver.common.by import By


class MainPage(BasePage):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # локатор для логин-ссылки

    def go_to_login_page(self):
        login_link = self.browser.find_element(*self.LOGIN_LINK)  # используем локатор
        login_link.click()
