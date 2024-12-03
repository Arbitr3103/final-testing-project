import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time


@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.xfail(reason="Known issue: success message does not disappear")),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    # page.solve_quiz_and_get_code()
    product_name = page.get_product_name()
    basket_message = page.get_basket_message()
    assert product_name == basket_message, "Product name in basket does not match the added product"
    product_price = page.get_product_price()
    basket_price = page.get_basket_price()
    assert product_price == basket_price, "Basket price does not match product price"


@pytest.mark.xfail(reason="Known issue: success message does not disappear")
def test_message_disappeared_after_adding_product(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_message_disappear()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Success message should not be present but appears due to known issue")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()


@pytest.mark.user
class TestUserActionsOnProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        self.login_page.open()

    @pytest.mark.new_user
    def test_register_new_user(self, browser):
        # Генерируем случайный email для регистрации
        email = str(time.time()) + "@fakemail.org"
        password = "securepassword123"
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()
        print(f"New user registered: {email}")

    @pytest.mark.existing_user
    def test_registered_user_can_login(self, browser):
        # Данные заранее зарегистрированного пользователя
        email = "existing_user@example.com"
        password = "securepassword123"
        self.login_page.login_user(email, password)
        self.login_page.should_be_authorized_user()
