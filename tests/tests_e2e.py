from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.catalog_page import CatalogPage
from pages.checkout import CheckoutPage
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.product_cart_page import ProductCartPage
from pages.administration_page import AdminPage
from pages.register_accaunt_page import RegisterPage

# 1. Проверка, что при переключении валют цены на товары меняются
def test_change_currency(browser):
    CatalogPage(browser).open_url()
    CatalogPage(browser).get_item()
    CatalogPage(browser).get_product_code()
    price_usd = CatalogPage(browser).get_price_item()
    CatalogPage(browser).get_dropdown_currency()
    CatalogPage(browser).get_eur_currency()
    price_euro = CatalogPage(browser).get_price_item()
    assert price_usd != price_euro

# 2. Проверка появления модального окна после клика на кнопку корзина
def test_check_modal_window(browser):
    MainPage(browser).open_url()
    BasePage(browser).get_button_cart_shopping()
    element = BasePage.MODAL_WINDOW
    assert BasePage(browser).find(element).is_displayed()

# 3. Проверка текста в модальном окне после клика по пустой корзине
def test_check_text_in_dropdown(browser):
    expected_text = "Your shopping cart is empty!"
    MainPage(browser).open_url()
    BasePage(browser).get_button_cart_shopping()
    element = BasePage.EMPTY_MODAL_WINDOW
    assert expected_text == BasePage(browser).find(element).text

# 4. Оформить покупку случайного товара
def test_pay_product(browser):
    MainPage(browser).open_url()
    MainPage(browser).get_item()# Ищем элемент и кликаем по нему
    browser.execute_script("document.body.style.zoom='75%'")
    initial_element = ProductCartPage(browser).get_initial_name_item().text
    ProductCartPage(browser).get_dropdown() # Ищем дропдаун и кликаем по нему
    ProductCartPage(browser).get_options_red() # Выбираем опцию RED и кликаем
    button_addcart = ProductCartPage(browser).get_button_addtocart() # Ищем кнопку Add to Cart
    BasePage(browser).custom_click(button_addcart) # Кликаем по кнопке кнопку Add to Cart
    BasePage(browser).get_popup_window_down() # Ожидаем пропадания всплывающего уведомления
    BasePage(browser).get_button_cart_shopping() # Ищем кнопку Корзина
    ProductCartPage(browser).checkout() # Кликаем по кнопке Checkout
    expected_element = ProductCartPage(browser).get_expected_name_item()
    assert CheckoutPage(browser).get_confirm_order().is_displayed()
    assert initial_element == expected_element.text

#5. Проверка логин/разлогин на странице Administration
def test_check_login_logout_admin_page(browser):
    AdminPage(browser).open_url()
    AdminPage(browser).sing_in()
    AdminPage(browser).sing_out()
    assert WebDriverWait(browser, 3).until(EC.title_is('Administration'))

# 6. Добавление нового товара в разделе администратора
def test_add_new_product(browser):
    AdminPage(browser).open_url()
    AdminPage(browser).sing_in() # авторизуемся в админке
    AdminPage(browser).open_menu_products() # открываем меню Products
    AdminPage(browser).add_new_product()

# 7. Удаление товара из списка в разделе администратора
def test_delete_product(browser):
    AdminPage(browser).open_url()
    AdminPage(browser).sing_in() # авторизуемся в админке
    AdminPage(browser).open_menu_products() # открываем меню Products
    AdminPage(browser).delete_product()

# 8. Регистрация нового пользователя в магазине opencart
def test_register_new_user(browser):
    RegisterPage(browser).open_url()
    RegisterPage(browser).create_new_user()
    AdminPage(browser).open_url()
    AdminPage(browser).sing_in()  # авторизуемся в админке
    AdminPage(browser).open_customer_list()
    AdminPage(browser).search_customer()