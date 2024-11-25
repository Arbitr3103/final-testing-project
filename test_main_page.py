from pages.login_page import LoginPage


def test_guest_can_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)  # Инициализируем LoginPage
    page.open()                      # Открываем страницу логина
    page.should_be_login_url()       # Проверяем, что URL корректный
    page.should_be_login_form()      # Проверяем наличие формы логина
    page.should_be_register_form()   # Проверяем наличие формы регистрации
