class SignupPage:
    def __init__(self, page):
        self.page = page
        self.url = "http://localhost:5173/signup"
        
        self.name_input = page.locator('input[type="text"]').first
        self.email_input = page.locator('input[type="email"]')
        self.password_input = page.locator('input[type="password"]')
        self.submit_button = page.get_by_role("button", name="Sign Up")

    def navigate(self):
        # Открытие страницы регистрации
        self.page.goto(self.url)

    def register(self, name, email, password):
        # Ввод имени
        self.name_input.fill(name)
        # Ввод email
        self.email_input.fill(email)
        # Ввод пароля
        self.password_input.fill(password)
        # Нажатие кнопки
        self.submit_button.click()