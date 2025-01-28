from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.product_cart_page import ProductCartPage

# 1. Проверка тайтла в карточке товара
def test_check_title(browser):
    ProductCartPage(browser).open_url()
    assert "HP LP3065" in browser.title

# 2. Проверка вкладки Specification в карточке товара
def test_check_specification(browser):
    ProductCartPage(browser).open_url()
    browser.execute_script("document.body.style.zoom='55%'")
    ProductCartPage(browser).get_specification()
    ProductCartPage(browser).check_list_strong_item()

# 3. Проверка вкладки Reviews в карточке товара
def test_check_reviews(browser):
    ProductCartPage(browser).open_url()
    browser.execute_script("document.body.style.zoom='50%'")
    ProductCartPage(browser).get_reviews()
    ProductCartPage(browser).check_list_label_item()

# 4. Проверка кнопки remove в корзине
def test_check_button_remove(browser):
    MainPage(browser).open_url()
    MainPage(browser).get_item()  # Ищем элемент и кликаем по нему
    browser.execute_script("document.body.style.zoom='75%'")
    initial_text = ProductCartPage(browser).get_initial_name_item().text
    ProductCartPage(browser).get_dropdown()  # Ищем дропдаун и кликаем по нему
    ProductCartPage(browser).get_options_red()  # Выбираем опцию RED и кликаем
    button_addcart = ProductCartPage(browser).get_button_addtocart()  # Ищем кнопку Add to Cart
    BasePage(browser).custom_click(button_addcart)  # Кликаем по кнопке кнопку Add to Cart
    BasePage(browser).get_popup_window_down()  # Ожидаем пропадания всплывающего уведомления
    BasePage(browser).get_button_cart_shopping.click()  # Ищем кнопку Корзина
    expected_text = ProductCartPage(browser).get_empty_cart_shopping().text
    assert initial_text != expected_text