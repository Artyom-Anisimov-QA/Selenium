from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# Локаторы страницы
featured_element_selector = (By.XPATH, '//*[text()="Featured"]')
banner_dat_left_selector = (By.XPATH, '//*[@id="carousel-banner-0"]/div[1]/button[1]')
banner_dat_right_selector = (By.XPATH, '//*[@id="carousel-banner-0"]/div[1]/button[2]')
carousel_selector = (By.XPATH, '//*[@id="carousel-banner-0"]/div[2]/div[1]')
item_selector = (By.XPATH, '//*[@id="content"]/div[2]/div[4]/div/div[1]/a/img')
camera_element_selector = (By.CSS_SELECTOR, '#product-info > ul > li:nth-child(2) > a')
expected_text_element_item_in_basket_selector = (By.CSS_SELECTOR, '#header-cart > div > ul > li > table > tbody > tr > td.text-start > a')

# Класс страницы
class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser) # передаём browser родительскому классу

    # Метод открывает url страницы в браузере
    def open_url(self):
        self.browser.get("http://192.168.0.144:8081")

    # Методы для страницы
    def get_item(self):
        return self.find(item_selector).click()

    def get_element_initial(self):
        return self.find(camera_element_selector)

    def get_expected_text(self, *args):
        return self.find(expected_text_element_item_in_basket_selector)

    # Ищем элемент Карусель
    def get_carousel_element(self):
        return self.find(carousel_selector)

    # Метод явно ожидает изменения атрибута элемента карусели
    def find_change_carousel(self, *args):
        return WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(*args))