from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# 1. Проверка наличия элементов в каталоге Laptops & Notebooks
def test_check_elements(browser, base_url):
    browser.get(base_url + '/en-gb/catalog/laptop-notebook')
    wait = WebDriverWait(browser, 3)
    desctops = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-left"]/div[1]/a[1]')))
    laptops_notebooks = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-left"]/div[1]/a[2]')))
    macs = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-left"]/div[1]/a[3]')))
    windows = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-left"]/div[1]/a[4]')))
    components = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-left"]/div[1]/a[5]')))
    tablets = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-left"]/div[1]/a[6]')))
    software = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-left"]/div[1]/a[7]')))
    phones = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-left"]/div[1]/a[8]')))
    cameras = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-left"]/div[1]/a[9]')))
    mp3players = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-left"]/div[1]/a[10]')))

    assert desctops.is_displayed()
    assert laptops_notebooks.is_displayed()
    assert macs.is_displayed()
    assert windows.is_displayed()
    assert components.is_displayed()
    assert tablets.is_displayed()
    assert software.is_displayed()
    assert phones.is_displayed()
    assert cameras.is_displayed()
    assert mp3players.is_displayed()
    assert desctops.text == "Desktops (13)"
    assert laptops_notebooks.text == "Laptops & Notebooks (5)"
    assert macs.text == "   - Macs (0)"
    assert windows.text == "   - Windows (0)"
    assert components.text == "Components (2)"
    assert tablets.text == "Tablets (1)"
    assert software.text == "Software (0)"
    assert phones.text == "Phones & PDAs (3)"
    assert cameras.text == "Cameras (2)"
    assert mp3players.text == "MP3 Players (4)"

# 2. Проверка наличия элемента счётчик в каталоге
def test_check_counter(browser, base_url):
    browser.get(base_url + '/en-gb/catalog/laptop-notebook')
    wait = WebDriverWait(browser, 3)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[5]/div[2]')))

    assert element.is_displayed()

# 3. Проверка открытия дропдауна с выбором отображаемых элементов на странице.
def test_check_dropdown_pagination(browser, base_url):
    browser.get(base_url + '/en-gb/catalog/laptop-notebook')
    wait = WebDriverWait(browser, 3)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-limit"]')))
    element.click()

    assert (browser.find_element(By.XPATH, '//*[@id="input-limit"]/option[1]').text == "10")
    assert (browser.find_element(By.XPATH, '//*[@id="input-limit"]/option[2]').text == "25")
    assert (browser.find_element(By.XPATH, '//*[@id="input-limit"]/option[3]').text == "50")
    assert (browser.find_element(By.XPATH, '//*[@id="input-limit"]/option[4]').text == "75")
    assert (browser.find_element(By.XPATH, '//*[@id="input-limit"]/option[5]').text == "100")

# 4. Проверка открытия дропдауна с сортировкой.
def test_check_dropdown_sort_by(browser, base_url):
    browser.get(base_url + '/en-gb/catalog/laptop-notebook')
    wait = WebDriverWait(browser, 3)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-sort"]')))
    element.click()

    assert browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[1]').is_displayed()
    assert browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[2]').is_displayed()
    assert browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[3]').is_displayed()
    assert browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[4]').is_displayed()
    assert browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[5]').is_displayed()
    assert browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[6]').is_displayed()
    assert browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[7]').is_displayed()
    assert browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[8]').is_displayed()
    assert browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[9]').is_displayed()
    assert (browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[1]').text == "Default")
    assert (browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[2]').text == "Name (A - Z)")
    assert (browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[3]').text == "Name (Z - A)")
    assert (browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[4]').text == "Price (Low > High)")
    assert (browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[5]').text == "Price (High > Low)")
    assert (browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[6]').text == "Rating (Highest)")
    assert (browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[7]').text == "Rating (Lowest)")
    assert (browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[8]').text == "Model (A - Z)")
    assert (browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[9]').text == "Model (Z - A)")


# 5. Проверка наличия элемента grid в каталоге
def test_check_element_grid(browser, base_url):
    browser.get(base_url + '/en-gb/catalog/laptop-notebook')
    wait = WebDriverWait(browser, 3)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="button-grid"]')))
    assert element.is_displayed()

# 6. Проверка, что при переключении валют цены на товары меняются в каталоге
def test_change_cureency_on_catalog(browser, base_url):
    browser.get(base_url + '/en-gb/catalog/laptop-notebook')
    wait = WebDriverWait(browser, 5)

    #Получаем значение цен товара в $
    price_hp_lp3065_us_dollar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/div/div/span[1]'))).text
    price_macbook_us_dollar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="product-list"]/div[2]/div/div[2]/div/div/span[1]'))).text
    price_macbook_air_us_dollar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="product-list"]/div[3]/div/div[2]/div/div/span[1]'))).text
    price_macbook_pro_us_dollar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="product-list"]/div[4]/div/div[2]/div/div/span[1]'))).text
    price_sony_vaio_us_dollar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="product-list"]/div[5]/div/div[2]/div/div/span[1]'))).text

    #Записываем в переменную значение цен
    old_price_hp_lp3065_us_dollar = price_hp_lp3065_us_dollar
    old_price_macbook_us_dollar = price_macbook_us_dollar
    old_price_macbook_air_us_dollar = price_macbook_air_us_dollar
    old_price_macbook_pro_us_dollar = price_macbook_pro_us_dollar
    old_price_sony_vaio_us_dollar = price_sony_vaio_us_dollar

    #Меняем валюту на фунты стерлинги и проверяем изменение цены товара
    dropdown_currency = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span')
    dropdown_currency.click()

    #В открывшемся дропдауне выбираем фунты и кликаем
    pound_sterling = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]/a')
    pound_sterling.click()

    # В ждём прогрузки страницы и проверяем зменение цен
    price_hp_lp3065_pound_sterling = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/div/div/span[1]'))).text
    price_macbook_pound_sterling = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="product-list"]/div[2]/div/div[2]/div/div/span[1]'))).text
    price_macbook_air_pound_sterling = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="product-list"]/div[3]/div/div[2]/div/div/span[1]'))).text
    price_macbook_pro_pound_sterling = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="product-list"]/div[4]/div/div[2]/div/div/span[1]'))).text
    price_sony_vaio_pound_sterling = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="product-list"]/div[5]/div/div[2]/div/div/span[1]'))).text

    assert old_price_hp_lp3065_us_dollar != price_hp_lp3065_pound_sterling, 'Цена товара не изменилась при смене валюты'
    assert old_price_macbook_us_dollar != price_macbook_pound_sterling, 'Цена товара не изменилась при смене валюты'
    assert old_price_macbook_air_us_dollar != price_macbook_air_pound_sterling, 'Цена товара не изменилась при смене валюты'
    assert old_price_macbook_pro_us_dollar != price_macbook_pro_pound_sterling, 'Цена товара не изменилась при смене валюты'
    assert old_price_sony_vaio_us_dollar != price_sony_vaio_pound_sterling, 'Цена товара не изменилась при смене валюты'
