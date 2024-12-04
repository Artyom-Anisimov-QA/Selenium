from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest

#1. Проверка тайтла на странице Register Account
def test_check_title_register_account(browser, base_url):
    browser.get(base_url + '/en-gb?route=account/register')
    wait = WebDriverWait(browser, 3)
    assert wait.until(EC.title_is('Register Account'))

#2. Проверка чекбокса Subscribe на странице Register Account
def test_check_checkbox_subscribe(browser, base_url):
    browser.get(base_url + '/en-gb?route=account/register')
    wait = WebDriverWait(browser, 3)
    checkbox_subscribe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-newsletter"]')))
    assert checkbox_subscribe.is_displayed()

#3. Проверка чекбокса 'I have read and agree to the Privacy Policy' на странице Register Account
def test_check_checkbox_privacy_policy(browser, base_url):
    browser.get(base_url + '/en-gb?route=account/register')
    wait = WebDriverWait(browser, 3)
    checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-register"]/div/div/input')))
    assert checkbox.is_displayed()

#4. Проверка наличия кнопки Continue на странице Register Account
def test_check_button_continue(browser, base_url):
    browser.get(base_url + '/en-gb?route=account/register')
    wait = WebDriverWait(browser, 3)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Continue"]')))
    assert button.is_displayed()
    assert button.is_enabled()

#5. Проверка регистрации пользователя на странице Register Account
def test_check_register_user(browser, base_url):
    browser.get(base_url + '/en-gb?route=account/register')

    #Находим инпуты
    input_first_name = browser.find_element(By.XPATH, '//*[@id="input-firstname"]')
    input_last_name = browser.find_element(By.XPATH, '//*[@id="input-lastname"]')
    input_email = browser.find_element(By.XPATH, '//*[@id="input-email"]')
    input_password = browser.find_element(By.XPATH, '//*[@id="input-password"]')

    #Вводим данные в инпуты
    input_first_name.send_keys('Joel')
    input_last_name.send_keys('Madden')
    input_email.send_keys('gc25@gc.com')
    input_password.send_keys('1234567')

    #Кликаем чекбоксы
    checkbox = browser.find_element(By.XPATH, '//*[@id="form-register"]/div/div/input')
    actions = ActionChains(browser)
    actions.move_to_element(checkbox).click().perform()

    #Кликаем на кнопку Continue
    button_continue = browser.find_element(By.XPATH, '//*[text()="Continue"]')
    actions = ActionChains(browser)
    actions.move_to_element(button_continue).click().perform()

    #Ожидаем появления сообщения об успешной регистрации
    wait = WebDriverWait(browser,5)
    wait.until(EC.title_is('Your Account Has Been Created!'))

    #Проверяем, что сообщение об успешной регистрации отображается
    expected_message = browser.find_element(By.XPATH, '//h1')

    assert expected_message.text == 'Your Account Has Been Created!', 'Ожидалось сообщение о создании аккаунта.'










