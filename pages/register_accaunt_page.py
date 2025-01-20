from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import generate_random_user
from pages.base_page import BasePage

# Локаторы страницы
checkbox_subscribe_selector = (By.XPATH, '//*[@id="input-newsletter"]')
checkbox_policy_selector = (By.XPATH, '//*[@id="form-register"]/div/div/input')
button_continue_selector = (By.XPATH, '//*[text()="Continue"]')
button_continue_acc_created_selector = (By.XPATH, '//*[@id="content"]/div/a')
input_first_name_selector = (By.XPATH, '//*[@id="input-firstname"]')
input_last_name_selector = (By.XPATH, '//*[@id="input-lastname"]')
input_email_selector = (By.XPATH, '//*[@id="input-email"]')
input_password_selector = (By.XPATH, '//*[@id="input-password"]')
expected_element_selector = (By.XPATH, '//*[@id="content"]/h1')
element_moloko = (By.XPATH, '//*[@id="form-register"]/fieldset[3]/legend')

# Класс страницы
class RegisterPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser) # передаём browser родительскому классу

    # Метод открывает url страницы в браузере
    def open_url(self):
        self.browser.get("http://192.168.0.144:8081/en-gb?route=account/register")

    # Методы для страницы
    # Метод создаёт нового пользователя в opencart
    def create_new_user(self):
        new_user = generate_random_user()
        first_name = new_user[0]
        last_name = new_user[1]
        email = new_user[2]
        password = new_user[3]

        self.browser.execute_script("document.body.style.zoom='75%'")
        self.find_clickable(input_first_name_selector).send_keys(first_name)
        self.find_clickable(input_last_name_selector).send_keys(last_name)
        self.find_clickable(input_email_selector).send_keys(email)
        self.find(element_moloko).click()
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        password_element = self.find_clickable(input_password_selector)
        password_element.send_keys(password)
        WebDriverWait(self.browser,3).until(EC.visibility_of_element_located(checkbox_policy_selector))
        self.find_clickable(checkbox_policy_selector).click()
        WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(button_continue_selector))
        self.find_clickable(button_continue_selector).click()
        WebDriverWait(self.browser, 5).until(
            EC.text_to_be_present_in_element(expected_element_selector, 'Your Account Has Been Created!'))

        # Запись email в .txt файл
        with open('email.txt', 'a') as file:
            file.write(email)

        return email

    # Метод ищет элемент checkbox_subscribe
    def get_element_checkbox_subscribe(self):
        return self.find_clickable(checkbox_subscribe_selector)

    # Метод ищет элемент checkbox_policy
    def get_element_checkbox_policy(self):
        return self.find_clickable(checkbox_policy_selector)

    # Метод ищет элемент кнопку continue
    def get_element_button_continue(self):
        return self.find_clickable(button_continue_selector)