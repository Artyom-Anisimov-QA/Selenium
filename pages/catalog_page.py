import allure
from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# Класс страницы
class CatalogPage(BasePage):
    # Локаторы страницы
    DROPDOWN_CURRENCY = (By.XPATH, '//*[@id="form-currency"]/div/a/span')
    DESKTOPS = (By.XPATH, '//*[@id="column-left"]/div[1]/a[1]')
    COUNTER = (By.XPATH, '//*[@id="content"]/div[5]/div[2]')
    DROPDOWN_SHOW = (By.XPATH, '//*[@id="input-limit"]')
    DROPDOWN_SORT_BY = (By.XPATH, '//*[@id="input-sort"]')
    OPTIONS_SORT_BY = (By.XPATH, '//*[@id="input-sort"]/option')
    BUTTON_GRID = (By.XPATH, '//*[@id="button-grid"]')
    EUR_CURRENCY = (By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a')
    ITEM_SELECTOR = (By.XPATH, '//*[@id="product-list"]/div[1]/div/div[1]/a/img')
    PRODUCT_CODE = (By.XPATH, '//*[@id="content"]/div/div[2]/ul[1]/li[2]')
    PRICE_ELEMENT = (By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[1]/h2/span')

    def __init__(self, browser):
        super().__init__(browser) # передаём browser родительскому классу

    # Метод открывает url страницы в браузере
    @allure.step("Opening URL")
    def open_url(self, url="http://192.168.0.144:8081/en-gb/catalog/laptop-notebook"):
        self.logger.debug("%s: Opening URL: %s" % (self.class_name, url))
        try:
            self.browser.get(url)
            self.logger.info("%s: Successfully opened URL: %s" % (self.class_name, url))
        except Exception as e:
            self.logger.error("%s: Failed to open URL: %s. Error: %s" % (self.class_name, url, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Failed to open URL",
                attachment_type=allure.attachment_type.PNG)


    # Методы для страницы
    # Метод получает элемент счетчика
    @allure.step("Getting element counter")
    def get_element_counter(self):
        self.logger.debug("%s: Getting element counter." % self.class_name)
        counter = self.find(self.COUNTER)
        if counter is not None:
            self.logger.info("%s: Successfully found element counter." % self.class_name)
        return counter


    # Метод получает элемент выпадающего списка
    @allure.step("Getting dropdown show element")
    def get_element_dropdown_show(self):
        self.logger.debug("%s: Getting dropdown show element." % self.class_name)
        dropdown_show = self.find(self.DROPDOWN_SHOW)
        if dropdown_show is not None:
            self.logger.info("%s: Successfully found dropdown show element." % self.class_name)
        return dropdown_show


    # Метод получает кнопку "Grid"
    @allure.step("Getting button Grid")
    def get_button_grid(self):
        self.logger.debug("%s: Getting button Grid." % self.class_name)
        button_grid = self.find(self.DROPDOWN_SORT_BY)
        if button_grid is not None:
            self.logger.info("%s: Successfully found button grid." % self.class_name)
        return button_grid


    # Метод проверяет значения в выпадающем списке "Show"
    @allure.step("Checking values in dropdown 'Show'")
    def check_values_in_show(self):
        expected_values = ["10", "25", "50", "75", "100"]
        self.logger.debug("%s: Checking values in dropdown Show." % self.class_name)
        try:
            for i, value in enumerate(expected_values, start=1):
                xpath = f'//*[@id="input-limit"]/option[{i}]'
                actual_value = self.browser.find_element(By.XPATH, xpath).text
                assert actual_value == value, f"Значение опции #{i} не соответствует ожидаемому: {actual_value} != {value}"
                self.logger.info(f"{self.class_name}: Option #{i} value is correct: {actual_value}")

        except NoSuchElementException as e:
            error_message = f"Элемент #{i} не найден: {e}"
            self.logger.error(f"{self.class_name}: {error_message}")
            allure.attach(
                name=f"Element not found: {xpath}",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(error_message)

        except AssertionError as e:
            error_message = str(e)
            self.logger.error(f"{self.class_name}: {error_message}")
            allure.attach(
                name=f"Assertion failed: {xpath}",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG)
            raise

        except Exception as e:
            error_message = f"Неизвестная ошибка при проверке элемента #{i}: {e}"
            self.logger.error(f"{self.class_name}: {error_message}")
            allure.attach(
                name=f"Unexpected error: {xpath}",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG)


    # Метод получает элемент
    def get_element_default(self):
        self.logger.debug("%s: Getting default element." % self.class_name)
        default_element = self.find(self.DROPDOWN_SORT_BY)
        if default_element is not None:
            self.logger.info("%s: Successfully found default element." % self.class_name)
        return default_element


    # Метод проверяет значения в выпадающем списке "Sort By"
    @allure.step("Checking values in dropdown 'Sort By' dropdown")
    def check_values_in_sort_by(self):
        expected_options = [
            "Default",
            "Name (A - Z)",
            "Name (Z - A)",
            "Price (Low > High)",
            "Price (High > Low)",
            "Rating (Highest)",
            "Rating (Lowest)",
            "Model (A - Z)",
            "Model (Z - A)"
        ]

        self.logger.debug("%s: Checking values in sort by dropdown." % self.class_name)

        options = WebDriverWait(self.browser, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="input-sort"]/option'))
        )

        for i in range(len(options)):
            actual_text = options[i].text
            expected_text = expected_options[i]
            assert actual_text == expected_text, f'Ожидается "{expected_text}", но получено "{actual_text}"'
            self.logger.info(f"{self.class_name}: Sort by option {i + 1} is correct: {actual_text}")


    # Метод проверяет список групповых элементов
    @allure.step("Checking list group items")
    def check_list_group_item(self):
        expected_items = [
            "Desktops (12)",
            "Laptops & Notebooks (5)",
            "   - Macs (0)",
            "   - Windows (0)",
            "Components (2)",
            "Tablets (1)",
            "Software (0)",
            "Phones & PDAs (2)",
            "Cameras (2)",
            "MP3 Players (4)"
        ]

        self.logger.debug("%s: Checking list group items." % self.class_name)
        try:
            for i, item in enumerate(expected_items, start=1):
                xpath = f'//*[@id="column-left"]/div[1]/a[{i}]'
                actual_item = self.browser.find_element(By.XPATH, xpath).text
                assert actual_item == item, f'Ожидается "{item}", но получено "{actual_item}"'
                self.logger.info(f"{self.class_name}: List group item {i} is correct: {actual_item}")

        except NoSuchElementException as e:
            error_message = f"Элемент #{i} не найден: {e}"
            self.logger.error(f"{self.class_name}: {error_message}")
            allure.attach(
                name=f"Element not found: {xpath}",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(error_message)

        except AssertionError as e:
            error_message = str(e)
            self.logger.error(f"{self.class_name}: {error_message}")
            allure.attach(
                name=f"Assertion failed: {xpath}",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG)
            raise

        except Exception as e:
            error_message = f"Неизвестная ошибка при проверке элемента #{i}: {e}"
            self.logger.error(f"{self.class_name}: {error_message}")
            allure.attach(
                name=f"Unexpected error: {xpath}",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG)


    # Метод получает выпадающий список валюты
    @allure.step("Getting dropdown currency element")
    def get_dropdown_currency(self):
        self.logger.debug("%s: Getting dropdown currency element." % self.class_name)
        currency_dropdown = self.find(self.DROPDOWN_CURRENCY)
        if currency_dropdown is not None:
            currency_dropdown.click()
            self.logger.info("%s: Successfully clicked on dropdown currency element." % self.class_name)
        return currency_dropdown


    # Метод получает элемент товара
    @allure.step("Getting item element")
    def get_item(self):
        self.logger.debug("%s: Getting item element." % self.class_name)
        item = self.find(self.ITEM_SELECTOR)
        if item is not None:
            item.click()
            self.logger.info("%s: Successfully clicked on item element." % self.class_name)
        return item


    # Метод получает код продукта
    @allure.step("Getting product code element")
    def get_product_code(self):
        self.logger.debug("%s: Getting product code element." % self.class_name)
        product_code_element = self.find(self.PRODUCT_CODE)
        if product_code_element is not None:
            product_code_element.click()
            self.logger.info("%s: Successfully clicked on product code element." % self.class_name)
        return product_code_element


    # Метод получает цену товара
    @allure.step("Getting currency product")
    def get_price_item(self):
        price = self.find(self.PRICE_ELEMENT).text
        if price:
            self.logger.info(f"{self.class_name}: Price of the item is {price}.")
        return price


    # Метод получает евро валюту
    @allure.step("Getting EUR currency")
    def get_eur_currency(self):
        self.logger.debug("%s: Getting EUR currency element." % self.class_name)
        eur_currency_element = self.find(self.EUR_CURRENCY)
        if eur_currency_element is not None:
            eur_currency_element.click()
            self.logger.info("%s: Successfully clicked on EUR currency element." % self.class_name)