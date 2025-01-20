from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Локаторы страницы
button_confirm_order_selector = (By.XPATH, '//*[@id="checkout-payment"]/div/button')

# Класс страницы
class CheckoutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser) # передаём browser родительскому классу

    # Метод открывает url страницы в браузере
    def open_url(self):
        self.browser.get("http://192.168.0.144:8081/en-gb?route=checkout/checkout")

    # Методы для страницы
    def get_confirm_order(self):
        return self.find(button_confirm_order_selector)