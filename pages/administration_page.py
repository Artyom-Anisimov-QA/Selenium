import os
import mysql.connector
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# Локаторы страницы
login_selector = (By.XPATH, '//*[@id="input-username"]')
passwd_selector = (By.XPATH, '//*[@id="input-password"]')
username_selector = (By.XPATH, '//*[@id="form-login"]/div[1]/label')
password_elem_selector = (By.XPATH, '//*[@id="form-login"]/div[2]/label')
button_login_selector = (By.XPATH, '//*[@id="form-login"]/div[3]/button')
menu_catalog_selector = (By.XPATH, '//*[@id="menu-catalog"]/a')
menu_customers_selector = (By.XPATH, '//*[@id="menu-customer"]/a')
menu_products_selector = (By.XPATH, '//*[@id="collapse-1"]/li[2]/a')
element_customers_selector = (By.XPATH, '//*[@id="collapse-5"]/li[1]/a')
add_new_selector = (By.XPATH, '//*[@id="content"]/div[1]/div/div/a/i')
product_name_selector = (By.XPATH, '//*[@id="input-name-1"]')
meta_tag_title_selector = (By.XPATH, '//*[@id="input-meta-title-1"]')
menu_data_selector =(By.XPATH, '//*[@id="form-product"]/ul/li[2]/a')
menu_image_selector =(By.XPATH, '//*[@id="form-product"]/ul/li[9]/a')
menu_seo_selector =(By.XPATH, '//*[@id="form-product"]/ul/li[11]/a')
model_input_selector =(By.XPATH, '//*[@id="input-model"]')
price_input_selector =(By.XPATH, '//*[@id="input-price"]')
keyword_input_selector =(By.XPATH, '//*[@id="input-keyword-0-1"]')
name_input_selector =(By.XPATH, '//*[@id="input-name"]')
email_input_selector =(By.XPATH, '//*[@id="input-email"]')
button_edit_selector =(By.XPATH, '//*[@id="image"]/div/button[1]')
button_save_selector =(By.XPATH, '//*[@id="content"]/div[1]/div/div/button/i')
button_filter_selector =(By.XPATH, '//*[@id="button-filter"]')
button_delete_selector =(By.XPATH, '//*[@id="content"]/div[1]/div/div/button[3]')
button_logout_selector =(By.XPATH, '//*[@id="nav-logout"]/a/span')
image_selector = (By.XPATH, '//*[@id="filemanager"]/div/div[2]/div[3]/div[3]/div[1]/a/img')
to_end_element_selector = (By.XPATH, '//*[@id="form-product"]/div[2]/div[1]/ul/li[5]/a')
expection_alert_selector = (By.XPATH, '//*[@id="alert"]/div')
checkbox_selector = (By.XPATH, '//*[@id="form-product"]/div[1]/table/thead/tr/td[1]/input')
expection_element_selector = (By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr/td')
expection_email_selector = (By.XPATH, '//*[@id="form-customer"]/div[1]/table/tbody/tr/td[3]')
moloko = (By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div/div[1]')

# Класс страницы
class AdminPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser) # передаём browser родительскому классу

    # Метод открывает url страницы в браузере
    def open_url(self):
        self.browser.get("http://192.168.0.144:8081/administration/")

    # Методы для страницы
    # Метод авторизации в админке
    def sing_in(self):
        login = self.find(login_selector)
        password = self.find(passwd_selector)
        login.send_keys('user')
        password.send_keys('bitnami')
        self.find_clickable(button_login_selector).click()

    # Метод разлогина из админки
    def sing_out(self):
        self.find_clickable(button_logout_selector).click()

    # Метод открытия меню для добавления нового продукта
    def open_menu_products(self):
        self.find_clickable(menu_catalog_selector).click()
        self.find_clickable(menu_products_selector).click()

    # Метод проверки пользователей opencart
    def open_customer_list(self):
        self.find_clickable(menu_customers_selector).click()
        self.find_clickable(element_customers_selector).click()

    # Метод поиска пользователя
    def search_customer(self):
        filename = 'email.txt'
        with open(filename, 'r') as file:
            initial_email = file.read()
        os.remove(filename)

        self.browser.execute_script("document.body.style.zoom='75%'")
        self.find(email_input_selector).click()
        self.find(email_input_selector).send_keys(initial_email)
        WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(button_filter_selector))
        self.find(button_filter_selector).click()
        expected_email = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(expection_email_selector)).text
        assert expected_email == initial_email

    # Метод добавления нового продукта в Products
    def add_new_product(self):
        self.browser.execute_script("document.body.style.zoom='70%'")
        self.find_clickable(add_new_selector).click() # кликаем по элементу "+"
        self.browser.execute_script("document.body.style.zoom='50%'")
        self.find_clickable(product_name_selector).click()
        self.find_clickable(product_name_selector).send_keys('Xiaomi 12x')
        self.find_clickable(meta_tag_title_selector).click()
        self.find_clickable(meta_tag_title_selector).send_keys('Xiaomi 12x')
        self.find_clickable(menu_data_selector).click()
        self.find_clickable(model_input_selector).click()
        self.find_clickable(model_input_selector).send_keys('Product 25')
        self.browser.execute_script("document.body.style.zoom='50%'")
        self.find_clickable(price_input_selector).click()
        self.find_clickable(price_input_selector).send_keys('750$')
        self.browser.execute_script("document.body.style.zoom='60%'")
        self.find_clickable(menu_image_selector).click()
        self.find(button_edit_selector).click()
        self.find(image_selector).click()
        self.find(menu_seo_selector).click()
        self.find(keyword_input_selector).send_keys('Xiaomi_12x')
        self.find(button_save_selector).click()
        expected = self.find(expection_alert_selector)
        print(expected.text)
        assert expected.text == 'Success: You have modified products!'

# Метод удаления продукта из списка Products
    def delete_product(self):
        self.browser.execute_script("document.body.style.zoom='75%'")
        self.find_clickable(name_input_selector).click()
        self.find(name_input_selector).send_keys('Xiaomi 12x')
        self.find(button_filter_selector).click()
        self.find_clickable(checkbox_selector).click()
        self.find(moloko).click()
        self.find(button_delete_selector).click()
        WebDriverWait(self.browser, 5).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        alert.accept()
        self.find_clickable(name_input_selector).click()
        self.find_clickable(name_input_selector).send_keys('\b'*10)
        self.find_clickable(name_input_selector).send_keys('Xiaomi 12x')
        time.sleep(3)
        self.find(button_filter_selector).click()
        WebDriverWait(self.browser,3).until(EC.text_to_be_present_in_element(expection_element_selector, 'No results!'))