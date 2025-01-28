from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage, BasePage


# 1. Проверка тайтла на главной странице
def test_check_title(browser):
    MainPage(browser).open_url()
    assert "Your Store" in browser.title

# 2. Проверка наличия элемента Featured на главной странице
def test_check_element_featured(browser):
    MainPage(browser).open_url()
    assert MainPage(browser).find(MainPage.FEATURED_ELEMENT_SELECTOR).is_displayed

# 3. Проверка наличия кнопки Корзина на главной странице
def test_check_button_basket(browser):
    MainPage(browser).open_url()
    element = BasePage(browser).find(BasePage.BASKET_BUTTON)
    assert element.is_displayed()

# 4. Проверка наличия кнопки Поиск на главной странице
def test_check_button_search(browser):
    MainPage(browser).open_url()
    assert MainPage(browser).find(BasePage.SEARCH_BUTTON).is_displayed()

# 5. Проверка наличия кнопок баннера-карусели
def test_check_elements_banner(browser):
    MainPage(browser).open_url()
    assert MainPage(browser).find(MainPage.BANNER_DAT_LEFT_SELECTOR).is_displayed()
    assert MainPage(browser).find(MainPage.BANNER_DAT_RIGHT_SELECTOR).is_displayed()

# 6. Проверка работоспособности карусели на главной странице
def test_check_element_carousel(browser):
    MainPage(browser).open_url()
    element = MainPage(browser).get_carousel_element()
    initial_class = element.get_attribute("class") # Получаем значение атрибута class элемента карусели

    # Функция проверяет, изменился ли класс элемента
    def check_class_change(browser):
        current_class = MainPage(browser).find_change_carousel(MainPage.CAROUSEL_SELECTOR).get_attribute("class")
        return current_class != initial_class

    WebDriverWait(browser, 5).until(check_class_change) #Ожидаем изменения значения атрибута class
    update_class = element.get_attribute("class")
    assert initial_class != update_class