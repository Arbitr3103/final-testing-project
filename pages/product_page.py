import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        """Кликает на кнопку добавления в корзину, ожидая её появления"""
        add_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET_BUTTON)
        )
        add_button.click()

    # def solve_quiz_and_get_code(self):
    #     """Решает задачу в алерте, если она появляется"""
    #     try:
    #         alert = self.browser.switch_to.alert
    #         x = alert.text.split(" ")[2]
    #         answer = str(math.log(abs((12 * math.sin(float(x))))))
    #         alert.send_keys(answer)
    #         alert.accept()
    #         try:
    #             alert = self.browser.switch_to.alert
    #             alert_text = alert.text
    #             print(f"Your code: {alert_text}")
    #             alert.accept()
    #         except NoAlertPresentException:
    #             print("No second alert presented")
    #     except NoAlertPresentException:
    #         print("No alert present initially")

    def get_product_name(self):
        """Возвращает название товара со страницы товара"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_basket_message(self):
        """Возвращает сообщение о добавлении товара в корзину"""
        return self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text

    def get_product_price(self):
        """Возвращает цену товара со страницы товара"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_basket_price(self):
        """Возвращает сообщение о стоимости корзины"""
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE).text

    def should_not_be_success_message(self):
        """Проверяет, что сообщение об успехе отсутствует"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_message_disappear(self):
        """Проверяет, что сообщение исчезает через некоторое время"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear"

    def is_not_element_present(self, how, what, timeout=4):
        """Проверяет, что элемент не появляется в течение заданного времени"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """Проверяет, что элемент исчезает в течение заданного времени"""
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((how, what)))
        except:
            return False
        return True

    def should_be_correct_product_in_basket(self):
        """Проверка, что добавленный товар соответствует тому, что в корзине"""
        # Получение названия продукта с продуктовой страницы
        product_name = self.get_product_name()
        print(f"Product name from product page: {product_name}")

        # Получение названия продукта из сообщения корзины
        basket_message = self.get_basket_message()
        print(f"Product name from basket message: {basket_message}")

        # Проверка совпадения названия
        assert product_name == basket_message, f"Expected product name '{product_name}', but got '{basket_message}'"

        # Получение цены продукта с продуктовой страницы
        product_price = self.get_product_price()
        print(f"Product price from product page: {product_price}")

        # Получение цены продукта из сообщения корзины
        basket_price = self.get_basket_price()
        print(f"Product price from basket message: {basket_price}")

        # Проверка совпадения цены
        assert product_price == basket_price, f"Expected basket price '{product_price}', but got '{basket_price}'"
