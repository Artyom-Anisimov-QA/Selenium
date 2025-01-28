import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import generate_random_user
from pages.base_page import BasePage

# Класс страницы
class RegisterPage(BasePage):
    # Локаторы страницы
    CHECKBOX_SUBSCRIBE = (By.XPATH, '//*[@id="input-newsletter"]')
    CHECKBOX_POLICY = (By.XPATH, '//*[@id="form-register"]/div/div/input')
    BUTTON_CONTINUE = (By.XPATH, '//*[text()="Continue"]')
    BUTTON_CONTINUE_ACC_CREATED = (By.XPATH, '//*[@id="content"]/div/a')
    INPUT_FIRST_NAME = (By.XPATH, '//*[@id="input-firstname"]')
    INPUT_LAST_NAME = (By.XPATH, '//*[@id="input-lastname"]')
    INPUT_EMAIL = (By.XPATH, '//*[@id="input-email"]')
    INPUT_PASSWORD = (By.XPATH, '//*[@id="input-password"]')
    EXPECTED_ELEMENT = (By.XPATH, '//*[@id="content"]/h1')
    ELEMENT_MOLKO = (By.XPATH, '//*[@id="form-register"]/fieldset[3]/legend')

    def __init__(self, browser):
        super().__init__(browser) # передаём browser родительскому классу

    # Метод открывает url страницы в браузере
    @allure.step("Opening URL: http://192.168.0.144:8081/en-gb?route=account/register")
    def open_url(self):
        url = "http://192.168.0.144:8081/en-gb?route=account/register"
        self.logger.debug("%s: Opening URL: %s" % (self.class_name, url))
        try:
            self.browser.get(url)
            self.logger.info("%s: Successfully opened URL: %s" % (self.class_name, url))
        except Exception as e:
            self.logger.error("%s: Failed to open URL: %s. Error: %s" % (self.class_name, url, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )


    # Методы для страницы
    # Метод создаёт нового пользователя в opencart
    @allure.step("Starting the process of creating a new user")
    def create_new_user(self):
        try:
            self.logger.info("Starting the process of creating a new user.")

            # Генерация данных пользователя
            new_user = generate_random_user()
            first_name = new_user[0]
            last_name = new_user[1]
            email = new_user[2]
            password = new_user[3]

            self.logger.debug(f"Generated user details: {first_name} {last_name}, Email: {email}")

            # Уменьшение масштаба страницы
            self.browser.execute_script("document.body.style.zoom='75%'")

            # Заполнение имени
            with allure.step("Entering first name"):
                self.logger.debug("Entering first name.")
                self.find_clickable(self.INPUT_FIRST_NAME).send_keys(first_name)

            # Заполнение фамилии
            with allure.step("Entering last name"):
                self.logger.debug("Entering last name.")
                self.find_clickable(self.INPUT_LAST_NAME).send_keys(last_name)

            # Заполнение email
            with allure.step("Entering email"):
                self.logger.debug("Entering email.")
                self.find_clickable(self.INPUT_EMAIL).send_keys(email)

            # Клик по чекбоксу
            with allure.step("Clicking on the checkbox"):
                self.logger.debug("Clicking on the checkbox.")
                self.find(self.ELEMENT_MOLKO).click()

            # Скролл к полю пароля
            with allure.step("Scrolling down to the password input field"):
                self.logger.debug("Scrolling down to the password input field.")
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Заполнение пароля
            with allure.step("Entering password"):
                self.logger.debug("Entering password.")
                password_element = self.find_clickable(self.INPUT_PASSWORD)
                password_element.send_keys(password)

            # Ожидание и клик по чекбоксу политики
            with allure.step("Clicking on the policy checkbox"):
                self.logger.info("Waiting for the policy checkbox to be visible.")
                WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(self.CHECKBOX_POLICY))
                self.logger.debug("Clicking on the policy checkbox.")
                self.find_clickable(self.CHECKBOX_POLICY).click()

            # Ожидание и клик по кнопке продолжения
            with allure.step("Clicking on the continue button"):
                self.logger.info("Waiting for the continue button to be visible.")
                WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(self.BUTTON_CONTINUE))
                self.logger.debug("Clicking on the continue button.")
                self.find_clickable(self.BUTTON_CONTINUE).click()

            # Ожидание подтверждения создания аккаунта
            with allure.step("Waiting for confirmation message after account creation"):
                self.logger.info("Waiting for confirmation message after account creation.")
                WebDriverWait(self.browser, 5).until(
                    EC.text_to_be_present_in_element(self.EXPECTED_ELEMENT, 'Your Account Has Been Created!')
                )

            # Запись email в файл
            with allure.step("Writing email to file"):
                with open('email.txt', 'a') as file:
                    file.write(email + '\n')
                    self.logger.info(f"Email '{email}' has been written to email.txt.")

            # Логирование успешного создания пользователя
            with allure.step("New user created successfully"):
                self.logger.info("New user created successfully.")

            return email

        except Exception as e:
            # Логирование ошибки
            self.logger.error(f"Error!!! New user is not created. Error: {str(e)}")
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )


    # Метод ищет элемент checkbox_subscribe
    @allure.step("Getting the subscribe checkbox element")
    def get_element_checkbox_subscribe(self):
        self.logger.debug("Getting the subscribe checkbox element.")
        return self.find_clickable(self.CHECKBOX_SUBSCRIBE)

    # Метод ищет элемент checkbox_policy
    @allure.step("Getting the policy checkbox element")
    def get_element_checkbox_policy(self):
        self.logger.debug("Getting the policy checkbox element.")
        return self.find_clickable(self.CHECKBOX_POLICY)

    # Метод ищет элемент кнопку continue
    @allure.step("Getting the continue button element")
    def get_element_button_continue(self):
        self.logger.debug("Getting the continue button element.")
        return self.find_clickable(self.BUTTON_CONTINUE)