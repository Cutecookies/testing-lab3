from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_place_order(page: Page):
    # Авторизация
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("1111@yandex.ru", "1111") 

    # Ожидание успешного входа 
    expect(page.get_by_role("button", name="Logout")).to_be_visible(timeout=10000)

    # Добавление товара в корзину
    home_page = HomePage(page)
    home_page.navigate()

    # Ожидание загрузки товаров (появления первой кнопки Add Cart)
    expect(page.get_by_role("button", name="Add Cart").first).to_be_visible(timeout=10000)

    home_page.add_first_product_to_cart()
    
    # Ожидание появления зеленого уведомления об успешном добавлении
    expect(page.locator('.Toastify__toast')).to_be_visible(timeout=10000)

    # Переход в корзину
    cart_page = CartPage(page)
    cart_page.navigate()
    cart_page.go_to_checkout()

    # Заполнение данных
    checkout_page = CheckoutPage(page)

    # Ожидание загрузки формы оформления (появления поля First Name)
    expect(checkout_page.first_name).to_be_visible(timeout=10000)

    checkout_page.fill_shipping_info(
        first_name="Anna",
        last_name="Test",
        email="1111@yandex.ru",
        address="123 Test Street",
        city="Belgorod",
        pin_code="123456"
    )
    
    # Подтверждение заказа
    checkout_page.place_order()

    # Проверка, что заказ оформлен (например, появилось сообщение или редирект)  
    page.wait_for_timeout(2000) # Ожидание загрузки страницы
    expect(page).not_to_have_url("**/checkout") 