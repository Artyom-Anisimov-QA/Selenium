import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


# Класс страницы
class CheckoutPage(BasePage):
    # Локаторы страницы
    BUTTON_CONFIRM_ORDER = (By.XPATH, '//*[@id="checkout-payment"]/div/button')

    def __init__(self, browser):
        super().__init__(browser) # передаём browser родительскому классу

    # Метод открывает url страницы в браузере
    @allure.step("Opening URL")
    def open_url(self, url="http://192.168.0.144:8081/en-gb?route=checkout/checkout"):
        self.logger.debug("%s: Opening URL: %s" % (self.class_name, url))
        try:
            self.browser.get(url)
            self.logger.info("%s: Successfully opened URL: %s" % (self.class_name, url))
        except Exception as e:
            self.logger.error("%s: Failed to open URL: %s. Error: %s" % (self.class_name, url, str(e)))
            raise Exception(f"Failed to open URL: {url}. Error: {e}")


    # Метод получает кнопку подтверждения заказа
    @allure.step("Getting confirm order button")
    def get_confirm_order(self):
        self.logger.debug("%s: Getting confirm order button." % self.class_name)
        try:
            confirm_button = self.find(self.BUTTON_CONFIRM_ORDER)
            if confirm_button is not None:
                self.logger.info("%s: Successfully found confirm order button." % self.class_name)
            else:
                self.logger.warning("%s: Confirm order button not found." % self.class_name)
            return confirm_button
        except Exception as e:
            self.logger.error("%s: Error finding confirm order button. Error: %s" % (self.class_name, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Error finding confirm order button",
                attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error finding confirm order button: {e}")