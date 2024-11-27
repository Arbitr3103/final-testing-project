import math
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_product_name(self):
        # Возвращает название товара со страницы товара
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_basket_message(self):
        # Возвращает сообщение о добавлении товара в корзину
        return self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text

    def get_product_price(self):
        # Возвращает цену товара со страницы товара
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_basket_price(self):
        # Возвращает сообщение о стоимости корзины
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE).text
