from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.signup_page import SignupPage 
from pages.home_page import HomePage

import re

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    # Вход с тестовыми данными
    login_page.login("1111@yandex.ru", "1111")
    
    # Проверка, что аккаунт вошел 
    expect(page).not_to_have_url("**/login")

def test_user_registration(page: Page):
    signup_page = SignupPage(page)
    signup_page.navigate()
    
    # Регистрация нового пользователя (Email должен быть уникальным)
    import random
    random_id = random.randint(1000, 9999)
    test_email = f"anna_test_{random_id}@example.com"
    
    signup_page.register("Anna", test_email, "Password123!")
    
    # Проверка, что после регистрации перекинуло на логин
    expect(page).not_to_have_url("**/signup")

def test_logout(page: Page):
    # Авторизация
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("1111@yandex.ru", "1111") 
    
    #  Выход
    home_page = HomePage(page)
    home_page.logout()
    
    #  Проверка, что перекинуло на страницу логина
    expect(page).to_have_url(re.compile(r".*/login"))