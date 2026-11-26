from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page):
        self.page = page
        self.url = "http://localhost:5173/cart"
        
        # Кнопка перехода к оформлению
        self.proceed_to_checkout_button = page.get_by_role("button", name="Proceed to Checkout")

    def navigate(self):
        # Открытие страницы корзины
        self.page.goto(self.url)

    def go_to_checkout(self):
        expect(self.proceed_to_checkout_button).to_be_visible(timeout=15000)
        # Нажатие кнопки перехода к оформлению
        self.proceed_to_checkout_button.click()