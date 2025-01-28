from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# Локаторы страницы
dropdown_currency_selector = (By.XPATH, '//*[@id="form-currency"]/div/a/span')
desctops_selector = (By.XPATH, '//*[@id="column-left"]/div[1]/a[1]')
counter_selector = (By.XPATH, '//*[@id="content"]/div[5]/div[2]')
dropdown_show_selector = (By.XPATH, '//*[@id="input-limit"]')
dropdown_sort_by_selector =(By.XPATH, '//*[@id="input-sort"]')
options_sort_by = (By.XPATH, '//*[@id="input-sort"]/option')
button_grid_selector = (By.XPATH, '//*[@id="button-grid"]')
dropdown_currency = (By.XPATH, '//*[@id="form-currency"]/div/a')
eur_currency = (By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a')
item_selector = (By.XPATH, '//*[@id="product-list"]/div[1]/div/div[1]/a/img')
product_code = (By.XPATH, '//*[@id="content"]/div/div[2]/ul[1]/li[2]')
price_element = (By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[1]/h2/span')

# Класс страницы
class CatalogPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser) # передаём browser родительскому классу

    # Метод открывает url страницы в браузере
    def open_url(self):
        self.browser.get("http://192.168.0.144:8081/en-gb/catalog/laptop-notebook")

    # Методы для страницы
    def get_element_counter(self):
        return self.find(counter_selector)

    def get_element_dropdown_show(self):
        return self.find(dropdown_show_selector)

    def get_button_grid(self):
        return self.find(dropdown_sort_by_selector)

    def check_values_in_show(self):
        expected_values = ["10", "25", "50", "75", "100"]
        for i, value in enumerate(expected_values, start=1):
            xpath = f'//*[@id="input-limit"]/option[{i}]'
            actual_value = self.browser.find_element(By.XPATH, xpath).text
            assert actual_value == value, f"Значение опции #{i} не соответствует ожидаемому: {actual_value} != {value}"

    def get_element_default(self):
        return self.find(dropdown_sort_by_selector)

    def check_values_in_sort_by(self):
        # Получаем список всех элементов option внутри селектора
        options = (WebDriverWait(self.browser, 2).until
                   (EC.presence_of_all_elements_located((By.XPATH, '//*[@id="input-sort"]/option'))))

        expected_options = ["Default",
                            "Name (A - Z)",
                            "Name (Z - A)",
                            "Price (Low > High)",
                            "Price (High > Low)",
                            "Rating (Highest)",
                            "Rating (Lowest)",
                            "Model (A - Z)",
                            "Model (Z - A)"]

        for i in range(len(options)):
            actual_text = options[i].text
            expected_text = expected_options[i]
            assert actual_text == expected_text, f'Ожидается "{expected_text}", но получено "{actual_text}"'

    def check_list_group_item(self):
        expected_items = ["Desktops (13)",
                          "Laptops & Notebooks (5)",
                          "   - Macs (0)",
                          "   - Windows (0)",
                          "Components (2)",
                          "Tablets (1)",
                          "Software (0)",
                          "Phones & PDAs (3)",
                          "Cameras (2)",
                          "MP3 Players (4)"]

        for i, item in enumerate(expected_items, start=1):
            xpath = f'//*[@id="column-left"]/div[1]/a[{i}]'
            actual_item = self.browser.find_element(By.XPATH, xpath).text

    def get_dropdown_currency(self):
        return self.find(dropdown_currency_selector).click()

    def get_item(self):
        return self.find(item_selector).click()

    def get_product_code(self):
        return self.find(product_code).click()

    def get_price_item(self):
        return self.find(price_element).text

    def get_eur_currency(self,):
        return self.find(eur_currency).click()