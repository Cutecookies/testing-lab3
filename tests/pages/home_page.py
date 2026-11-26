class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = "http://localhost:5173/"
        
        # Локаторы
        self.product_cards = page.locator('.group.border.rounded-lg')
        self.first_add_to_cart_button = page.get_by_role("button", name="Add Cart").first

    def navigate(self):
        # Открытие главной страницы
        self.page.goto(self.url)

    def add_first_product_to_cart(self):
        # Нажатие кнопки "Add Cart" у первого товара
        self.first_add_to_cart_button.click()

    def logout(self):
    # Нажатие кнопки "Logout"
        self.page.get_by_role("button", name="Logout").click()