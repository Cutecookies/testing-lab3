class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "http://localhost:5173/login"
        
        # Селекторы 
        self.email_input = page.locator('input[type="email"]')
        self.password_input = page.locator('input[type="password"]')
        self.submit_button = page.get_by_role("button", name="Login") 

    def navigate(self):
        # Открытие страницы логина
        self.page.goto(self.url)

    def login(self, email, password):
        # Заполнение формы входа
        self.email_input.fill(email)
        self.password_input.fill(password)
        # Нажатие кнопки
        self.submit_button.click()