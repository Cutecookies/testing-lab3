from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_add_to_cart(page: Page):
    # Авторизация 
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("1111@yandex.ru", "1111") 
    
    # Переход на главную страницу
    home_page = HomePage(page)
    home_page.navigate()
    
    # Ожидание загрузки товаров
    expect(home_page.product_cards.first).to_be_visible()
    
    # Добавление в корзину
    home_page.add_first_product_to_cart()
    
    # Проверка появления уведомления об успехе
    expect(page.locator('.Toastify__toast')).to_be_visible()