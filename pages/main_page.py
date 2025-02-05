import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


# Класс страницы
class MainPage(BasePage):
    # Локаторы страницы
    FEATURED_ELEMENT_SELECTOR = (By.XPATH, '//*[text()="Featured"]')
    BANNER_DAT_LEFT_SELECTOR = (By.XPATH, '//*[@id="carousel-banner-0"]/div[1]/button[1]')
    BANNER_DAT_RIGHT_SELECTOR = (By.XPATH, '//*[@id="carousel-banner-0"]/div[1]/button[2]')
    CAROUSEL_SELECTOR = (By.XPATH, '//*[@id="carousel-banner-0"]/div[2]/div[1]')
    ITEM_SELECTOR = (By.XPATH, '//*[@id="content"]/div[2]/div[4]/div/div[1]/a/img')
    CAMERA_ELEMENT_SELECTOR = (By.CSS_SELECTOR, '#product-info > ul > li:nth-child(2) > a')
    EXPECTED_TEXT_ELEMENT_ITEM_IN_BASKET_SELECTOR = (By.CSS_SELECTOR, '#header-cart > div > ul > li > table > tbody > tr > td.text-start > a')

    def __init__(self, browser):
        super().__init__(browser)

    # Метод открывает url страницы в браузере
    @allure.step("Opening URL")
    def open_url(self, url="http://192.168.0.144:8081"):
        self.logger.debug("%s: Opening URL: %s" % (self.class_name, url))
        try:
            self.browser.get(url)
            self.logger.info("%s: Successfully opened URL: %s" % (self.class_name, url))
        except Exception as e:
            self.logger.error("%s: Failed to open URL: %s. Error: %s" % (self.class_name, url, str(e)))


    # Методы для страницы
    # Методы ищет продукт на странице
    @allure.step("Selecting a product")
    def get_item(self):
        self.logger.debug(f"{self.class_name}: Selecting a product.")
        try:
            item = self.find(self.ITEM_SELECTOR)
            item.click()
            self.logger.info(f"{self.class_name}: Successfully selected a product.")
            return item
        except Exception as e:
            self.logger.error(f"{self.class_name}: Error selecting product. Error: {str(e)}")
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Error selecting product",
                attachment_type=allure.attachment_type.PNG)
            return None

    # Метод находит элемент камеры на странице
    @allure.step("Finding camera element on page")
    def get_element_initial(self):
        self.logger.debug(f"{self.class_name}: Finding {self.CAMERA_ELEMENT_SELECTOR} element on page.")
        try:
            element = self.find(self.CAMERA_ELEMENT_SELECTOR)
            self.logger.info(f"{self.class_name}: Successfully found {self.CAMERA_ELEMENT_SELECTOR} element.")
            return element
        except Exception as e:
            self.logger.error(f"{self.class_name}: Error finding {self.CAMERA_ELEMENT_SELECTOR} element. Error: {str(e)}")
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name=f"Error finding {self.CAMERA_ELEMENT_SELECTOR} element",
                attachment_type=allure.attachment_type.PNG)
            return None


    # Метод находит ожидаемый текст элемента
    @allure.step("Finding expected text in basket")
    def get_expected_text(self):
        self.logger.debug(f"{self.class_name}: Finding expected text in basket.")
        try:
            expected_text = self.find(self.EXPECTED_TEXT_ELEMENT_ITEM_IN_BASKET_SELECTOR)
            self.logger.info(f"{self.class_name}: Successfully found expected text in basket.")
            return expected_text
        except Exception as e:
            self.logger.error(f"{self.class_name}: Error finding expected text in basket. Error: {str(e)}")
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Error finding expected text in basket",
                attachment_type=allure.attachment_type.PNG)
            return None


    # Метод ищет элемент карусели на странице
    @allure.step("Finding carousel element on page")
    def get_carousel_element(self):
        self.logger.debug(f"{self.class_name}: Finding carousel element on page.")
        try:
            carousel_element = self.find(self.CAROUSEL_SELECTOR)
            self.logger.info(f"{self.class_name}: Successfully found carousel element.")
            return carousel_element
        except Exception as e:
            self.logger.error(f"{self.class_name}: Error finding carousel element. Error: {str(e)}")
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Error finding carousel element",
                attachment_type=allure.attachment_type.PNG)
            return None


    # Метод ожидает изменения атрибута элемента карусели
    @allure.step("Finding carousel element on page")
    def find_change_carousel(self, *args):
        self.logger.debug(f"{self.class_name}: Waiting for the attribute of the carousel element to change.")
        try:
            result = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(*args))
            self.logger.info(f"{self.class_name}: Successfully detected change in carousel element attribute.")
            return result
        except Exception as e:
            self.logger.error(f"{self.class_name}: Error waiting for carousel element attribute change. Error: {str(e)}")
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Error waiting for carousel element attribute change",
                attachment_type=allure.attachment_type.PNG)
            return None