import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# Класс страницы
class ProductCartPage(BasePage):
    # Локаторы страницы
    HP_LP3065 = (By.XPATH, '//h1')
    SPECIFICATION = (By.CSS_SELECTOR, '#content > div > ul > li:nth-child(2) > a')
    ELEMENT_MEMORY = (By.CSS_SELECTOR, '#tab-specification > div > table > thead:nth-child(1) > tr > td > strong')
    REVIEWS = (By.CSS_SELECTOR, '#content > div > ul > li:nth-child(3) > a')
    TEXT_IN_REVIEWS = (By.XPATH, '//*[@id="form-review"]/h2')
    EMPTY_BASKET = (By.XPATH, '//*[@id="header-cart"]/div/ul/li')
    DROPDOWN_SELECT_COLORS = (By.XPATH, '//*[@id="input-option-226"]')
    OPTIONS_RED_COLOR = (By.XPATH, '//*[@id="input-option-226"]/option[2]')
    ADDTOCART_BUTTON = (By.XPATH, '//*[text()="Add to Cart"]')
    INITIAL_ITEM_NAME = (By.XPATH, '//*[@id="content"]/div/div[2]/h1')
    EXPECTED_ITEM_NAME = (By.XPATH, '//*[@id="checkout-confirm"]/div[1]/table/tbody/tr/td[1]/a')
    CHECKOUT = (By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[5]/a/span')

    def __init__(self, browser):
        super().__init__(browser) # передаём browser родительскому классу

    # Метод открывает url страницы в браузере
    @allure.step("Opening URL: http://192.168.0.144:8081/en-gb/product/laptop-notebook/hp-lp3065?limit=10")
    def open_url(self):
        url = "http://192.168.0.144:8081/en-gb/product/laptop-notebook/hp-lp3065?limit=10"
        self.logger.debug("%s: Opening URL: %s" % (self.class_name, url))
        try:
            self.browser.get(url)
            with allure.step("Successfully opened URL"):
                self.logger.info("%s: Successfully opened URL %s" % (self.class_name, url))
        except Exception as e:
            self.logger.error("%s: Failed to open URL: %s. Error: %s" % (self.class_name, url, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG)


    # Методы для страницы
    # Метод получает начальное название товара
    @allure.step("Getting initial name of the item")
    def get_initial_name_item(self):
        self.logger.debug("%s: Getting initial name of the item." % self.class_name)
        initial_name = self.find(self.INITIAL_ITEM_NAME)
        if initial_name is not None:
            self.logger.info("%s: Successfully found initial name of the item." % self.class_name)
        return initial_name


    # Метод получает ожидаемое название товара
    @allure.step("Getting expected name of the item")
    def get_expected_name_item(self):
        self.logger.debug("%s: Getting expected name of the item." % self.class_name)
        expected_name = self.find(self.EXPECTED_ITEM_NAME)
        if expected_name is not None:
            self.logger.info("%s: Successfully found expected name of the item." % self.class_name)
        return expected_name


    # Метод получает выпадающий список
    @allure.step("Getting dropdown for color selection")
    def get_dropdown(self):
        self.logger.debug("%s: Getting dropdown for color selection." % self.class_name)
        dropdown = self.find(self.DROPDOWN_SELECT_COLORS)
        if dropdown is not None:
            dropdown.click()
            self.logger.info("%s: Successfully clicked on color dropdown." % self.class_name)
        return dropdown


    # Метод получает опцию RED color
    @allure.step("Getting red color option")
    def get_options_red(self):
        self.logger.debug("%s: Getting red color option." % self.class_name)
        red_option = self.find(self.OPTIONS_RED_COLOR)
        if red_option is not None:
            red_option.click()
            self.logger.info("%s: Successfully clicked on red color option." % self.class_name)
        return red_option


    # Метод получает кнопку добавления в корзину
    @allure.step("Getting add to cart button")
    def get_button_addtocart(self):
        self.logger.debug("%s: Getting add to cart button." % self.class_name)
        add_to_cart_button = self.find(self.ADDTOCART_BUTTON)
        if add_to_cart_button is not None:
            self.logger.info("%s: Successfully found add to cart button." % self.class_name)
        return add_to_cart_button


    # Метод получает спецификацию товара
    @allure.step("Getting specification of the product")
    def get_specification(self):
        self.logger.debug("%s: Getting specification of the product." % self.class_name)
        try:
            specification_element = self.find_clickable(self.SPECIFICATION)
            specification_element.click()
            WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(self.ELEMENT_MEMORY))
            self.logger.info("%s: Successfully opened product specification." % self.class_name)
        except Exception as e:
            self.logger.error("%s: Error opening product specification. Error: %s" % (self.class_name, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Error opening product specification",
                attachment_type=allure.attachment_type.PNG)


    # Метод получает отзывы о товаре
    @allure.step("Getting reviews of the product")
    def get_reviews(self):
        self.logger.debug("%s: Getting reviews of the product." % self.class_name)
        try:
            reviews_element = self.find_clickable(self.REVIEWS)
            reviews_element.click()
            WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.TEXT_IN_REVIEWS))
            self.logger.info("%s: Successfully opened product reviews." % self.class_name)
        except Exception as e:
            self.logger.error("%s: Error opening product reviews. Error: %s" % (self.class_name, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Error opening product reviews",
                attachment_type=allure.attachment_type.PNG)


    # Метод проверяет список характеристик товара
    @allure.step("Checking list of product characteristics")
    def check_list_strong_item(self):
        expected_items = ['Memory', 'Processor']
        try:
            for i, item in enumerate(expected_items, start=1):
                xpath = f'//*[@id="tab-specification"]/div/table/thead[{i}]/tr/td/strong'
                actual_item = self.browser.find_element(By.XPATH, xpath).text
                assert actual_item == item, f"Наименование элемента #{i} не соответствует ожидаемому: {actual_item} != {item}"
                self.logger.info(f"{self.class_name}: Strong item #{i} is correct: {actual_item}")

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


    # Метод проверяет список меток для отзывов
    @allure.step("Checking list of tags for reviews")
    def check_list_label_item(self):
        expected_items = ['Your Name', 'Your Review', 'Rating']
        try:
            for i, item in enumerate(expected_items, start=2):
                xpath = f'//*[@id="form-review"]/div[{i}]/label'
                actual_item = self.browser.find_element(By.XPATH, xpath).text
                assert actual_item == item, f"Наименование элемента #{i} не соответствует ожидаемому: {actual_item} != {item}"
                self.logger.info(f"{self.class_name}: Label item #{i} is correct: {actual_item}")

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


    # Метод получает пустую корзину
    @allure.step("Getting empty cart-shopping element")
    def get_empty_cart_shopping(self):
        self.logger.debug("%s: Getting empty cart-shopping element." % self.class_name)
        empty_basket_element = self.find(self.EMPTY_BASKET)
        if empty_basket_element is not None:
            self.logger.info("%s: Successfully found empty cart-shopping element." % self.class_name)
        return empty_basket_element

    # Метод кликает по элементу 'Checkout'
    @allure.step("Clicking  button CHECKOUT")
    def checkout(self):
        self.logger.debug("%s: Clicking  button CHECKOUT." % self.class_name)
        try:
            checkout_button = self.find(self.CHECKOUT)
            checkout_button.click()
            self.logger.info("%s: Successfully clicked on CHECKOUT button." % self.class_name)
        except Exception as e:
            self.logger.error("%s: Error clicking on CHECKOUT button. Error: %s" % (self.class_name, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Error clicking on CHECKOUT button",
                attachment_type=allure.attachment_type.PNG)