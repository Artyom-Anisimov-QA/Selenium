from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# Описание локаторов
price_macbook_us_dollar_selector = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/div/div/span[1]')
price_iphone_us_dollar_selector = (By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div/div/span[1]')
price_apple_cinema_us_dollar_selector = (By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div[2]/div/div/span[1]')
price_canon_eos_5d_us_dollar_selector = (By.XPATH,'//*[@id="content"]/div[2]/div[4]/div/div[2]/div/div/span[1]')
pound_sterling_selector = (By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]/a')
price_macbook_pound_sterling_selector = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/div/div/span[1]')
price_iphone_pound_sterling_selector = (By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div/div/span[1]')
price_apple_cinema_pound_sterling_selector = (By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div[2]/div/div/span[1]')
price_canon_eos_5d_pound_sterling_selector = (By.XPATH, '//*[@id="content"]/div[2]/div[4]/div/div[2]/div/div/span[1]')
search_button_selector = (By.XPATH, '//*[@id="search"]/button')
remove_button_selector = (By.XPATH, '//*[@class="fa-solid fa-circle-xmark"]/parent::*')
basket_button_selector = (By.XPATH, '//*[@id="header-cart"]/div/button')
empty_modal_window_selector = (By.XPATH, '//*[@id="header-cart"]/div/ul/li')
popup_window_selector = (By.XPATH, '//*[@id="alert"]/div')
checkout_selector = (By.XPATH, '//*[@id="header-cart"]/div/ul/li/div/p/a[2]/strong')
modal_window_selector = (By.XPATH, '//*[@id="header-cart"]/div/ul')

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    # Метод ищет элементы на странице
    def find(self, *args):
        return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(*args))

    # Метод ищет кликабельные элементы на странице
    def find_clickable(self, *args):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(*args))

    # Метод кликает по элементу
    def custom_click(self, element):
        ActionChains(self.browser).move_to_element(element).pause(0.5).click().perform()

    # Метод ищет кнопку Корзина на странице
    def get_button_basket(self):
        return self.find(basket_button_selector)

    # Метод ищет модальное окно
    def get_modal_window(self):
        return self.browser.find_element(By.NAME, "Your shopping cart is empty!")

    # Метод дёт пропадания всплывающего окна
    def get_popup_window_down(self):
        old_element = self.find(popup_window_selector)
        WebDriverWait(self.browser, 10).until(EC.staleness_of(old_element))

    # Метод кликает по элементу checkout
    def checkout(self):
        self.browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/ul/li/div/p/a[2]/strong').click()