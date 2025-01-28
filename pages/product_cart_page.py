from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# Локаторы страницы
hp_lp3065 = (By.XPATH, '//h1')
specification_selector = (By.CSS_SELECTOR, '#content > div > ul > li:nth-child(2) > a')
element_memory_selector = (By.CSS_SELECTOR, '#tab-specification > div > table > thead:nth-child(1) > tr > td > strong')
reviews_selector = (By.CSS_SELECTOR, '#content > div > ul > li:nth-child(3) > a')
text_in_reviews = (By.XPATH, '//*[@id="form-review"]/h2')
empty_basket = (By.XPATH, '//*[@id="header-cart"]/div/ul/li')
dropdown_select_colors_selector = (By.XPATH, '//*[@id="input-option-226"]')
options_red_color_selector = (By.XPATH, '//*[@id="input-option-226"]/option[2]')
addtocart_button_selector = (By.XPATH, '//*[text()="Add to Cart"]')
initial_item_name_selector = (By.XPATH, '//*[@id="content"]/div/div[2]/h1')
expected_item_name_selector = (By.XPATH, '//*[@id="checkout-confirm"]/div[1]/table/tbody/tr/td[1]/a')

# Класс страницы
class ProductCartPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser) # передаём browser родительскому классу

    # Метод открывает url страницы в браузере
    def open_url(self):
        self.browser.get("http://192.168.0.144:8081/en-gb/product/laptop-notebook/hp-lp3065?limit=10")

    # Методы для страницы
    def get_initial_name_item(self):
        return self.find(initial_item_name_selector)

    def get_expected_name_item(self):
        return self.find(expected_item_name_selector)

    def get_dropdown(self):
        return self.find(dropdown_select_colors_selector).click()

    def get_options_red(self):
        return self.find(options_red_color_selector).click()

    def get_button_addtocart(self):
        return self.find(addtocart_button_selector)

    def get_specification(self):
        self.find_clickable(specification_selector).click()
        (WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(element_memory_selector)))

    def get_reviews(self):
        self.find_clickable(reviews_selector).click()
        (WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(text_in_reviews)))

    def check_list_strong_item(self):
        expected_items = ['Memory', 'Processor']
        for i, item in enumerate(expected_items, start=1):
            xpath = f'//*[@id="tab-specification"]/div/table/thead[{i}]/tr/td/strong'
            actual_item = self.browser.find_element(By.XPATH, xpath).text
            assert actual_item == item, f"Наименование элемента #{i} не соответствует ожидаемому: {actual_item} != {item}"

    def check_list_label_item(self):
        expected_items = ['Your Name', 'Your Review', 'Rating']
        for i, item in enumerate(expected_items, start=2):
            xpath = f'//*[@id="form-review"]/div[{i}]/label'
            actual_item = self.browser.find_element(By.XPATH, xpath).text
            assert actual_item == item, f"Наименование элемента #{i} не соответствует ожидаемому: {actual_item} != {item}"

    def get_empty_basket(self):
        return self.find(empty_basket)