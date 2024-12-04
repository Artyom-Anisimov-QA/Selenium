from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest

# 1. Проверка тайтла на главной странице
def test_check_title(browser, base_url):
    browser.get(base_url)
    assert "Your Store" in browser.title

# 2. Проверка наличия элемента Featured на главной странице
def test_check_element_featured(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 5)
    message = wait.until(EC.presence_of_element_located((By.XPATH, '//*[text()="Featured"]')))
    assert message.is_displayed()

# 3. Проверка наличия кнопки Корзина на главной странице
def test_check_button_basket(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 5)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="header-cart"]/div/button')))
    assert element.is_displayed()

# 4. Проверка наличия кнопки Поиск на главной странице
def test_check_button_search(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 5)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search"]/button')))
    assert element.is_displayed()

# 5. Проверка текста в дропдауне после клика на кнопку Корзина
def test_check_text_in_dropdown(browser, base_url):
    expected_text = "Your shopping cart is empty!"
    browser.get(base_url)
    browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button').click()
    wait = WebDriverWait(browser, 5)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="header-cart"]/div/ul/li')))
    assert expected_text in element.text

# 6. Проверка наличия кнопок баннера-карусели
def test_check_elements_banner(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 5)
    element1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="carousel-banner-0"]/div[1]/button[1]')))
    element2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="carousel-banner-0"]/div[1]/button[2]')))
    assert element1.is_displayed()
    assert element2.is_displayed()


# 7. Проверка работоспособности карусели
def test_check_element_carousel(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="carousel-banner-0"]/div[2]/div[1]')))

    #Получаем значение атрибута class элемента карусели
    initial_class = element.get_attribute("class")
    print(f"Initial class: {initial_class}")

    #Функция проверяет, изменился ли класс элемента
    def check_class_change(driver):
        current_class = driver.find_element(By.XPATH, '//*[@id="carousel-banner-0"]/div[2]/div[1]').get_attribute("class")
        return current_class != initial_class

    #Ожидаем изменения значения атрибута class
    wait.until(check_class_change)
    update_class = element.get_attribute("class")
    print(f"Update class: {update_class}")

    assert initial_class != update_class

# 8. Проверка функции добавления случайного товара в корзину
def test_check_add_item_in_basket(browser, base_url):
    browser.get(base_url)

    #Ищем элемент  и кликаем по нему
    element_camera = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/div/div[1]/a/img')
    element_camera.location_once_scrolled_into_view
    element_camera.click()

    wait = WebDriverWait(browser, 10)
    initial_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#product-info > ul > li:nth-child(2) > a')))

    # Находим дропдаун с опциями выбора цвета
    dropdown_select = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-option-226"]')))
    dropdown_select.click()

    # Выбираем опцию в дропдауне
    options_red = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-option-226"]/option[2]')))
    options_red.click()

    # Ищем кнопку Add to Cart и кликаем по ней
    action = ActionChains(browser)
    button_addtocart = browser.find_element(By.XPATH, '//*[text()="Add to Cart"]')
    action.move_to_element(button_addtocart).click().perform()

    # Ожидаем пропадания всплывающего уведомления
    old_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="alert"]/div')))
    wait.until(EC.staleness_of(old_element))

    # Ищем кнопку Корзина и кликаем по ней
    button_basket = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button/i/parent::*')
    action.move_to_element(button_basket).click().perform()

    expected_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#header-cart > div > ul > li > table > tbody > tr > td.text-start > a')))

    assert initial_element.text == expected_element.text, 'Название товара на главной странице не соотвествет названию товара в корзине'


# 9. Проверка, что при переключении валют цены на товары меняются на главной странице
def test_change_cureency_on_main_page(browser, base_url):
    browser.get(base_url)

    #Получаем значение цен товара в $
    price_macbook_us_dollar = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/div/div/span[1]').text
    price_iphone_us_dollar = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div/div/span[1]').text
    price_apple_cinema_us_dollar = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div[2]/div/div/span[1]').text
    price_canon_eos_5d_us_dollar = browser.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[4]/div/div[2]/div/div/span[1]').text

    #Записываем в переменную значение цен
    old_price_macbook_us_dollar = price_macbook_us_dollar
    old_price_iphone_us_dollar = price_iphone_us_dollar
    old_price_apple_cinema_us_dollar = price_apple_cinema_us_dollar
    old_price_canon_eos_5d_us_dollar = price_canon_eos_5d_us_dollar

    #Меняем валюту на фунты стерлинги и проверяем изменение цены товара
    dropdown_currency = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span')
    dropdown_currency.click()

    #В открывшемся дропдауне выбираем фунты и кликаем
    pound_sterling = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]/a')
    pound_sterling.click()

    # В ждём прогрузки страницы и проверяем зменение цен
    wait = WebDriverWait(browser, 5)
    price_macbook_pound_sterling = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/div/div/span[1]'))).text
    price_iphone_pound_sterling = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div/div/span[1]'))).text
    price_apple_cinema_pound_sterling = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div[2]/div/div/span[1]'))).text
    price_canon_eos_5d_pound_sterling = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[4]/div/div[2]/div/div/span[1]'))).text

    assert old_price_macbook_us_dollar != price_macbook_pound_sterling, 'Цена товара не изменилась при смене валюты'
    assert old_price_iphone_us_dollar != price_iphone_pound_sterling, 'Цена товара не изменилась при смене валюты'
    assert old_price_apple_cinema_us_dollar != price_apple_cinema_pound_sterling, 'Цена товара не изменилась при смене валюты'
    assert old_price_canon_eos_5d_us_dollar != price_canon_eos_5d_pound_sterling, 'Цена товара не изменилась при смене валюты'























