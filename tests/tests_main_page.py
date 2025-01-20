from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import search_button_selector
from pages.main_page import MainPage, BasePage, featured_element_selector, \
    banner_dat_left_selector, banner_dat_right_selector, carousel_selector

# 1. Проверка тайтла на главной странице
def test_check_title(browser):
    MainPage(browser).open_url()
    assert "Your Store" in browser.title

# 2. Проверка наличия элемента Featured на главной странице
def test_check_element_featured(browser):
    MainPage(browser).open_url()
    assert MainPage(browser).find(featured_element_selector).is_displayed

# 3. Проверка наличия кнопки Корзина на главной странице
def test_check_button_basket(browser):
    MainPage(browser).open_url()
    assert BasePage(browser).get_button_basket().is_displayed()

# 4. Проверка наличия кнопки Поиск на главной странице
def test_check_button_search(browser):
    MainPage(browser).open_url()
    assert MainPage(browser).find(search_button_selector).is_displayed()

# 5. Проверка наличия кнопок баннера-карусели
def test_check_elements_banner(browser):
    MainPage(browser).open_url()
    assert MainPage(browser).find(banner_dat_left_selector).is_displayed()
    assert MainPage(browser).find(banner_dat_right_selector).is_displayed()

# 6. Проверка работоспособности карусели на главной странице
def test_check_element_carousel(browser):
    MainPage(browser).open_url()
    element = MainPage(browser).get_carousel_element()
    initial_class = element.get_attribute("class") # Получаем значение атрибута class элемента карусели

    # Функция проверяет, изменился ли класс элемента
    def check_class_change(browser):
        current_class = MainPage(browser).find_change_carousel(carousel_selector).get_attribute("class")
        return current_class != initial_class

    WebDriverWait(browser, 5).until(check_class_change) #Ожидаем изменения значения атрибута class
    update_class = element.get_attribute("class")
    assert initial_class != update_class