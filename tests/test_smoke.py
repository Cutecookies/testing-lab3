from playwright.sync_api import Page, expect

def test_homepage_loads(page: Page):
    # Открытие локального сайта
    page.goto("http://localhost:5173/")
    
    # Проверка, что заголовок страницы (вкладки) содержит Vite + React + TS
    expect(page).to_have_title("Vite + React + TS")