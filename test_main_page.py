from selenium.webdriver.common.by import By

from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # создаём объект страницы
    page.open()  # открываем страницу
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")  # заменим позже на метод из Page Object
    login_link.click()

