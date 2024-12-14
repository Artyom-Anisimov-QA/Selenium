from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# 1. Проверка тайтла в карточке товара
def test_check_title(browser, base_url):
    browser.get(base_url + '/en-gb/product/laptop-notebook/hp-lp3065?limit=10')
    assert "HP LP3065" in browser.title

# 2. Проверка функции добавления товара в корзину
def test_check_add_item_in_basket(browser, base_url):
    browser.get(base_url + '/en-gb/product/laptop-notebook/hp-lp3065?limit=10')
    initial_element = browser.find_element(By.XPATH, "//h1")
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add to Cart"]')))
    browser.execute_script("arguments[0].click();", element)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="header-cart"]/div/button')))
    browser.execute_script("arguments[0].click();", element)
    expected_element = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="HP LP3065"]')))

    assert initial_element.text == expected_element.text

# 3. Проверка вкладки Specification в карточке товара
def test_check_specification(browser, base_url):
    browser.get(base_url +'/en-gb/product/laptop-notebook/hp-lp3065?limit=10')
    wait = WebDriverWait(browser, 3)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Specification"]')))
    browser.execute_script("arguments[0].click();", element)
    expected_element1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@colspan="2"]//strong[text()="Memory"]/parent::*')))
    expected_element2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//td[text()="test 1"]')))
    expected_element3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@colspan="2"]//strong[text()="Processor"]/parent::*')))
    expected_element4 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="No. of Cores"]')))
    expected_element5 = wait.until(EC.element_to_be_clickable((By.XPATH, '//td[text()="16GB"]')))
    expected_element6 = wait.until(EC.element_to_be_clickable((By.XPATH, '//td[text()="4"]')))

    assert expected_element1.is_displayed()
    assert expected_element2.is_displayed()
    assert expected_element3.is_displayed()
    assert expected_element4.is_displayed()
    assert expected_element5.is_displayed()
    assert expected_element6.is_displayed()

# 4. Проверка вкладки Reviews в карточке товара
def test_check_reviews(browser, base_url):
    browser.get(base_url + '/en-gb/product/laptop-notebook/hp-lp3065?limit=10')
    wait = WebDriverWait(browser, 3)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@role="presentation"][3]/a')))
    browser.execute_script("arguments[0].click();", element)
    expected_element1 = wait.until(EC.presence_of_element_located((By.XPATH, '//h2[text()="Write a review"]')))
    expected_element2 = wait.until(EC.presence_of_element_located((By.XPATH, '//label[text()="Your Name"]')))
    expected_element3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-name"]')))
    expected_element4 = wait.until(EC.presence_of_element_located((By.XPATH, '//label[text()="Your Review"]')))
    expected_element5 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-text"]')))
    expected_element6 = wait.until(EC.presence_of_element_located((By.XPATH, '//label[text()="Rating"]')))
    expected_element7 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-rating"]')))
    expected_element8 = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Back"]')))
    expected_element9 = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Continue"]')))

    assert expected_element1.is_displayed()
    assert expected_element2.is_displayed()
    assert expected_element3.is_displayed()
    assert expected_element4.is_displayed()
    assert expected_element5.is_displayed()
    assert expected_element6.is_displayed()
    assert expected_element7.is_displayed()
    assert expected_element8.is_displayed()
    assert expected_element9.is_displayed()


# 5. Проверка кнопки remove в корзине
def test_check_button_remove(browser, base_url):
    browser.get(base_url + '/en-gb/product/laptop-notebook/hp-lp3065?limit=10')
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add to Cart"]')))
    browser.execute_script("arguments[0].click();", element)

    # Ожидаем пропадания всплывающего уведомления
    old_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="alert"]/div')))
    wait.until(EC.staleness_of(old_element))

    # Получаем начальный текст кнопки корзины
    initial_price = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-cart"]/div/button'))).text

    # Кликаем по кнопке корзина
    element = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button/i/parent::*')
    browser.execute_script("arguments[0].click();", element)

    # Ожидаем появления крестика для удаления товара и нажимаем его
    remove_item_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="fa-solid fa-circle-xmark"]/parent::*')))
    remove_item_button.click()

    # Ожидаем изменения текста кнопки корзины
    wait.until_not(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="header-cart"]/div/button'), initial_price))

    # Получаем обновленный текст кнопки корзины
    expected_price = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button').text

    assert expected_price != initial_price, 'Элемент Цена на корзине не изменился после удаления позиций!'
