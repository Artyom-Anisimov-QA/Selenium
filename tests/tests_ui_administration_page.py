from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


#1. Проверка логин/разлогин на странице Administration
def test_check_login_logout_admin_page(browser, base_url):
    browser.get(base_url + '/administration/index.php?route=common/login')
    login_input = browser.find_element(By.XPATH, '//*[@id="input-username"]')
    passwd_input = browser.find_element(By.XPATH, '//*[@id="input-password"]')
    login_input.send_keys('user')
    passwd_input.send_keys('bitnami')
    button_login = browser.find_element(By.XPATH, '//*[@id="form-login"]/div[3]/button')
    button_login.click()
    wait = WebDriverWait(browser, 5)
    user_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="nav-profile"]/a/span'))).text
    assert user_element == '   John Doe'
    assert wait.until(EC.title_is('Dashboard'))
    button_logout = browser.find_element(By.XPATH, '//*[@id="nav-logout"]/a')
    button_logout.click()
    assert wait.until(EC.title_is('Administration'))

#2. Проверка наличия инпута Username на странице Administration
def test_check_input_username_admin_page(browser, base_url):
    browser.get(base_url + '/administration/index.php?route=common/login')
    wait = WebDriverWait(browser,3)
    input_username = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-username"]')))
    assert input_username.is_displayed()
    assert input_username.get_attribute('name') == 'username'

#3. Проверка наличия элемента Username на странице Administration
def test_check_element_username_admin_page(browser, base_url):
    browser.get(base_url + '/administration/index.php?route=common/login')
    wait = WebDriverWait(browser,3)
    element_username = wait.until(EC.presence_of_element_located((By.XPATH, '//*[text()="Username"]')))
    assert element_username.is_displayed()
    assert element_username.text == 'Username'

#4. Проверка наличия инпута Password на странице Administration
def test_check_input_password_admin_page(browser, base_url):
    browser.get(base_url + '/administration/index.php?route=common/login')
    wait = WebDriverWait(browser,3)
    input_password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-password"]')))
    assert input_password.is_displayed()
    assert input_password.get_attribute('name') == 'password'

#5. Проверка наличия элемента Username на странице Administration
def test_check_element_password_admin_page(browser, base_url):
    browser.get(base_url + '/administration/index.php?route=common/login')
    wait = WebDriverWait(browser,3)
    element_password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[text()="Password"]')))
    assert element_password.is_displayed()
    assert element_password.text == 'Password'













