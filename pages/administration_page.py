import allure
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# Класс страницы
class AdminPage(BasePage):
    # Локаторы страницы
    LOGIN = (By.XPATH, '//*[@id="input-username"]')
    PASSWD = (By.XPATH, '//*[@id="input-password"]')
    USERNAME = (By.XPATH, '//*[@id="form-login"]/div[1]/label')
    PASSWORD_ELEM = (By.XPATH, '//*[@id="form-login"]/div[2]/label')
    BUTTON_LOGIN = (By.XPATH, '//*[@id="form-login"]/div[3]/button')
    MENU_CATALOG = (By.XPATH, '//*[@id="menu-catalog"]/a')
    MENU_CUSTOMERS = (By.XPATH, '//*[@id="menu-customer"]/a')
    MENU_PRODUCTS = (By.XPATH, '//*[@id="collapse-1"]/li[2]/a')
    ELEMENT_CUSTOMERS = (By.XPATH, '//*[@id="collapse-5"]/li[1]/a')
    ADD_NEW = (By.XPATH, '//*[@id="content"]/div[1]/div/div/a/i')
    PRODUCT_NAME = (By.XPATH, '//*[@id="input-name-1"]')
    META_TAG_TITLE = (By.XPATH, '//*[@id="input-meta-title-1"]')
    MENU_DATA = (By.XPATH, '//*[@id="form-product"]/ul/li[2]/a')
    MENU_IMAGE = (By.XPATH, '//*[@id="form-product"]/ul/li[9]/a')
    MENU_SEO = (By.XPATH, '//*[@id="form-product"]/ul/li[11]/a')
    MODEL_INPUT = (By.XPATH, '//*[@id="input-model"]')
    PRICE_INPUT = (By.XPATH, '//*[@id="input-price"]')
    KEYWORD_INPUT = (By.XPATH, '//*[@id="input-keyword-0-1"]')
    NAME_INPUT = (By.XPATH, '//*[@id="input-name"]')
    EMAIL_INPUT = (By.XPATH, '//*[@id="input-email"]')
    BUTTON_EDIT = (By.XPATH, '//*[@id="image"]/div/button[1]')
    BUTTON_SAVE = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button/i')
    BUTTON_FILTER = (By.XPATH, '//*[@id="button-filter"]')
    BUTTON_DELETE = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button[3]')
    BUTTON_LOGOUT = (By.XPATH, '//*[@id="nav-logout"]/a/span')
    IMAGE = (By.XPATH, '//*[@id="filemanager"]/div/div[2]/div[3]/div[3]/div[1]/a/img')
    TO_END_ELEMENT = (By.XPATH, '//*[@id="form-product"]/div[2]/div[1]/ul/li[5]/a')
    EXCEPTION_ALERT = (By.XPATH, '//*[@id="alert"]/div')
    CHECKBOX = (By.XPATH, '//*[@id="form-product"]/div[1]/table/thead/tr/td[1]/input')
    EXCEPTION_ELEMENT = (By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr/td')
    EXCEPTION_EMAIL = (By.XPATH, '//*[@id="form-customer"]/div[1]/table/tbody/tr/td[3]')
    MOLOKO = (By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div/div[1]')

    def __init__(self, browser):
        super().__init__(browser) # передаём browser родительскому классу


    # Метод открывает url страницы в браузере
    @allure.step("Opening URL")
    def open_url(self):
        url = "http://192.168.0.144:8081/administration/"
        self.logger.debug("%s: Opening URL: %s" % (self.class_name, url))
        try:
            self.browser.get(url)
            with allure.step("Successfully opened URL"):
                self.logger.info("%s: Successfully opened URL %s" % (self.class_name, url))
        except Exception as e:
            self.logger.error("%s: Failed to open URL: %s. Error: %s" % (self.class_name, url, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Failed to open URL",
                attachment_type=allure.attachment_type.PNG)


    # Методы для страницы
    # Метод авторизации в админке
    @allure.step("Signing in to admin page")
    def sing_in(self):
        self.logger.debug("%s: Signing in to admin page." % self.class_name)
        try:
            login = self.find(self.LOGIN)
            password = self.find(self.PASSWD)
            login.send_keys('user')
            password.send_keys('bitnami')
            self.find_clickable(self.BUTTON_LOGIN).click()
            with allure.step("Successfully signed in as user"):
                self.logger.info("%s: Successfully signed in as user." % self.class_name)
        except Exception as e:
            self.logger.error("%s: Error during sign in. Error: %s" % (self.class_name, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Error during sign in",
                attachment_type=allure.attachment_type.PNG)


    # Метод разлогина из админки
    @allure.step("Signing out from admin panel")
    def sing_out(self):
        self.logger.debug("%s: Signing out from admin panel." % self.class_name)
        try:
            self.find_clickable(self.BUTTON_LOGOUT).click()
            with allure.step("Successfully signed out"):
                self.logger.info("%s: Successfully signed out." % self.class_name)
        except Exception as e:
            self.logger.error("%s: Error during sign out. Error: %s" % (self.class_name, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Error during sign out",
                attachment_type=allure.attachment_type.PNG)


    # Метод открывает меню для добавления нового продукта
    @allure.step("Opening menu for products")
    def open_menu_products(self):
        self.logger.debug("%s: Opening menu for products." % self.class_name)
        try:
            self.find_clickable(self.MENU_CATALOG).click()
            self.find_clickable(self.MENU_PRODUCTS).click()
            with allure.step("Successfully opened products menu"):
                self.logger.info("%s: Successfully opened products menu." % self.class_name)
        except Exception as e:
            self.logger.error("%s: Error opening products menu. Error: %s" % (self.class_name, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Error opening products menu",
                attachment_type=allure.attachment_type.PNG)


    # Метод открывает список пользователей opencart
    @allure.step("Opening customer list")
    def open_customer_list(self):
        self.logger.debug("%s: Opening customer list." % self.class_name)
        try:
            self.find_clickable(self.MENU_CUSTOMERS).click()
            self.find_clickable(self.ELEMENT_CUSTOMERS).click()
            with allure.step("Successfully opened customer list"):
                self.logger.info("%s: Successfully opened customer list." % self.class_name)
        except Exception as e:
            self.logger.error("%s: Error opening customer list. Error: %s" % (self.class_name, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Error opening customer list",
                attachment_type=allure.attachment_type.PNG)


    # Метод поиска пользователя
    @allure.step("Searching a customer")
    def search_customer(self):
        filename = 'email.txt'
        try:
            # Чтение email из файла
            with open(filename, 'r') as file:
                initial_email = file.read().strip()  # Удаляем лишние пробелы и символы новой строки
            os.remove(filename)  # Удаление файла после чтения

            self.logger.debug("%s: Searching for customer with email: %s" % (self.class_name, initial_email))

            # Установка масштаба страницы
            self.browser.execute_script("document.body.style.zoom='75%'")

            # Ввод email в поле поиска
            with allure.step("Insert email in the input search"):
                self.find(self.EMAIL_INPUT).click()
                self.find(self.EMAIL_INPUT).send_keys(initial_email)

            # Применение фильтра
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(self.BUTTON_FILTER))
            self.find(self.BUTTON_FILTER).click()

            # Ожидание появления email в результатах поиска
            with allure.step("Waiting for expected email in search results"):
                expected_email = WebDriverWait(self.browser, 5).until(
                    EC.visibility_of_element_located(self.EXCEPTION_EMAIL)).text

            # Проверка, что найденный email соответствует ожидаемому
            assert expected_email == initial_email, f"Expected email: {initial_email}, but found: {expected_email}"
            self.logger.info("%s: Customer found with email: %s" % (self.class_name, expected_email))

        except AssertionError:
            # Логирование и прикрепление скриншота при ошибке AssertionError
            self.logger.error("%s: Expected email does not match found email." % self.class_name)
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="assertion_error_screenshot",
                attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            # Логирование и прикрепление скриншота при других ошибках
            self.logger.error("%s: Error searching for customer. Error: %s" % (self.class_name, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="error_screenshot",
                attachment_type=allure.attachment_type.PNG)


    # Метод добавления нового продукта в Products
    @allure.step("Adding a new product")
    def add_new_product(self):
        self.logger.debug("%s: Starting the process of adding a new product." % self.class_name)
        try:
            # Установка масштаба страницы
            self.browser.execute_script("document.body.style.zoom='70%'")
            self.logger.info("%s: Page zoom set to 70%%." % self.class_name)

            # Клик по элементу добавления нового продукта
            with allure.step("Clicking on 'Add New' button"):
                self.find_clickable(self.ADD_NEW).click()
                self.logger.info("%s: Clicked on 'Add New' button." % self.class_name)

            # Установка масштаба страницы
            self.browser.execute_script("document.body.style.zoom='50%'")
            self.logger.info("%s: Page zoom set to 50%%." % self.class_name)

            # Заполнение полей продукта
            with allure.step("Filling product details"):
                self.find_clickable(self.PRODUCT_NAME).send_keys('Xiaomi 12x')
                self.logger.info("%s: Set product name to 'Xiaomi 12x'." % self.class_name)

                self.find_clickable(self.META_TAG_TITLE).send_keys('Xiaomi 12x')
                self.logger.info("%s: Set meta tag title to 'Xiaomi 12x'." % self.class_name)

                self.find_clickable(self.MENU_DATA).click()
                self.logger.info("%s: Clicked on 'Data' menu." % self.class_name)

                self.find_clickable(self.MODEL_INPUT).send_keys('Product 25')
                self.logger.info("%s: Set model to 'Product 25'." % self.class_name)

                self.find_clickable(self.PRICE_INPUT).send_keys('750$')
                self.logger.info("%s: Set price to '750$'." % self.class_name)

            # Установка масштаба страницы
            self.browser.execute_script("document.body.style.zoom='60%'")
            self.logger.info("%s: Page zoom set to 60%%." % self.class_name)

            # Добавление изображения
            with allure.step("Adding product image"):
                self.find_clickable(self.MENU_IMAGE).click()
                self.find(self.BUTTON_EDIT).click()
                self.find(self.IMAGE).click()
                self.logger.info("%s: Set image 'Xiaomi 12x'." % self.class_name)

            # Заполнение SEO-данных
            with allure.step("Filling SEO details"):
                self.find_clickable(self.MENU_SEO).click()
                self.find_clickable(self.KEYWORD_INPUT).send_keys('Xiaomi_12x')
                self.logger.info("%s: Set SEO keyword to 'Xiaomi_12x'." % self.class_name)

            # Сохранение продукта
            with allure.step("Saving the product"):
                self.find(self.BUTTON_SAVE).click()
                self.logger.debug("%s: Clicked on save button." % self.class_name)

            # Проверка на успешное добавление продукта
            with allure.step("Checking for success alert"):
                expected = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.EXCEPTION_ALERT))
                assert expected.text == 'Success: You have modified products!'
                self.logger.info("%s: Product added successfully. Alert message received: '%s'" % (self.class_name, expected.text))

        except AssertionError:
            # Логирование и прикрепление скриншота при ошибке AssertionError
            self.logger.error("%s: Product addition failed. Expected alert message not received." % self.class_name)
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="assertion_error_screenshot",
                attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            # Логирование и прикрепление скриншота при других ошибках
            self.logger.error("%s: Error adding new product. Error: %s" % (self.class_name, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="error_screenshot",
                attachment_type=allure.attachment_type.PNG)


# Метод удаления продукта из списка Products
    @allure.step("Deleting a product")
    def delete_product(self):
        self.logger.info("Starting the process of deleting a product.")
        try:
            # Установка масштаба страницы
            self.browser.execute_script("document.body.style.zoom='75%'")
            self.logger.debug("Set page zoom to 75%.")

            # Ввод имени продукта для поиска
            with allure.step("Entering product name 'Xiaomi 12x' in the input field"):
                self.logger.debug("Clicking on the name input field.")
                self.find_clickable(self.NAME_INPUT).click()
                self.logger.debug("Entering product name 'Xiaomi 12x' in the input field.")
                self.find(self.NAME_INPUT).send_keys('Xiaomi 12x')

            # Применение фильтра
            with allure.step("Applying filter to find the product"):
                self.logger.debug("Clicking on the filter button.")
                self.find(self.BUTTON_FILTER).click()

            # Выбор продукта для удаления
            with allure.step("Selecting the product for deletion"):
                self.logger.debug("Clicking on the checkbox for the product.")
                self.find_clickable(self.CHECKBOX).click()
                self.logger.debug("Clicking on the product to select it for deletion.")
                self.find(self.MOLOKO).click()

            # Удаление продукта
            with allure.step("Deleting the product"):
                self.logger.debug("Clicking on the delete button.")
                self.find(self.BUTTON_DELETE).click()

                self.logger.info("Waiting for confirmation alert to appear.")
                WebDriverWait(self.browser, 5).until(EC.alert_is_present())

                alert = self.browser.switch_to.alert
                self.logger.info("Accepting the alert to confirm deletion.")
                alert.accept()

            # Очистка поля ввода и повторный поиск для подтверждения удаления
            with allure.step("Confirming deletion by searching for the product again"):
                self.logger.debug("Clearing the name input field.")
                self.find_clickable(self.NAME_INPUT).click()

                self.logger.debug("Clearing previous input by sending backspace keys.")
                self.find_clickable(self.NAME_INPUT).send_keys('\b' * 10)

                self.logger.debug("Re-entering product name 'Xiaomi 12x' in the input field.")
                self.find_clickable(self.NAME_INPUT).send_keys('Xiaomi 12x')

                self.logger.debug("Clicking on the filter button again.")
                self.find(self.BUTTON_FILTER).click()

                self.logger.info("Waiting for 'No results!' text to confirm deletion.")
                WebDriverWait(self.browser, 10).until(
                    EC.text_to_be_present_in_element(self.EXCEPTION_ELEMENT, 'No results!'))

        except Exception as e:
            # Логирование и прикрепление скриншота при ошибке
            self.logger.error(f"Error while deleting product: {str(e)}")
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="deletion_error_screenshot",
                attachment_type=allure.attachment_type.PNG)