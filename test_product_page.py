# import pytest
# from pages.product_page import ProductPage
#
#
# @pytest.mark.parametrize('link', [
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                  marks=pytest.mark.xfail(reason="Known issue: success message does not disappear")),
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
# ])
# def test_guest_can_add_product_to_basket(browser, link):
#     # Тест добавления товара в корзину
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     product_name = page.get_product_name()
#     basket_message = page.get_basket_message()
#     assert product_name == basket_message, "Product name in basket does not match the added product"
#     product_price = page.get_product_price()
#     basket_price = page.get_basket_price()
#     assert product_price == basket_price, "Basket price does not match product price"
#
#
# @pytest.mark.xfail(reason="Known issue: success message does not disappear")
# def test_message_disappears_after_adding_product(browser):
#     # Тест на исчезновение сообщения
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()  # Добавляем товар в корзину
#     page.should_message_disappear()  # Проверяем, что сообщение исчезает
#
#
# def test_guest_cant_see_success_message(browser):
#     # Тест на отсутствие сообщения до добавления товара
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()  # Проверяем, что сообщение отсутствует
#
#
# @pytest.mark.xfail(reason="Success message should not be present but appears due to known issue")
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()  # Добавляем товар в корзину
#     page.should_not_be_success_message()  # Проверяем, что сообщение отсутствует


# import pytest
# from pages.product_page import ProductPage
#
#
# @pytest.mark.xfail(reason="Success message should not be present but appears due to known issue")
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()  # Добавляем товар в корзину
#     page.should_not_be_success_message()  # Проверяем, что сообщение отсутствует
#
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()  # Проверяем, что сообщение отсутствует
#
#
# @pytest.mark.xfail(reason="Known issue: success message does not disappear")
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()  # Добавляем товар в корзину
#     page.should_message_disappear()  # Проверяем, что сообщение исчезает


import pytest
from pages.product_page import ProductPage


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
    # Здесь можно добавить проверку, что открылась страница логина
