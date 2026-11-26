class CheckoutPage:
    def __init__(self, page):
        self.page = page
        
        # Локаторы полей 
        self.first_name = page.locator('input[name="firstName"]')
        self.last_name = page.locator('input[name="lastName"]')
        self.email = page.locator('input[name="email"]') 
        self.address = page.locator('input[name="address"]')
        self.city = page.locator('input[name="city"]')
        self.pin_code = page.locator('input[name="pinCode"]')

        # Кнопка подтверждения заказа
        self.place_order_button = page.get_by_role("button", name="Place Order")

    def fill_shipping_info(self, first_name, last_name, email, address, city, pin_code):
        # Заполнение формы доставки
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.email.fill(email)
        self.address.fill(address)
        self.city.fill(city)
        self.pin_code.fill(pin_code)

    def place_order(self):
        # Нажатие кнопки оформления
        self.place_order_button.click()